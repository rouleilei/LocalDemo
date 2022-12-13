import time

import itsdangerous
from itsdangerous import URLSafeTimedSerializer
from fastapi import APIRouter, Request, Response, HTTPException, status
from fastapi.responses import StreamingResponse

from captcha import ImageCaptcha
from config import POOLS, Conf
from repository import UserRepo
from model import UserModel
from utils import generate_token, generate_captcha_code

router = APIRouter(
    prefix="/user",
)

_DB_NAME = 'user'
_COOKIE_NAME = 'fastapiusersauth'
_CAPTCHA_SECRET = "coinbase-captcha"


@router.get("/gen_captcha")
async def admin_gen_captcha():
    code = generate_captcha_code()
    serializer = URLSafeTimedSerializer(_CAPTCHA_SECRET)
    code_id = serializer.dumps(code)
    return code_id


@router.get("/get_captcha")
async def admin_get_captcha(code_id: str):
    serializer = URLSafeTimedSerializer(_CAPTCHA_SECRET)
    code = serializer.loads(code_id)
    image = ImageCaptcha(fonts=["./static/font/DroidSansMono.ttf"])
    data = image.generate(code)
    return StreamingResponse(data, media_type="image/png")


@router.post("/register")
async def register(user: UserModel):
    await UserRepo.insert(user)
    return "ok"


@router.post("/login")
async def login(request: Request, code_id: str, captcha: str, user: UserModel, response: Response):
    # step 1: auth captcha
    serializer = itsdangerous.URLSafeTimedSerializer(_CAPTCHA_SECRET)
    try:
        code = serializer.loads(code_id, max_age=60)
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'BadTimeSignature,reason{str(error)}')
    else:
        if code.lower() != captcha.lower():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BadTimeSignature')

    # step 2: auth user
    now = int(time.time())
    user_obj = await POOLS['MONGODB'][Conf.COLLECTION][_DB_NAME].find_one({'username': user.username})
    if not user_obj:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user")
    if user.password != user_obj.get('password'):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid password")

    # step 3: set cookie
    user_id = str(user_obj.get('_id'))
    log = {
        'user_id': user_id,
        'create_ts': int(time.time()),
    }
    token = generate_token(user_id)
    response.set_cookie(_COOKIE_NAME, token)
    await POOLS['MONGODB'][Conf.COLLECTION]['user_logs'].insert_one(log)

    # step 4: update cookie expiry time
    token_obj = await POOLS['MONGODB'][Conf.COLLECTION]['token'].find_one({'name': user.username, 'token': token})
    if not token_obj:
        await POOLS['MONGODB'][Conf.COLLECTION]['token'].insert_one(
            {'name': user.username, 'token': token, 'create_ts': now}
        )
    else:
        await POOLS['MONGODB'][Conf.COLLECTION]['token'].find_one_and_update(
            {'name': user.username, 'token': token}, {'$set': {'update_ts': now}}
        )
    return 'ok'


@router.get('/logout')
async def logout(request: Request, response: Response):
    response.set_cookie("_cookie_name", '')

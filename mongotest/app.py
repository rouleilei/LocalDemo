import re

from fastapi import FastAPI, Request
from starlette.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from starlette.templating import Jinja2Templates
import router
from config import Conf, CONNECTORS, POOLS

app = FastAPI()

app.include_router(router.router)

app.mount('/static', StaticFiles(directory="static"), name='static')
templates = Jinja2Templates(directory="static")

DB_POOL = None

COOKIE_KEY = 'fastapiusersauth'
COOKIE_PATTERN = re.compile(f"{COOKIE_KEY}=(.*?);")


@app.on_event("startup")
async def startup_event():
    _db = 'MONGODB'
    config = Conf.get_config_by_prefix(_db)
    kwargs = {}
    for key, value in config.items():
        kwargs[key] = value

    POOLS[_db] = CONNECTORS[_db](**kwargs)


@app.on_event("shutdown")
async def shutdown_event():
    _db = 'MONGODB'
    POOLS[_db].close()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    url = str(request.url)
    response = await call_next(request)
    if "login" in url and response.status_code == 200:
        resp_set_cookie = response.headers.get("set-cookie")
        if resp_set_cookie:
            result = COOKIE_PATTERN.findall(resp_set_cookie)

    return response


@app.get("/")
def home():
    return RedirectResponse(url="/sign_in")


@app.get('/sign_in')
async def sign_in(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

from datetime import datetime, timedelta
from typing import Optional
import random

import jwt

JWT_ALGORITHM = "HS256"
lifetime_seconds = 86400
secret = "storageadmin-user"
token_audience = "fastapi-users:auth"


def generate_captcha_code():
    captcha_code = ''
    while len(captcha_code) < 4:
        random_num = random.randint(0, 3)
        if random_num <= 1:
            random_str = str(random.randint(0, 9))
        elif random_num == 2:
            random_str = chr(random.randint(65, 90))
        else:
            random_str = chr(random.randint(97, 122))
        if random_str not in ['1', 'o', 'O', '0', 'L', 'l', 'i', 'I']:
            captcha_code += random_str
    return captcha_code


def generate_jwt(
        data: dict,
        secret: str,
        lifetime_seconds: Optional[int] = None,
        algorithm: str = JWT_ALGORITHM,
) -> str:
    payload = data.copy()
    if lifetime_seconds:
        expire = datetime.utcnow() + timedelta(seconds=lifetime_seconds)
        payload["exp"] = expire
    return jwt.encode(payload, secret, algorithm=algorithm)


def generate_token(user_id: str) -> str:
    data = {"user_id": user_id, "aud": token_audience}
    return generate_jwt(data, secret, lifetime_seconds, JWT_ALGORITHM)

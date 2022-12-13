from config import POOLS
from model import UserModel
import uuid

db = POOLS["MONGODB"]


class UserRepo:
    @staticmethod
    async def insert(user: UserModel):
        id = str(uuid.uuid4())
        _book = {
            "_id": id,
            "username": user.username,
            "password": user.password,
        }
        await db.get_collection("user").insert_one(_book)

from fastapi import APIRouter, Body, Depends
from src.models.user import UserSchema, UserLoginSchema
from src.auth.auth_bearer import JWTBearer
from src.auth.auth_handler import signJWT

users = []

router = APIRouter()

@router.post("/signup", tags=["User"])
async def create_user(user: UserSchema = Body(...)):
    users.append(user) # replace with db call, making sure to hash the password first
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


@router.post("/login", tags=["User"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }
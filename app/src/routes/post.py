from fastapi import APIRouter
from src.models.post import PostSchema
from fastapi import Depends
from src.auth.auth_bearer import JWTBearer

posts = [
    {
        "id": 1,
        "title": "Pancake",
        "content": "Lorem Ipsum ..."
    }
]

router = APIRouter()


@router.get("/", tags=["Post"])
async def get_posts() -> dict:
    return { "data": posts }

@router.get("/{id}", tags=["Post"])
async def get_single_post(id: int) -> dict:
    if id > len(posts):
        return {
            "error": "No such post with the supplied ID."
        }

    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }

@router.post("/", dependencies=[Depends(JWTBearer())], tags=["Post"])
async def add_post(post: PostSchema) -> dict:
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "data": "post added."
    }

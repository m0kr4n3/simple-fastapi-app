from fastapi import FastAPI
from app.routes.post import router as PostRouter
from app.routes.user import router as UserRouter
from app.routes.student import router as StudentRouter

app = FastAPI()

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your blog!."}

app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(PostRouter, tags=["Post"], prefix="/posts")
app.include_router(StudentRouter, tags=["Student"], prefix="/students")
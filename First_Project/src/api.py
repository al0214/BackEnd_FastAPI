from fastapi import FastAPI
from todos.todo import todo_router
import uvicorn

router = FastAPI(root_path="/proxy/8000/")

@router.get("/hello")
async def say_hello() -> dict:
    return {
        "message": "Hello!"
    }

router.include_router(todo_router)

if __name__ == "__main__":
    uvicorn.run("api:router", reload=True)
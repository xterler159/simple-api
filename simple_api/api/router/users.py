from fastapi.routing import APIRouter


def users_router():
    router = APIRouter()

    @router.get("/")
    async def root_users():
        return {"users:": []}

    return router

import uvicorn

from fastapi import FastAPI

from .router import users


class Application:
    def __init__(self, port):
        self.port = port

    def start(self):
        app = FastAPI(title="simple app")
        app.include_router(users.users_router())

        uvicorn.run(port=self.port, app=app)


def create_app():
    return None

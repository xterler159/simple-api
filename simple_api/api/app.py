from fastapi import FastAPI

from simple_api.api.router import users


class Application:
    def __init__(self, port):
        self.port = port

    @staticmethod
    def start():
        app = FastAPI(title="simple app")
        app.include_router(users.users_router())
        return app


def create_app():
    app = FastAPI(title="simple app")
    app.include_router(users.users_router())

    return Application.start()

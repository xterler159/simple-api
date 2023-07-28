import uvicorn
from fastapi import FastAPI

from .router import users


class Application:
    def __init__(self, port):
        self.port = port

    def start(self):
        # print("=======================START=======================")
        # print(self.port)
        # print("=======================START=======================")

        fast_api_app = FastAPI(
            title="simple app",
        )

        fast_api_app.include_router(router=users.users_router(), prefix="/users")

        # @fast_api_app.get("/")
        # def root():
        #     return {"Hello": "World"}

        uvicorn.run(port=self.port, app=fast_api_app)

import fastapi
import uvicorn
from fastapi import FastAPI

from src.database.database import engine
from src.database.models import *
from src.server.routers.user import router

app = FastAPI()


@app.get("/", tags=['Docs'])
def docs():
    return fastapi.responses.RedirectResponse(url="/docs")


app.include_router(router)

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8099)

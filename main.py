from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from models.base import Base
import models
from db.database import engine


async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

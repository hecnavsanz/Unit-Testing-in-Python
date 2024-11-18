from contextlib import asynccontextmanager
from typing import Annotated

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
from typing import Annotated
from fastapi import FastAPI, Depends
from sqlmodel import Session, create_engine, select
from geoalchemy2.shape import to_shape
from models.nyc import Street

engine = create_engine('postgresql://labs:Pytest-TDD.Labs_4ALL@localhost:18080/gis_db', echo=True)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "FastAPI Application with SQLAlchemy and PostGIS"}


@app.get("/streets/")
async def read_streets(session: SessionDep) -> list[Street]:
    results = session.exec(select(Street)).all()
    return results

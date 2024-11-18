from typing import Optional, Any
from sqlmodel import SQLModel, Field, Column
from geoalchemy2 import Geometry


class Street(SQLModel, table=True):
    __tablename__ = 'nyc_streets'
    gid: Optional[int] = Field(primary_key=True)
    id: int = Field(unique=True)
    name: str = Field()
    oneway: str = Field()
    type: str = Field()
    geom: Any = Field(sa_column=Column(Geometry('MULTILINESTRING', srid=26918)))


# class SubwayStations(Base):
#     __tablename__ = 'nyc_subway_stations'
#     gid = Column(Integer, primary_key=True)
#     objectid = Column(Integer, unique=True)
#     id = Column(Integer, unique=True)
#     name = Column(String)
#     geom = Column(Geometry('POINT', srid=26918))


#
# python: session
#
# from sqlalchemy import create_engine
# engine = create_engine('postgresql://labs:Pytest-TDD.Labs_4ALL@localhost:18080/gis_db', echo=True)
# from sqlalchemy.orm import sessionmaker
# Session = sessionmaker(bind=engine)
# session = Session()

# from models.nyc import Street
# Street.__table__
# street = Street(name="tutu", oneway=None, type="residential", geom="MULTILINESTRING ((586728.695515043 4497971.05313857, 586886.3582256545 4498000.5364795))")
# session.add(street)
# session.commit()

# tutu_street = session.query(Street).filter_by(name='tutu').first()
# tutu_street.type
# tutu_street.geom

# query = session.query(Street).order_by(Street.name)
# for street in query:
#   print(street.name, street.type)

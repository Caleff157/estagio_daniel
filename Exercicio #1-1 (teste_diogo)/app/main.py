import sqlalchemy as db
from os import environ
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from time import sleep
from loguru import logger

connection_str = f'mysql+pymysql://{environ["USER"]}:{environ["PASSWORD"]}@{environ["HOST"]}:{environ["PORT"]}/{environ["DATABASE"]}'

engine = db.create_engine(connection_str)

Base = declarative_base()

class City(Base):

    __tablename__ = 'city'

    id_table = db.Column(db.Integer, primary_key=True)
    name_person = db.Column('name', db.String(225))
    city_name = db.Column('city_name', db.String(225))

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

index = 0
while index < 1000:

    city = City()
    city.name_person = f'Pessoa {index}'
    city.city_name = f'Cidade {index}'

    index += 1

    session.add(city)
    session.commit()

    logger.success(f'Dados do indice {index} adicionados com sucesso')
    sleep(3)
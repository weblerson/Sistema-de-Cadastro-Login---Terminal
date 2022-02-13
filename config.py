from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER = "root"
PASSWORD = ""
HOST = "localhost"
DB = "teste"
PORT = "3307"

CONNECTION = f"mariadb+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

engine = create_engine(CONNECTION, echo = False)

Session = sessionmaker(bind = engine)
session = Session()

Base = declarative_base()
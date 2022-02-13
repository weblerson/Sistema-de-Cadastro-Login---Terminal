from config import *

class Person(Base):
    __tablename__ = "pessoas"
    id = Column(Integer, primary_key = True, autoincrement = True)
    nome = Column(String(60))
    email = Column(String(100), nullable = False)
    senha = Column(String(200), nullable = False)

Base.metadata.create_all(engine)
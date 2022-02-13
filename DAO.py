from config import *
from model import *
import bcrypt

class PersonDAO:
    @classmethod
    def read(cls):
        people_list = session.query(Person).all()

        return people_list

    @classmethod
    def register(cls, person: Person, ta):
        encoded_password = person.password.encode('utf-8')
        hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
        hashed_password = hashed_password.decode('utf-8')

        session.add(Person(nome = person.name, email = person.email, senha = hashed_password))
        session.commit()

    @classmethod
    def create_table(cls, table: PersonTable):
        class PersonTable(Base):
            __tablename__ = table.table_name
            id = Column(Integer, primary_key = True, autoincrement = True)
            nome = Column(String(table.len_name), nullable = False)
            email = Column(String(table.len_email), nullable = False)
            senha = Column(String(table.len_password), nullable = False)

        Base.metadata.create_all(engine)


PersonDAO.register(Person("Erin", "erin@gmail.com", "Komaeda13"))
    
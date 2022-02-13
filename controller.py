from config import *
from model import Person
import bcrypt

class PersonController:
    @classmethod
    def read(cls):
        email_list = [person.email for person in session.query(Person).all()]

        return email_list

    @classmethod
    def register(cls, name, email, password):
        email_list = PersonController.read()
        provider_list = ["@gmail.com", "@hotmail.com", "@yahoo.com", "@mail.com"]
        character_list = [character for character in "@#$%&()_-+[}]{.,<>;:\/?|"]

        if name.strip() == '' or email.strip() == '' or password.strip() == '':
            return "Você não pode deixar de preencher nenhum campo!"
        
        for provider in provider_list:
            if provider in email:
                break

            if provider == provider_list[len(provider_list) - 1]:
                return "Endereço de email digitado inválido."

        if email in email_list:
            return "O endereço de email digitado já existe. Tente outro."

        if len(password) < 8:
            return "A senha digitada é muito curta. Digite uma senha acima de 8 caracteres!"

        for character in character_list:
            if character in password:
                break

            if character == character_list[len(character_list) - 1]:
                return "Sua senha não possui nenhum caractere especial. Tente novamente."

        encoded_password = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
        hashed_password = hashed_password.decode('utf-8')

        try:
            session.add(Person(nome = name, email = email, senha = hashed_password))
            session.commit()

            return True

        except:
            return False

    @classmethod
    def login(cls, email, password):
        try:
            email_list = PersonController.read()
        
        except:
            return False, None

        if email not in email_list:
            return "Email e/ou senha incorreto(s). Tente novamente ou cadastre-se.", None

        try:
            person = session.query(Person).filter_by(email = email).one()

        except:
            return False, None

        encoded_password = password.encode('utf-8')

        if bcrypt.hashpw(encoded_password, person.senha.encode('utf-8')).decode('utf-8') == person.senha:
            return True, person.nome

        else:
            return "Email e/ou senha incorretor(s). Tente novamente ou cadastre-se", None
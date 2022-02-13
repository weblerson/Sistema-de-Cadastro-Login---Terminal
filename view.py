from controller import *
import os

class Interface:
    is_authenticated = False
    username = None

    @classmethod
    def run(cls):
        while True:
            options = ["0", "1", "2", "3", "4"]

            print("Terminal de ações do programa. Selecione a opção desejada:")

            print('''
            Digite 0 para encerrar o programa.
            Digite 1 para ir para o menu principal.
            Digite 2 para se cadastrar no sistema.
            Digite 3 para fazer login no sistema.
            Digite 4 para fazer logout no sistema.''')
            Interface.breakline()
            
            choice = input("Escolha: ")

            if choice not in options:
                while True:
                    Interface.clear()
                    print("Digite uma opção válida!")
                    
                    input("Digite qualquer tecla para continuar: ")

                    Interface.clear()

                    break

            if choice == '0':
                Interface.clear()

                break

            if choice == '1' and Interface.is_authenticated:
                Interface.homepage()

            elif choice == '1' and not Interface.is_authenticated:
                while True:
                    Interface.clear()
                    print("Você precisa fazer login para entrar!")

                    input("Digite qualquer tecla para sair: ")

                    Interface.clear()

                    break

            if choice == '2':
                Interface.register()
            
            if choice == '3':
                Interface.login()

            if choice == '4' and Interface.is_authenticated:
                Interface.logout()

            elif choice == '4' and not Interface.is_authenticated:
                Interface.clear()

                print("Você precisa estar autenticado no sistema para fazer logout!")
                Interface.breakline()

    @classmethod
    def homepage(cls):
        while True:
            Interface.clear()
            print(f"Olá, {Interface.username}! Esta é a página principal.")

            input("Digite qualquer tecla para sair: ")

            Interface.clear()

            break

    @classmethod
    def register(cls):
        while True:
            Interface.clear()

            print("Digite 0 a qualquer momento para sair!")
            Interface.breakline()

            name = input("Digite seu nome: ")
            if name == '0':
                Interface.clear()
                break

            Interface.breakline()
            print("Provedores de email válidos: @gmail.com, @hotmail.com, @yahoo.com, @mail.com")
            email = input("Digite seu email: ")
            if email == '0':
                Interface.clear()
                break

            password = input("Digite sua senha: ")
            if password == '0':
                Interface.clear()
                break

            success = "Você foi cadastrado com sucesso no sistema!"
            error = "Ocorreu algum erro de comunicação com o sistema. Não foi possível fazer o cadastro."
            again = Interface.test(PersonController.register(name, email, password), success, error)

            if again:
                continue

            else:
                pass

            Interface.clear()

            break

    @classmethod
    def login(cls):
        while True:
            Interface.clear()

            print("Digite 0 a qualquer momento para sair!")
            Interface.breakline()

            email = input("Digite seu email: ")
            if email == '0':
                Interface.clear()
                break
            
            password = input("Digite sua senha: ")
            if password == '0':
                Interface.clear()
                break

            success = "Você foi autenticado com sucesso no sistema!"
            error = "Ocorreu algum erro de comunicação com o sistema. Não foi possível fazer a autenticação."

            result, name = PersonController.login(email, password)

            if result == True:
                Interface.clear()

                Interface.is_authenticated = True
                Interface.username = name

                print(success)
                Interface.breakline()

                input("Digite qualquer tecla para continuar: ")
                Interface.clear()

                break

            elif result == False:
                Interface.clear()

                print(error)
                Interface.breakline()

                input("Digite qualquer tecla para continuar: ")
                Interface.clear()

                break

            else:
                Interface.clear()
                print(result)

                Interface.breakline()

                print("Para tentar novamente, digite S. Senão, digite qualquer tecla para sair.")
                choice = input("Escolha: ").upper()
                
                if choice == 'S':
                    continue

                else:
                    pass

    @classmethod
    def logout(cls):
        Interface.clear()

        Interface.is_authenticated = False
        Interface.username = None

        input("Você foi desconectado com sucesso do sistema. Digite qualquer tecla para continuar: ")

        Interface.clear()

    @classmethod
    def breakline(cls):
        print("")

    @classmethod
    def clear(cls):
        os.system("cls")

    @classmethod
    def test(cls, function, success, error):
        if function == True:
            Interface.clear()
            print(success)

            Interface.breakline()

            input("Digite qualquer tecla para continuar: ")
        
        elif function == False:
            Interface.clear()
            print(error)

            Interface.breakline()

            input("Digite qualquer tecla para continuar: ")

        else:
            Interface.clear()
            print(function)

            Interface.breakline()

            print("Para tentar novamente, digite S. Senão, digite qualquer tecla para sair.")
            choice = input("Escolha: ").upper()
            
            if choice == 'S':
                return True

if __name__ == "__main__":
    Interface.run()
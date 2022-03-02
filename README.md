# Sistema de Cadastro/Login - Terminal
Sistema de cadastro e login de usuários por meio de terminal.

A aplicação utiliza o banco de dados MariaDB.

Para utilizar, basta mudar as configurações como host, porta etc no arquivo config.py e instalar as bibliotecas utilizadas executando o comando "pip install -r requirements.txt" no terminal no diretório raiz do projeto.

# Criando o servidor localhost FastAPI:
Para criar, execute o comando "uvicorn API:app --reload" na raiz do projeto.

Para consumir a API com o id, nome e email dos usuários cadastrados, fazer uma requisição do tipo GET para o seu localhost: http://127.0.0.1:8000

# Exemplo de requisição usando Python e a biblioteca Requests:
request = requests.get("http://127.0.0.1:8000")
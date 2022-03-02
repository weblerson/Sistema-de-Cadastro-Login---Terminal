from controller import PersonController
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return PersonController.read_users()
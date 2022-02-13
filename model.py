class Person:
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password

class PersonTable:
    def __init__(self, table_name: str, len_name: int, len_email: int, len_password: int):
        self.table_name = table_name
        self.len_name = len_name
        self.len_email = len_email
        self.len_password = len_password
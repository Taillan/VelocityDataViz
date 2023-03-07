
from typing import List

class Participation():
    def __init__(self, username: str, password: str, email: str, id: int=None):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
    
    def toJSON(self):
        return {"username": self.playerName, "password": self.password, "email":self.email}
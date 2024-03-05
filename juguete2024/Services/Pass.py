import bcrypt
from decouple import config


class PassService:
    
    salt = bcrypt.gensalt()

    @classmethod
    def encrypt_pass(cls, password:bytes):
        try:
            encPass = bcrypt.hashpw(password, cls.salt)
            return encPass
        except ValueError as e:
            raise e


    @classmethod
    def check_pass(cls, password:bytes, encPass:bytes):
        try:
            if bcrypt.checkpw(password, encPass):
                return True
        except ValueError as e:
            raise e
            


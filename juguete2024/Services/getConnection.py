from decouple import config
import psycopg2


DBNAME=config('DBNAME')
USER=config('USER')
PASSWORD=config('PASSWORD')
HOST=config('HOST')

class Connection:

    def __init__(self, dbname, user, password, host):
        self.dbname = DBNAME
        self.user = USER
        self.password = PASSWORD
        self.host = HOST


    @classmethod
    def getConnection(cls):

        try:
            cnx = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
            if cnx:
                print('Connected')
                print(cnx)
                return True
            return cnx
        except psycopg2.Error as e:
            raise e



if __name__ == '__main__':
    c = Connection
    c.getConnection()

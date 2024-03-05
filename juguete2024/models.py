from flask_sqlalchemy import SQLAlchemy
from psycopg2 import connect
import psycopg2
import psycopg2


db = SQLAlchemy()

class User(db.Model):
    class Meta:
        __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<User: %r>' % self.username

    @classmethod
    def create_user(cls, username, password):
        with connect("dbname=juguete user=postgres password=Z4dk13l2017**") as cnx:
            cur = cnx.cursor()
            cur.execute("INSERT INTO users(username, password)VALUES(%s,%s)",(username, password))
            cnx.commit()


    @classmethod
    def list(cls):
        with connect("dbname=juguete user=postgres password=Z4dk13l2017**") as cnx:
            cur = cnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cur.execute("SELECT * FROM users")
            result = cur.fetchall()
            print(result)
            return result
            cnx.commit()



class Trabajador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app = db.Column(db.String(), nullable=False)
    apm = db.Column(db.String(), nullable=False)
    nombres = db.Column(db.String(), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    sexo = db.Column(db.String(), nullable=False)
    matricula = db.Column(db.String(), nullable=False)
    adscripcion = db.Column(db.String(), nullable=False)
    horario = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Matricula: %r' % self.matricula


    @classmethod
    def create_worker(cls, app, apm, nombres, edad, sexo, matricula, adscripcion, horario, user_id):
        pass



class Hijo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(), nullable=False)
    sexo = db.Column(db.String(), nullable=False)
    f_nac = db.Column(db.String(), nullable=False)
    edad = db.Column(db.String(), nullable=False)
    edad_a = db.Column(db.String(), nullable=False)
    trabajador_id = db.Column(db.Integer, db.ForeignKey('trabajador.id'), nullable=False)

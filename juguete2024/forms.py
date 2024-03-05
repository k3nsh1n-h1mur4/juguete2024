from wtforms import Form, StringField, PasswordField, validators, SelectField
from wtforms.validators import Length, InputRequired, DataRequired

class UserForm(Form):
    username = StringField('Usuario: ', [validators.Length(min=4, max=14)])
    password = PasswordField('Password: ', [validators.Length(min=8, max=14)])



class TrabajadorForm(Form):
    SEXO = [
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
    ]
    
    HORARIO = [
        ('MATUTINO','MATUTINO'),
        ('VESPERTINO','VESPERTINO'),
        ('NOCTURNO','NOCTURNO'),
        ('JORNADA ACUMULADA','JORNADA ACUMULADA')
    ]
    
    app = StringField('Apellido Paterno: ', [validators.InputRequired(message='Dato Requerido')])
    apm = StringField('Apellido Materno: ', [validators.InputRequired(message='Dato Requerido')])
    nombres = StringField('Nombre(s): ', [validators.DataRequired(message='Dato Requerido')])
    edad = StringField('Edad: ', [validators.DataRequired(message='Dato Requerido')])
    sexo = SelectField('Sexo: ', choices=SEXO)
    matricula = StringField('Matricula: ', [validators.DataRequired(message='Dato Requerido')])
    adscripcion = StringField('Adscripcion: ', [validators.DataRequired(message='Dato Requerido')])
    horario = SelectField('Horario: ', choices=HORARIO)

from . import app
from flask import request, render_template, url_for, redirect 

from .forms import UserForm

from .Services.Pass import PassService 

from juguete2024.models import db, User, Trabajador

@app.route('/')
def index():
    return 'Hello'


@app.route('/register_user', methods=['GET', 'POST'])
def register_user():
    title = 'Registro Usuario'
    error = None
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        #print(username, password)
        enc = PassService.encrypt_pass(str.encode(password))
        #print(enc)
        User.create_user(username, enc)
    return render_template('register.html', form=form)


@app.route('/listado')
def listado():
    title = 'Listado'
    if request.method == 'GET':
        r = User.list()
    return render_template('listado.html', r=r)










from flask import Blueprint, request, flash, url_for, redirect
from flask.templating import render_template

from juguete2024.forms import TrabajadorForm

worker = Blueprint('worker', __name__, url_prefix='/worker')

@worker.route('/')
def index_worker():
    return 'Blueprint Worker'

@worker.route('/register_worker', methods=['GET', 'POST'])
def register_worker():
    title = 'Registro Trabajador'
    form = TrabajadorForm(request.form)
    if request.method == 'POST' and form.validate():
        pass
    return render_template('worker/add_worker.html', form=form)


@worker.route('/list_worker')
def list_worker():
    title = 'Listado Trabajadores'
    if request.method == 'GET':
        pass    
    
    return render_template('worker/list.html')


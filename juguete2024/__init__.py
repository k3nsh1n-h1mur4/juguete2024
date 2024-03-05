"An amazing jugueteApp"
__version__ = "0.1"

import os
from flask import Flask, g, Blueprint
from flask_sqlalchemy import SQLAlchemy

from juguete2024.models import db

from juguete2024.worker import worker


app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = os.urandom(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Z4dk13l2017**@localhost:5432/juguete'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
    app.register_blueprint(worker)

    import juguete2024.views
    
    db.init_app(app)
    db.create_all()

    print(db)

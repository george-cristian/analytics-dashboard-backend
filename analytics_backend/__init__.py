import os
from flask import Flask
from .extensions import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

from analytics_backend import views
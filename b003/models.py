from flask import Flask
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLALchemy(app)
apimanager = APIManager(app, flask_sqlalchemy_db=db)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)


db.create_all()

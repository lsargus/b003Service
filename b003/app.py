from flask import Flask, render_template, request
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# configração para banco de dados
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///b003SQL.db'
# db = SQLAlchemy(app)


# model da tabela
# class Person(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    first_name = db.Column(db.Text)
#    last_name = db.Column(db.Text)


## comando para criar as tabelas no banco
# db.create_all()

# api_manager = APIManager(app, flask_sqlalchemy_db=db)
# api_manager.create_api(Person, methods=['GET', 'POST', 'DELETE', 'PUT'])

global nivel
nivel = 0

@app.route('/')
def localiza_pulso():
    return "<p>Hello, World!</p>"


@app.route('/testeGet', methods=['GET'])
def teste_get():
    valvula1 = request.args.get('v1')
    valvula2 = request.args.get('v2')

    global nivel

    if valvula1 == "true":
         nivel += 1
    if valvula2 == "true":
        nivel -= 1
    if nivel < 0:
        nivel = 0

    return "<p>Peguei " + valvula1 + " Peguei " + valvula2 + " " + str(nivel)+ "</p>"


if __name__ == "__main__":
    app.run()

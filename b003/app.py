from flask import Flask, render_template, request, json
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# configração para banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///b003SQL.db'
db = SQLAlchemy(app)


# model da tabela
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)


## comando para criar as tabelas no banco
db.create_all()

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Person, methods=['GET', 'POST', 'DELETE', 'PUT'])


@app.route('/')
def localiza_pulso():
    return "<p>Hello, World!</p>"


@app.route('/testePost', methods=['POST'])
def teste_post():
    request_data = request.get_json()
    x = request_data['x']
    y = request_data['y']
    codBody = request_data['codBody']
    print(x)
    print(y)
    print(codBody)

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


if __name__ == "__main__":
    app.run()

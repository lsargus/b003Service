from flask import Flask, request
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy

from b003.pyModbus.synchronousCliente.synchronousClientConnection import synchronous_client_connection

from flask import request, json

app = Flask(__name__)
app.config.from_object('config.Config')
CORS(app)

nivel = 0


# import declared routes
from tensorflow import tensorflow

@app.route('/testeGet', methods=['GET'])
def teste_get():
    valvula1 = request.args.get('v1')
    valvula2 = request.args.get('v2')
    nivel_byte = [False, False, False, False, False, False, False, False];
    global nivel

    if valvula1 == "true":
        nivel += 1
      #  connection.write_coil(True, 1)
   # else:
       # connection.write_coil(False, 1)

    if valvula2 == "true":
        nivel -= 1
    #    connection.write_coil(True, 2)
    #else:
     #   connection.write_coil(False, 2)

    if nivel < 0:
        nivel = 0

    #connection.write_register(nivel, 1)


    return "<p>Peguei " + valvula1 + " Peguei " + valvula2 + " " + str(nivel) + "</p>"

@app.route('/testeGet2', methods=['GET'])
def teste_get2():
    return "v1=1, v2=0"
if __name__ == "__main__":
    app.run(host="localhost", port=5000)

from flask import Flask, request
from flask_cors import CORS
from flask_restless import APIManager


app = Flask(__name__)
app.config.from_object('config.Config')
CORS(app)

# import declared routes
from tensorflow import rotasTensorflow
from simulador import rotasSimulador

if __name__ == "__main__":
    app.run(host="localhost", port=5000)

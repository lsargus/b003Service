from flask import Flask
from flask_cors import CORS

from flask import request, json

app = Flask(__name__)
app.config.from_object('config.Config')
CORS(app)

# import declared routes
from tensorflow import tensorflow

if __name__ == "__main__":
    app.run(host="localhost", port=5000)

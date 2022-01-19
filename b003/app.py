from flask import Flask, request
from flask_cors import CORS
from flask_restless import APIManager

from b003.pyModbus.synchronousCliente.synchronousClientConnection import SynchronousClientConnection

app = Flask(__name__)
app.config.from_object('config.Config')
CORS(app)

# import declared routes
from tensorflow import rotasTensorflow
from simulador import rotasSimulador

if __name__ == "__main__":
    connection = SynchronousClientConnection()
    # connection.connect()

    UNIT = 0x1

    # while True:
    #     co = connection.client.read_coils(0, 8, unit=UNIT)
    #     di = connection.client.read_discrete_inputs(0, 8, unit=UNIT)
    #     hr = connection.client.read_holding_registers(0, count=10, unit=UNIT)
    #     ir = connection.client.read_input_registers(0, count=10, unit=UNIT)
    #
    #     connection.client.write_coil(1, True)
    #     connection.client.write_register(3, 19)

    # print(co)
    app.run(host="localhost", port=5000)

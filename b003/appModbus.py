from flask import Flask
from flask_cors import CORS

from b003.dao.requestModbusDao import RequestModbusDao
from b003.database import Database
from b003.enums.tpRegister import TpRegister
from b003.models.requestModbusServer import RequestModbusServer
from b003.pyModbus.asynchronousServer.asynchronousServer import AsynchronousServer
from b003.pyModbus.synchronousServer.synchronousServer import SynchronousServer

app = Flask(__name__)
app.config.from_object('config.Config')
CORS(app)

if __name__ == "__main__":
    server = SynchronousServer()
    server.start()


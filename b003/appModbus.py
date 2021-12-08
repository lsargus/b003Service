from flask import Flask
from flask_cors import CORS

from b003.dao.requestModbusDao import RequestModbusDao
from b003.database2 import Database2
from b003.pyModbus.asynchronousServer.asynchronousServer import AsynchronousServer

app = Flask(__name__)
app.config.from_object('config.Config')
CORS(app)

if __name__ == "__main__":
    #server = AsynchronousServer()
    #server.start()

    while True:
        dao = RequestModbusDao()

        # busca requisições pendentes no banco]
        result = dao.find_pending()



    print(r)


from flask import request, json
from b003.dao.requestModbusDao import RequestModbusDao
from b003.enums.tpRegister import TpRegister
from b003.models.requestModbusServer import RequestModbusServer
import datetime

from __main__ import app


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


@app.route('/testeBotao', methods=['POST'])
def teste_botao():
    request_data = request.get_json()
    bot = request_data['bot']

    dao = RequestModbusDao()

    req = RequestModbusServer()

    req.ip_clp = '10.0.0.10'
    req.tp_register = TpRegister.INPUT_REGISTERS
    req.ds_request = bot
    req.executed = False
    req.dt_create = datetime.datetime.now()

    dao.persistRequest(req)

    return json.dumps({'success': True, 'msg': bot}), 200, {'ContentType': 'application/json'}
    # server.context[0x00].getValues(1, 0x00, count=10)

    # rr = connection.read_discrete_inputs(0, 1)
    #
    # if rr.bits[0]:
    #     msg = 'Botão ligado'
    # else:
    #     msg = 'Botão desligado'
    #
    # return json.dumps({'success': True, 'msg': msg}), 200, {'ContentType': 'application/json'}


@app.route('/teste_lampada', methods=['POST'])
def teste_lampada():
    request_data = request.get_json()
    lamp = request_data['lamp']

    print(lamp)
    # server.context[0x00].setValues(2, 0x00, 1)
    # connection.write_coil(lamp, 0)
    #
    # return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/teste_analog', methods=['POST'])
def teste_analog():
    pass
    # server.context[0x00].getValues(3, 0x00, count=10)
    # rr = connection.read_imput_register(0, 1)
    #
    # msg = 'Valor: ' + str(rr.registers[0])
    #
    # return json.dumps({'success': True, 'msg': msg}), 200, {'ContentType': 'application/json'}


@app.route('/teste_medidor', methods=['POST'])
def teste_medidor():
    request_data = request.get_json()
    valor = request_data['valor']

    # server.context[0x00].setValues(4, 0x00, valor)
    print(valor)

    # connection.write_register(valor, 0)
    #
    # return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

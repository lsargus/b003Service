from __main__ import app

from flask import request

from b003.converterValueRequestModbus import convert_modbus_requesto_bool_to_array_string, \
    convert_modbus_requesto_string_to_array_bool
from b003.dao.requestModbusDao import RequestModbusDao
from b003.enums.tpRegister import TpRegister
from b003.models.requestModbusServer import RequestModbusServer
import datetime


@app.route('/testeGet', methods=['GET'])
def teste_get():
    valvula1 = request.args.get('v1')
    valvula2 = request.args.get('v2')

    dao = RequestModbusDao()

    req = RequestModbusServer()

    req.ip_clp = '10.0.0.10'
    req.tp_register = TpRegister.INPUT_REGISTERS
    req.ds_request = convert_modbus_requesto_bool_to_array_string(valvula1.casefold() == "true", valvula2.casefold() == "true")
    convert_modbus_requesto_string_to_array_bool(req.ds_request)
    req.executed = False
    req.dt_create = datetime.datetime.now()

    dao.persistRequest(req)

    return "<p>Peguei " + valvula1 + " Peguei " + valvula2 + "</p>"

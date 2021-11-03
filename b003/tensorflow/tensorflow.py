from flask import request, json

from __main__ import app

from b003.pyModbus.synchronousCliente.synchronousClientConnection import synchronous_client_connection

connection = synchronous_client_connection('192.168.100.39', 502)
connection.connect()


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

    print(bot)

    rr = connection.read_discrete_inputs(0, 1)

    if rr.bits[0]:
        msg = 'Botão ligado'
    else:
        msg = 'Botão desligado'

    return json.dumps({'success': True, 'msg': msg}), 200, {'ContentType': 'application/json'}


@app.route('/teste_lampada', methods=['POST'])
def teste_lampada():
    request_data = request.get_json()
    lamp = request_data['lamp']

    print(lamp)

    connection.write_coil(lamp, 0)

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/teste_analog', methods=['POST'])
def teste_analog():
    rr = connection.read_imput_register(0, 1)

    msg = 'Valor: ' + str(rr.registers[0])

    return json.dumps({'success': True, 'msg': msg}), 200, {'ContentType': 'application/json'}


@app.route('/teste_medidor', methods=['POST'])
def teste_medidor():
    request_data = request.get_json()
    valor = request_data['valor']

    print(valor)

    connection.write_register(valor, 0)

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

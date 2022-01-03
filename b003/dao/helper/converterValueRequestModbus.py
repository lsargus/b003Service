from numpy import array


def convert_modbus_requesto_bool_to_array_string(*args):
    msg = ''

    for i, valor in enumerate(args):
        # coloca virgula se não for o primeiro valor
        if i:
            msg = msg + ','

        msg = msg + '1' if valor else '0'

    return msg


def convert_modbus_requesto_string_to_array_bool(msg):
    v = msg.split(',')

    return array(v, dtype=bool)


def convert_modbus_requesto_int_to_array_string(*args):
    msg = ''

    for i, valor in enumerate(args):
        # coloca virgula se não for o primeiro valor
        if i:
            msg = msg + ','

        msg = msg + str(valor)

    return msg


def convert_modbus_requesto_string_to_array_int(msg):
    v = msg.split(',')

    return array(v, dtype=int)

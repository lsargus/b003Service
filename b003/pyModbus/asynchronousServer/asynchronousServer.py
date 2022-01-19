import logging

from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.server.asynchronous import StartTcpServer
from pymodbus.version import version
from twisted.internet.task import LoopingCall

from b003.dao.requestModbusDao import RequestModbusDao
from b003.enums.tpRegister import TpRegister
from b003.pyModbus.customModbusResponse import CustomModbusRequest

FORMAT = '%(asctime)-15s %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s'


class AsynchronousServer:
    def __init__(self, host='127.0.0.1', port=5020):
        logging.basicConfig(format=FORMAT)

        self.port = port
        self.host = host

        # ----------------------------------------------------------------------- #
        # initialize your data store
        # ----------------------------------------------------------------------- #
        di_block = ModbusSequentialDataBlock(0, [False] * 8)
        co_block = ModbusSequentialDataBlock(0, [False] * 8)
        hr_block = ModbusSequentialDataBlock(0, [10] * 10)
        ir_block = ModbusSequentialDataBlock(0, [10] * 10)
        store = ModbusSlaveContext(
            di=di_block,
            co=co_block,
            hr=hr_block,
            ir=ir_block,
            zero_mode=True)

        # store.register(1, 'co', co_block)
        # store.register(4, 'ir', ir_block)
        # store.register(2, 'di', di_block)
        # store.register(16, 'hr', hr_block)

        self.context = ModbusServerContext(slaves=store, single=True)

        self.log = logging.getLogger()
        self.log.setLevel(logging.DEBUG)

        # ----------------------------------------------------------------------- #
        # initialize the server information
        # ----------------------------------------------------------------------- #
        # If you don't set this or any fields, they are defaulted to empty strings.
        # ----------------------------------------------------------------------- #
        self.identity = ModbusDeviceIdentification()
        self.identity.VendorName = 'Pymodbus'
        self.identity.ProductCode = 'PM'
        self.identity.VendorUrl = 'http://github.com/riptideio/pymodbus/'
        self.identity.ProductName = 'Pymodbus Server'
        self.identity.ModelName = 'Pymodbus Server'
        self.identity.MajorMinorRevision = version.short()

        # ----------------------------------------------------------------------- #
        # run the server you want
        # ----------------------------------------------------------------------- #

    def start(self):
        time = 5  # 5 seconds delay
        loop = LoopingCall(f=updating_writer, a=(self.context, self.log))
        loop.start(time, now=False)  # initially delay by time

        # TCP Server
        StartTcpServer(self.context, identity=self.identity, address=(self.host, self.port),
                       custom_functions=[CustomModbusRequest])

    def read_coil(self, adress: int = 0, count: int = 1):
        """
        Realiza a leitura de um valor discreto
        :param adress: endereço do bite
        :param count: quantidade de bites a serem lidos
        :return:
        """
        return self.context.getValues(adress, count)


def updating_writer(a):
    """ A worker process that runs every so often and
    updates live values of the context. It should be noted
    that there is a race condition for the update.

    :param a: he input arguments to the call
    """
    log = a[1]
    log.debug("updating the context")
    context = a[0]

    slave_id = 0x00

    # dao = RequestModbusDao()

    # busca requisições pendentes no banco]
    # result = dao.find_pending()

    vd = context[slave_id].store['d']
    vc = context[slave_id].store['c']
    vi = context[slave_id].store['i']
    vh = context[slave_id].store['h']

    context[slave_id].store['c'].setValues(0, True)
    context[slave_id].store['c'].setValues(1, False)
    context[slave_id].store['c'].setValues(2, True)
    context[slave_id].store['c'].setValues(3, False)
    context[slave_id].store['c'].setValues(4, True)
    context[slave_id].store['c'].setValues(5, False)
    context[slave_id].store['c'].setValues(6, True)
    context[slave_id].store['c'].setValues(7, False)

    context[slave_id].store['d'].setValues(0, True)
    context[slave_id].store['d'].setValues(1, False)
    context[slave_id].store['d'].setValues(2, True)
    context[slave_id].store['d'].setValues(3, False)
    context[slave_id].store['d'].setValues(4, True)
    context[slave_id].store['d'].setValues(5, False)
    context[slave_id].store['d'].setValues(6, True)
    context[slave_id].store['d'].setValues(7, False)

    context[slave_id].store['h'].setValues(0, '11')
    context[slave_id].store['h'].setValues(1, '12')
    context[slave_id].store['h'].setValues(2, '13')
    context[slave_id].store['h'].setValues(3, '14')
    context[slave_id].store['h'].setValues(4, '15')
    context[slave_id].store['h'].setValues(5, '16')
    context[slave_id].store['h'].setValues(6, '17')
    context[slave_id].store['h'].setValues(7, '18')

    context[slave_id].store['i'].setValues(0, '11')
    context[slave_id].store['i'].setValues(1, '12')
    context[slave_id].store['i'].setValues(2, '13')
    context[slave_id].store['i'].setValues(3, '14')
    context[slave_id].store['i'].setValues(4, '15')
    context[slave_id].store['i'].setValues(5, '16')
    context[slave_id].store['i'].setValues(6, '17')
    context[slave_id].store['i'].setValues(7, '18')

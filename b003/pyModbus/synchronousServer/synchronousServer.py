import logging

from pymodbus.version import version
from pymodbus.server.sync import StartTcpServer

from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSparseDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

from twisted.internet.task import LoopingCall

from b003.pyModbus.customModbusResponse import CustomModbusRequest

FORMAT = '%(asctime)-15s %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s'


class SynchronousServer:
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


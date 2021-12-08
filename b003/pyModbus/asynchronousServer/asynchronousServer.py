import logging

from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.server.asynchronous import StartTcpServer
from pymodbus.version import version
from twisted.internet.task import LoopingCall

FORMAT = '%(asctime)-15s %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s'


class AsynchronousServer:
    def __init__(self, host='127.0.0.1', port=5020):
        logging.basicConfig(format=FORMAT)

        self.port = port
        self.host = host

        self.store = ModbusSlaveContext(
            di=ModbusSequentialDataBlock(0, [17] * 100),
            co=ModbusSequentialDataBlock(0, [17] * 100),
            hr=ModbusSequentialDataBlock(0, [17] * 100),
            ir=ModbusSequentialDataBlock(0, [17] * 100))
        self.context = ModbusServerContext(slaves=self.store, single=True)
        self.log = logging.getLogger()
        self.log.setLevel(logging.INFO)

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
        time = 1  # 1 seconds delay
        loop = LoopingCall(f=updating_writer, a=(self.context, self.log))
        loop.start(time, now=False)  # initially delay by time
        # TCP Server
        StartTcpServer(self.context, identity=self.identity, address=(self.host, self.port))



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
    # lê valores analógicos
    print(context[slave_id].getValues(1, 0x00, count=10))
    #print(context[slave_id].getValues(2, 0x00, count=10))
    #print(context[slave_id].getValues(3, 0x00, count=10))
    #print(context[slave_id].getValues(4, 0x00, count=10))

    # lê valores discretos
    #print(context[slave_id].getValues(1, 0x00, count=10))

    #context[slave_id].setValues(2, 0x00, '99')
    #context[slave_id].setValues(4, 0x00, '99')

import struct
# --------------------------------------------------------------------------- #
# import the various server implementations
# --------------------------------------------------------------------------- #
from pymodbus.pdu import ModbusRequest, ModbusResponse, ModbusExceptions
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.bit_read_message import ReadCoilsRequest
from pymodbus.compat import int2byte, byte2int
# --------------------------------------------------------------------------- #
# configure the client logging
# --------------------------------------------------------------------------- #
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)


# --------------------------------------------------------------------------- #
# create your custom message
# --------------------------------------------------------------------------- #
# The following is simply a read coil request that always reads 16 coils.
# Since the function code is already registered with the decoder factory,
# this will be decoded as a read coil response. If you implement a new
# method that is not currently implemented, you must register the request
# and response with a ClientDecoder factory.
# --------------------------------------------------------------------------- #


class CustomModbusResponse(ModbusResponse):
    function_code = 55
    _rtu_byte_count_pos = 2

    def __init__(self, values=None, **kwargs):
        ModbusResponse.__init__(self, **kwargs)
        self.values = values or []

    def encode(self):
        """ Encodes response pdu

        :returns: The encoded packet message
        """
        result = int2byte(len(self.values) * 2)
        for register in self.values:
            result += struct.pack('>H', register)
        return result

    def decode(self, data):
        """ Decodes response pdu

        :param data: The packet data to decode
        """
        byte_count = byte2int(data[0])
        self.values = []
        for i in range(1, byte_count + 1, 2):
            self.values.append(struct.unpack('>H', data[i:i + 2])[0])


class CustomModbusRequest(ModbusRequest):
    function_code = 15
    _rtu_frame_size = 4

    def __init__(self, address=None, **kwargs):
        ModbusRequest.__init__(self, **kwargs)
        self.address = address
        self.count = 8

    def encode(self):
        return struct.pack('>HH', self.address, self.count)

    def decode(self, data):
        self.address, self.count = struct.unpack('>HH', data)

    def execute(self, context):
        if not (1 <= self.count <= 0x7d0):
            return self.doException(ModbusExceptions.IllegalValue)
        if not context.validate(self.function_code, self.address, self.count):
            return self.doException(ModbusExceptions.IllegalAddress)
        values = context.getValues(self.function_code, self.address,
                                   self.count)
        return CustomModbusResponse(values)

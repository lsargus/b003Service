from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import logging

FORMAT = '%(asctime)-15s %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s'


class synchronous_client_connection:
    def __init__(self, host='192.168.100.39', port=502):
        logging.basicConfig(format=FORMAT)

        self.client = ModbusClient(host, port=port)
        self.log = logging.getLogger()
        self.log.setLevel(logging.INFO)

    def connect(self):
        self.log.info('Conecta ao server.')
        self.client.connect()

    def close_connect(self):
        self.log.info('Fecha a conexão ao server.')
        self.client.close()

    def read_coil(self, adress: int = 0, count: int = 1):
        """
        Realiza a leitura de um valor discreto
        :param adress: endereço do bite
        :param count: quantidade de bites a serem lidos
        :return:
        """
        self.log.debug("Lê valor discreto")
        rr = self.client.read_coils(adress, count)

        return rr

    def write_coil(self, valor, adress: int = 0):
        """
        Realiza a escrita de um valor discreto
        :param value: valor a ser escrito
        :param adress: endereço do bite
        :return:
        """
        self.log.debug("Escreve um valor discreto")
        rr = self.client.write_coil(adress, valor)

        return rr

    def read_discrete_inputs(self, adress: int = 0, count: int = 1):
        """
        Realiza a leitura de entradas discretas
        :param adress: endereço do bite
        :param count: quantidade de bites a serem lidos
        :return:
        """
        self.log.debug("Lê valor entrada discreta.")
        rr = self.client.read_discrete_inputs(adress, count)

        return rr

    def read_register(self, adress: int = 0, count: int = 1):
        self.log.debug("Lê valor analógico.")
        rr = self.client.read_holding_registers(adress, count)

        return rr

    def write_register(self, valor, adress: int = 0):
        self.log.debug("Escreve valor analógico.")
        rr = self.client.write_register(adress, valor)

        return rr

    def read_imput_register(self, adress: int = 0, count: int = 1):
        self.log.debug("Lê valor analógico de entrada.")
        rr = self.client.read_input_registers(adress, count)

        return rr

from b003.database import Database
from b003.database import Database
from b003.models.requestModbusServer import RequestModbusServer
from sqlalchemy.sql import select

SQL_ATUALIZA_REQUEST = 'UPDATE Request_modbus SET tp_register=%s, ip_clp=%s, cd_response=%s, executed=%s, ' \
                       'dt_create=%s, dt_executed = %s  where id = %s '
SQL_CRIA_REQUEST = 'INSERT into Request_modbus (tp_register, ip_clp, ds_request, cd_response, executed, dt_create, ' \
                   'dt_executed) values (?, ?, ?, ?, ?, ?, ?) '


class RequestModbusDao:
    def __init__(self):
        self.__db = Database('b003SQL.db')

    def persistRequest(self, request: RequestModbusServer):
        session = self.__db.session
        #cur = self.__db.cursor
        if request.id:
            session.merge(request)
            # cur.execute(SQL_ATUALIZA_REQUEST, (
            #     request.tp_register, request.ip_clp, request.cd_response, request.executed, request.dt_create,
            #     request.dt_executed, request.id))
        else:
            session.add(request)
        #     RequestModbusServer.ins
        #     cur.execute(SQL_CRIA_REQUEST, (
        #         request.tp_register, request.ip_clp, request.ds_request, request.cd_response, request.executed,
        #         request.dt_create, request.dt_executed))
        # self.__db.commit()

        session.commit()

    def find_pending(self):
        session = self.__db.session

        result = session.query(RequestModbusServer).filter(RequestModbusServer.executed == False).first()
        return result

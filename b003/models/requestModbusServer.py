from sqlalchemy import Column, DateTime, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref

from b003.models.base import Base
from b003.enums.intEnum import IntEnum
from b003.enums.tpRegister import TpRegister

from b003.models.responseModbus import ResponseModbusServer


class RequestModbusServer(Base):
    __tablename__ = 'Request_modbus'

    id = Column(Integer, primary_key=True)
    tp_register = Column(IntEnum(TpRegister))
    ip_clp = Column(String(20), nullable=False)
    ds_request = Column(String(255), nullable=False)
    cd_response = Column(Integer, ForeignKey('Response_modbus.id'))
    executed = Column(Boolean, nullable=True)
    dt_create = Column(DateTime, nullable=False)
    dt_executed = Column(DateTime, nullable=True)

    response = relationship("ResponseModbusServer", backref=backref("Response_modbus", uselist=False))

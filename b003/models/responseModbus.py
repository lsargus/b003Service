from sqlalchemy import Column, DateTime, String, Integer
from sqlalchemy.orm import relationship

from b003.models.base import Base
from b003.enums.intEnum import IntEnum
from b003.enums.tpResponseModbus import TpResponseModbus


class ResponseModbusServer(Base):
    __tablename__ = 'Response_modbus'

    id = Column(Integer, primary_key=True)
    tp_response = Column(IntEnum(TpResponseModbus))
    response = Column(String(255), nullable=False)
    dt_create = Column(DateTime, nullable=False)

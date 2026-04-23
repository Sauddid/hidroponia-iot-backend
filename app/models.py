from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class Reading(Base):
    __tablename__ = "readings"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer)
    temperatura = Column(Float)
    humedad_ambiente = Column(Float)
    humedad_sustrato = Column(Float)

class Command(Base):
    __tablename__ = "commands"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer)
    accion = Column(String)
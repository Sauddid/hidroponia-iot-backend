from pydantic import BaseModel

class DeviceCreate(BaseModel):
    name: str

class ReadingCreate(BaseModel):
    device_id: int
    temperatura: float
    humedad_ambiente: float
    humedad_sustrato: float

class CommandCreate(BaseModel):
    device_id: int
    accion: str
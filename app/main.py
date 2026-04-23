from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import engine, SessionLocal, Base

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

# -------- DEPENDENCIA DB --------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------- HOME --------
@app.get("/")
def home():
    return {"mensaje": "API HIDROPONIA con DB 🌱"}

# -------- DEVICES --------
@app.get("/devices")
def get_devices(db: Session = Depends(get_db)):
    return db.query(models.Device).all()

@app.post("/devices")
def create_device(device: schemas.DeviceCreate, db: Session = Depends(get_db)):
    new_device = models.Device(name=device.name)
    db.add(new_device)
    db.commit()
    db.refresh(new_device)
    return new_device

# -------- READINGS --------
# -------- READINGS --------
@app.post("/readings")
def create_reading(reading: schemas.ReadingCreate, db: Session = Depends(get_db)):
    new_reading = models.Reading(**reading.dict())
    db.add(new_reading)
    db.commit()
    return {"mensaje": "Lectura guardada"}

@app.get("/readings")
def get_readings(db: Session = Depends(get_db)):
    return db.query(models.Reading).all()

# -------- COMMANDS --------
@app.post("/commands")
def create_command(command: schemas.CommandCreate, db: Session = Depends(get_db)):
    new_command = models.Command(**command.dict())
    db.add(new_command)
    db.commit()
    return {"mensaje": "Comando enviado"}

@app.get("/commands/latest")
def get_latest_command(db: Session = Depends(get_db)):
    return db.query(models.Command).order_by(models.Command.id.desc()).first()
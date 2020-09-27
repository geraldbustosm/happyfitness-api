from typing import List
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Cors
origins = [
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get
@app.get("/sedes/", response_model=List[schemas.Sede])
def read_sedes(db: Session = Depends(get_db)):
    users = crud.get_sedes(db)
    return users

@app.get("/sede/{sede_id}", response_model=schemas.Sede)
def read_sede(sede_id:int, db: Session = Depends(get_db)):
    sede = crud.get_sede(db, sede_id=sede_id)
    if sede is None:
        raise HTTPException(status_code=404, detail="Sede not found")
    return sede

@app.get("/motivos/", response_model=List[schemas.Motivo])
def read_motivos(db: Session = Depends(get_db)):
    motivos = crud.get_motivos(db)
    return motivos

@app.get("/motivo/{motivo_id}", response_model=schemas.Motivo)
def read_motivo(motivo_id: int, db: Session = Depends(get_db)):
    motivo = crud.get_motivo(db, motivo_id=motivo_id)
    if motivo is None:
        raise HTTPException(status_code=404, detail="Motivo not found")
    return motivo

@app.get("/votaciones/", response_model=List[schemas.Votacion])
def read_votaciones(db: Session = Depends(get_db)):
    votaciones = crud.get_votaciones(db)
    return votaciones

@app.get("/votacion/{votacion_id}", response_model=schemas.Votacion)
def read_votacion(votacion_id:int, db: Session = Depends(get_db)):
    votacion = crud.get_votacion(db, votacion_id=votacion_id)
    if votacion is None:
        raise HTTPException(status_code=404, detail="Votacion not found")
    return votacion
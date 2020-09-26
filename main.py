from typing import List
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS
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

@app.get("/sedes/", response_model=List[schemas.Sede])
def read_sedes(db: Session = Depends(get_db)):
    users = crud.get_sedes(db)
    return users

@app.get("/sede/{sede_id}", response_model=schemas.Sede)
def read_users(sede_id:int, db: Session = Depends(get_db)):
    db_sede = crud.get_sede(db, sede_id=sede_id)
    if db_sede is None:
        raise HTTPException(status_code=404, detail="Sede not found")
    return db_sede


@app.get("/motivo/{motivo_id}", response_model=schemas.Motivo)
def read_user(motivo_id: int, db: Session = Depends(get_db)):
    db_motivo = crud.get_motivos(db, motivo_id=motivo_id)
    if db_motivo is None:
        raise HTTPException(status_code=404, detail="Motivo not found")
    return db_motivo
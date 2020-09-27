from typing import List, Optional

from pydantic import BaseModel

class VotacionBase(BaseModel):
    calificacion: int
    razon: Optional[str] = None
    motivo_id: int

class VotacionCreate(VotacionBase):
    pass

class Votacion(VotacionBase):
    id: int
    class Config:
        orm_mode = True

class MotivoBase(BaseModel):
    nombre: str
    correlativo: int
    sede_id: int

class MotivoCreate(MotivoBase):
    pass

class Motivo(MotivoBase):
    id: int
    votaciones: List[Votacion] = []

    class Config:
        orm_mode = True
        
class SedeBase(BaseModel):
    nombre: str

class SedeCreate(SedeBase):
    pass

class Sede(SedeBase):
    id: int
    motivos: List[Motivo] = []

    class Config:
        orm_mode = True
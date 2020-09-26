from typing import List

from pydantic import BaseModel

class MotivoBase(BaseModel):
    nombre: str
    correlativo: int

class MotivoCreate(MotivoBase):
    pass

class Motivo(MotivoBase):
    id: int
    sede_id: int

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
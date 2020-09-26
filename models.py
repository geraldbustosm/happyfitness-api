from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Sede(Base):
    __tablename__ = "sedes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True, nullable=False)
    motivos = relationship("Motivo", back_populates="sede")


class Motivo(Base):
    __tablename__ = "motivos"
    id = Column(Integer, primary_key=True, index=True)
    sede_id = Column(Integer, ForeignKey("sedes.id"))
    nombre = Column(String, index=True)
    correlativo = Column(Integer, index=True)
    sede = relationship("Sede", back_populates="motivos")
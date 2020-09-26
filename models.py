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
    votaciones = relationship("Votacion", back_populates="motivo")


class Votacion(Base):
    __tablename__ = "votaciones"
    id = Column(Integer, primary_key=True, index=True)
    motivo_id = Column(Integer, ForeignKey("motivos.id"))
    calificacion = Column(Integer, index=True, nullable=False)
    razon = Column(String, index=True)
    motivo = relationship("Motivo", back_populates="votaciones")
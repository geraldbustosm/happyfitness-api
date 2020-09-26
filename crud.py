from sqlalchemy.orm import Session

import models, schemas

def get_sedes(db: Session):
    return db.query(models.Sede).all()


def get_sede(db: Session, sede_id: int):
    return db.query(models.Sede).filter(models.Sede.id == sede_id).first()


def get_motivos(db: Session, motivo_id: int):
    return db.query(models.Motivo).filter(models.Motivo.id == motivo_id).first()
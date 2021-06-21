from sqlalchemy.orm import Session
from models import models
from schemas import schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    patients = db.query(models.Patient).all()
    return patients


def create(request: schemas.PatientCreate, db: Session):
    new_patient = models.Patient(
        first_name=request.first_name,
        last_name=request.last_name,
        gender=request.gender,
        birth_date=request.birth_date,
        nationality=request.nationality,
        email_address=request.email_address
    )
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient


def show(id: int, db: Session):
    patient = db.query(models.Patient).filter(models.Patient.id == id).first()
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient with the id:{id} is not available")
    return patient


def update(id: int, request: schemas.Patient, db: Session):
    patient = db.query(models.Patient).filter(models.Patient.id == id)

    if not patient.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient with id:{id} not found")

    patient.update(request.dict())
    db.commit()
    patient = db.query(models.Patient).filter(models.Patient.id == id).first()
    return patient


def delete(id: int, db: Session):
    patient = db.query(models.Patient).filter(models.Patient.id == id)

    if not patient.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient with id:{id} not found")

    patient.delete(synchronize_session=False)
    db.commit()
    return {'status': 'record deleted'}


def add_allergies(id: int, request: schemas.Allergy, db: Session):
    new_allergy = models.PatientAllergy(
        patient_id=id,
        reaction=request.reaction,
        description=request.description
    )
    db.add(new_allergy)
    db.commit()
    db.refresh(new_allergy)
    return new_allergy


def show_allergies(id: int, db: Session):
    patient = db.query(models.Patient).filter(models.Patient.id == id).first()
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient with the id:{id} is not available")
    return patient


def update_patient_allergy(patient_id: int, id: int, request: schemas.Allergy, db: Session):
    patient_allergy = db.query(models.PatientAllergy).filter(models.PatientAllergy.patient_id == patient_id, models.PatientAllergy.id == id)

    if not patient_allergy.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Allergy with id:{id} not found")

    patient_allergy.update(request.dict())
    db.commit()
    patient_allergy = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    return patient_allergy


def delete_patient_allergy(patiend_id: int, id: int, db: Session):
    patient_allergy = db.query(models.PatientAllergy).filter(models.PatientAllergy.patient_id == patiend_id, models.PatientAllergy.id == id)

    if not patient_allergy.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient Allergy id:{id} not found")

    patient_allergy.delete(synchronize_session=False)
    db.commit()
    return 'deleted'


def show_summary(id: int, db: Session):
    patient = db.query(models.Patient).filter(models.Patient.id == id).first()
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient with the id:{id} is not available")
    return patient

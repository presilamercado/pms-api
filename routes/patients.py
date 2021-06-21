from fastapi import APIRouter
from typing import List, Dict
from core import database
from schemas import schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException
from repository import patient

get_db = database.get_db

router = APIRouter()


@router.get('', response_model=List[schemas.ShowPatient], status_code=status.HTTP_200_OK)
def list_all_patients(db: Session = Depends(get_db)):
    return patient.get_all(db)


@router.get('/{id}', response_model=schemas.ShowPatient, status_code=status.HTTP_200_OK)
def get_patient_details(id: int, db: Session = Depends(get_db)):
    return patient.show(id, db)


@router.post('', status_code=status.HTTP_201_CREATED)
async def create_new_patient(request: schemas.PatientCreate, db: Session = Depends(get_db)):
    return patient.create(request, db)


@router.put('/{id}', response_model=schemas.ShowPatient, status_code=status.HTTP_202_ACCEPTED)
def update_patient(id: int, request: schemas.Patient, db: Session = Depends(get_db)):
    return patient.update(id, request, db)


@router.delete('/{id}')
def delete_patient(id: int, db: Session = Depends(get_db)):
    return patient.delete(id, db)


@router.get("/{id}/summary", response_model=schemas.ShowSummary, status_code=status.HTTP_200_OK)
async def get_patient_summary(id: int, db: Session = Depends(get_db)):
    return patient.show_summary(id, db)


@router.get("/{id}/allergies", response_model=schemas.ShowAllergy,  status_code=status.HTTP_200_OK)
async def get_patient_allergies(id: int, db: Session = Depends(get_db)):
    return patient.show_allergies(id, db)


@router.post("/{id}/allergies", status_code=status.HTTP_201_CREATED)
async def add_patient_allergy(id: int, request: schemas.AllergyCreate, db: Session = Depends(get_db)):
    return patient.add_allergies(id, request, db)


@router.put('/{patient_id}/allergies/{id}', response_model=schemas.ShowAllergy, status_code=status.HTTP_202_ACCEPTED)
def update_patient_allergy(patient_id: int, id: int, request: schemas.AllergyBase, db: Session = Depends(get_db)):
    return patient.update_patient_allergy(patient_id, id, request, db)


@router.delete('/{patient_id}/allergies/{id}', status_code=status.HTTP_200_OK)
def delete_patient_allergy(patient_id: int, id: int, db: Session = Depends(get_db)):
    return patient.delete_patient_allergy(patient_id, id, db)




from typing import List, Optional
from datetime import date
from pydantic import BaseModel


class PatientBase(BaseModel):
    first_name: str
    last_name: str
    gender: str
    birth_date: date
    nationality: str
    email_address: str


class AllergyBase(BaseModel):
    description: str
    reaction: str


class Allergy(AllergyBase):
    id: int
    patient_id: int
    class Config():
        orm_mode = True

class AllergyCreate(AllergyBase):
    pass


class PatientCreate(PatientBase):
    pass


class ShowPatient(BaseModel):
    id: int
    first_name: str
    last_name: str
    gender: str
    birth_date: date
    nationality: str
    email_address: str

    class Config():
        orm_mode = True


class ShowAllergy(Allergy):
    class Config():
        orm_mode = True

class ShowAllergies(BaseModel):
    patient_allergies: List[Allergy] = []
    class Config():
        orm_mode = True

class ShowSummary(PatientBase):
    id: int
    patient_allergies: List[Allergy] = []

    class Config():
        orm_mode = True


class Patient(PatientBase):
    class Config():
        orm_mode = True



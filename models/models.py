from sqlalchemy import Column, Integer, String, ForeignKey, Date
from core.database import Base
from sqlalchemy.orm import relationship

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    birth_date = Column(Date)
    nationality = Column(String)
    email_address = Column(String)

    patient_allergies = relationship('PatientAllergy', back_populates="creator")

class PatientAllergy(Base):
    __tablename__ = 'patient_allergies'

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    description = Column(String)
    reaction = Column(String)

    creator = relationship("Patient", back_populates="patient_allergies")
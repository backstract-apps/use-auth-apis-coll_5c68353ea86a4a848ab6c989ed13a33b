from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud_service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()

@router.post('/persons/', response_model=schemas.ReadPersonsSchema)
def create_persons(persons: schemas.CreatePersonsSchema, database: Session = Depends(get_db)):
    return crud_service.create_persons(database=database, persons=persons)

@router.get('/persons/', response_model=List[schemas.ReadPersonsSchema])
def read_personss(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    return crud_service.get_persons(database=database, skip=skip, limit=limit)

@router.get('/persons/{rollnumber}', response_model=schemas.ReadPersonsSchema)
def read_persons(rollnumber: int, database: Session = Depends(get_db)):
    db_persons = crud_service.get_persons_by_id(database=database, rollnumber=rollnumber)
    if db_persons is None:
        raise HTTPException(status_code=404, detail='Item not found')
    return db_persons

@router.put('/persons/{rollnumber}', response_model=schemas.ReadPersonsSchema)
def update_persons(rollnumber: int, persons: schemas.CreatePersonsSchema, database: Session = Depends(get_db)):
    db_persons = crud_service.update_persons(database=database, rollnumber=rollnumber, persons=persons)
    if db_persons is None:
        raise HTTPException(status_code=404, detail='Item not found')
    return db_persons

@router.delete('/persons/{rollnumber}')
def delete_persons(rollnumber: int, database: Session = Depends(get_db)):
    db_persons = crud_service.delete_persons(database=database, rollnumber=rollnumber)
    if db_persons is None:
        raise HTTPException(status_code=404, detail='Item not found')
    return db_persons


from sqlalchemy.orm import Session
import models, schemas

def get_persons(database: Session, skip: int = 0, limit: int = 100):
    return database.query(models.Persons).offset(skip).limit(limit).all()

def get_persons_by_id(database: Session, rollnumber: int):
    return database.query(models.Persons).filter(models.Persons.rollnumber == rollnumber).first()

def create_persons(database: Session, persons: schemas.CreatePersonsSchema):
    db_persons = models.Persons(**persons.dict())
    database.add(db_persons)
    database.commit()
    database.refresh(db_persons)
    return db_persons

def update_persons(database: Session, rollnumber: int, persons: schemas.CreatePersonsSchema):
    db_persons = database.query(models.Persons).filter(models.Persons.rollnumber == rollnumber).first()
    if db_persons is None:
        return None
    for key, value in persons.dict().items():
        setattr(db_persons, key, value)
    database.commit()
    database.refresh(db_persons)
    return db_persons

def delete_persons(database: Session, rollnumber: int):
    db_persons = database.query(models.Persons).filter(models.Persons.rollnumber == rollnumber).first()
    if db_persons is None:
        return None
    database.delete(db_persons)
    database.commit()
    return db_persons


from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException

def create_contact(db: Session, contact: schemas.ContactCreate):
    new = models.Contact(**contact.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

def get_contacts(db: Session):
    return db.query(models.Contact).all()

def search_contact(db: Session, name: str):
    return db.query(models.Contact).filter(
        models.Contact.name.contains(name)
    ).all()

def update_contact(db: Session, id: int, phone: str):
    contact = db.query(models.Contact).filter(models.Contact.id == id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")

    contact.phone = phone
    db.commit()
    return contact

def delete_contact(db: Session, id: int):
    contact = db.query(models.Contact).filter(models.Contact.id == id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")

    db.delete(contact)
    db.commit()
    return contact
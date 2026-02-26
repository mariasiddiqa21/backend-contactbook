from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException

def get_contacts(db):
    return db.query(models.Contact).all()

def create_contact(db, contact):
    new_contact = models.Contact(**contact.dict())
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact

def update_contact(db, contact_id, data: schemas.ContactCreate):
    contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    
    contact.name = data.name
    contact.phone = data.phone
    contact.email = data.email
    db.commit()
    db.refresh(contact)
    return contact


def delete_contact(db, contact_id):
    contact = db.query(models.Contact).get(contact_id)
    db.delete(contact)
    db.commit()

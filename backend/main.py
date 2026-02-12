from fastapi import FastAPI, Depends,HTTPException, Query ,Path
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine
from products import get_all_products


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
@app.get("/")
def root():
    return {"message": "Hello World"}


#@app.get("/products")
# def list_products(
#     name: str | None = Query(
#         default=None,
#         min_length=1,
#         max_length=10,
#         description="Name of the contact to search for"
#     )
# ):
#     products = get_all_products()

#     if not products:
#         raise HTTPException(status_code=404, detail="No contacts found")

#     # Search case
#     if name:
#         products = [
#             product for product in products
#             if name.lower() in product["name"].lower()
#         ]

#         if not products:
#             raise HTTPException(
#                 status_code=404,
#                 detail="Contact not found with that name"
#             )

#     return {
#         "total_contacts": len(products),
#         "contacts": products
#     }
    
# @app.get("/contact/{id}")
# def get_contact_by_id(
#     id: int = Path(
#         ...,
#         gt=0,
#         description="The ID of the contact to get",
#         example=4
#     )
# ):          
#     products=get_all_products()
#     for product in products:
#         if product["id"] == id:
#             return product   
#     raise HTTPException(status_code=404, detail="Contact not found")    


@app.post("/contact", response_model=schemas.ContactResponse)
def add_contact(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    return crud.create_contact(db, contact)

@app.get("/contact", response_model=list[schemas.ContactResponse])
def get_all(db: Session = Depends(get_db)):
    return crud.get_contacts(db)

@app.get("/contact/search")
def search(name: str, db: Session = Depends(get_db)):
    return crud.search_contact(db, name)



@app.put("/contact/{id}")
def update(id: int, phone: str, db: Session = Depends(get_db)):
    return crud.update_contact(db, id, phone)


@app.delete("/contact/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return crud.delete_contact(db, id)


from fastapi import FastAPI, Depends,HTTPException, Query ,Path
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine
from products import get_all_products
from fastapi.middleware.cors import CORSMiddleware



from database import engine, Base
from models import Contact

Base.metadata.create_all(bind=engine)
print("Database created successfully!")

app = FastAPI()
origins = [
    "http://localhost:3000",
    "http://localhost:3002",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        


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


@app.get("/contacts")
def get_contacts(db: Session = Depends(get_db)):
    return crud.get_contacts(db)

@app.post("/contacts")
def add_contact(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    return crud.create_contact(db, contact)

@app.put("/contacts/{id}")
def update_contact(id: int, contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    return crud.update_contact(db, id, contact)

@app.delete("/contacts/{id}")
def delete_contact(id: int, db: Session = Depends(get_db)):
    return crud.delete_contact(db, id)

from sqlalchemy import Column,Integer,String
from database import Base

class Contact(Base):
    __tablename__="contact"
    id=Column(Integer,primary_key=True)
    name =Column (String)
    phone=Column(String)    
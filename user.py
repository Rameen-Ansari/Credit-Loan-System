from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy.sql import func
from App.DB.base import base

class user(base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,index=True,nullable=False,unique=True)
    hashpwd=Column(String,nullable=False)
    fullname=Column(String,nullable=True)
    income=Column(Integer,nullable=True)
    emp_type=Column(String,nullable=True)
    created_at=Column(DateTime(timezone=True),server_default=func.now())
    

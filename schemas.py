from pydantic import BaseModel
from datetime import date,time


class USERS(BaseModel):
    Address : str
    Email : str
    Location : str
    Mobile : str
    Name : str
    UID : str

    class Config:
        orm_mode = True

class FAQ(BaseModel):
	questions: str
	answers: str

	class Config:
		orm_mode = True

class CATEGORIES(BaseModel):
    category_name : str 
    category_icon : str 

    class Config:
        orm_mode = True

class Donationsschema(BaseModel):
    UID : str
    did : str
    Category : str
    isDonation : str
    Description : str
    donor_address : str
    donor_name : str
    location : str
    postedtime : str
    expirytime : str
    quantity : str
    title : str
    user : str
    image : str
    class Config:
        orm_mode = True
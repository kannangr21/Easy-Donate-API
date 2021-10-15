from uuid import uuid4

import uvicorn
from fastapi import Depends, FastAPI
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

def get_db():
	db = SessionLocal()
	try:
		yield db 
	finally:
		db.close()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "https://easy-donate-api.herokuapp.com/", "http://easy-donate-api.herokuapp.com/",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
ROOT
"""
@app.get('/')
def root():
	return{'message':'Server is Running!!'}


"""
USERS

"""
def create_an_user(db,user_data):
	user_id = uuid4()
	print(user_id)
	db_user = db.query(models.Users).filter(models.Users.UID == str(user_id)).first()
	if db_user:
		{"message" : "User already exists!"}
	db_user = models.Users(
		Address = user_data.Address,
		Email = user_data.Email,
    	Location = user_data.Location,
		Mobile = user_data.Mobile,
		Name = user_data.Name,
		UID = str(user_id)
	)
	db.add(db_user)
	db.commit()
	db.refresh(db_user)
	return db_user

def get_user(db, uid):
	db_user = db.query(models.Users).filter(models.Users.UID == uid).first()
	db_user = jsonable_encoder(db_user)
	del db_user["UID"]
	return db_user



"""
FAQ

"""
def get_questions_all(db:Session):
	return db.query(models.faqtable).all()

def get_questions_id(db:Session,question_id:int):
	return db.query(models.faqtable).where(models.faqtable.faqid == question_id).first()

def create_faq(db:models.faqtable,sets: schemas.FAQ):
	db_faq = models.faqtable(**sets.dict())
	db.add(db_faq)
	db.commit()
	db.refresh(db_faq)
	return db_faq

"""CATEGORIES"""

def get_all_categories(db:Session):
	return db.query(models.Categories).all()

def create_category(db:Session,category_data:schemas.CATEGORIES):
	db_categories = models.Categories(
			category_name = category_data.category_name,
			category_icon = category_data.category_icon
		)
	db.add(db_categories)
	db.commit()
	db.refresh(db_categories)
	return db_categories

"""
USERS Endpoints
"""
@app.post('/user/create')
def create_user(user_data : schemas.USERS, db:Session = Depends(get_db)):
	return create_an_user(db, user_data)

@app.get('/user/{uid}')
def user(uid : str, db : Session = Depends(get_db)):
	return get_user(db, uid)


"""
FAQ Endpoints
"""

@app.get('/faqs/')
def get_qs(db:Session=Depends(get_db)):
	return get_questions_all(db)

@app.get('/faqs/{qid}')
def get_qs_id(qid:int,db:Session = Depends(get_db)):
	return  get_questions_id(db,qid)

@app.post('/faqs/')
def create_question_answer(sets:schemas.FAQ,db:Session = Depends(get_db)):
	db_faq = create_faq(db,sets)
	return db_faq

"""CATEGORIES Endpoints"""

#Returning all categories

@app.get('/categories/')			#This path decorator should be in first. Don't change the order
def get_categories(db:Session = Depends(get_db)):
	return get_all_categories(db)

#Posting new category
@app.post('/categories/')
def post_category(category_data:schemas.CATEGORIES,db:Session = Depends(get_db)):
	return create_category(db,category_data)

	

"""Donations API"""
@app.get("/donations/", response_model=List[schemas.Donationsschema])
def get_donations(db : Session = Depends(get_db)):
    db_donate = db.query(models.donationstable).all()
    if db_donate:
        return db_donate
    else:
        raise HTTPException(status_code=404, detail = "No donations found")   

@app.get("/donations/{id}", response_model = schemas.Donationsschema)
def get_donations_by_id(id : int, db : Session = Depends(get_db)):
    x = db.query(models.donationstable).filter(models.donationstable.did == id).first()
    if x:
        return x
    else:
    	raise HTTPException(status_code=404, detail = "No donation found")

@app.post("/donations/add/", response_model = schemas.Donationsschema)
def create_donation(context : schemas.Donationsschema, db : Session = Depends(get_db)):
    x = db.query(models.donationstable).filter(models.donationstable.did == context.did).first()
    if x:
        raise HTTPException(status_code = 400 ,detail = "Donations Already Exists!!") 
    try:
        db_donations = models.donationstable(
            did = context.did,
            Category = context.Category,
            isDonation = context.isDonation,
            Description = context.Description,
            donor_address = context.donor_address,
            donor_name = context.donor_name,
            location = context.location,
            postedtime = context.postedtime,
            date = context.date,
            time = context.time,
            quantity = context.quantity,
            title = context.title,
            user = context.user,
            image = context.image,
        )
        db.add(db_donations)
        db.commit()
        db.refresh(db_donations)
        return db_donations  
    except Exception as e:
        print(e)  

if __name__ == "__main__":
	uvicorn.run(app, DEBUG = True)

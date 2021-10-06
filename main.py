from uuid import uuid4

import uvicorn
from fastapi import Depends, FastAPI
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

import models
import schemas
from database import SessionLocal, engine


def get_db():
	db = SessionLocal()
	try:
		yield db 
	finally:
		db.close()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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

@app.get('/')
def root():
	return{'message':'Server is Running!!'}

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

if __name__ == "__main__":
	uvicorn.run(app, DEBUG = True)

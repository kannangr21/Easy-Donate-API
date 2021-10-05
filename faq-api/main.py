from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional,List
from sqlalchemy import Column,Integer,String,create_engine
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite+pysqlite:///./db.sqlite3:'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

def get_db():
	db = SessionLocal()
	try:
		yield db 
	finally:
		db.close()

class faqtable(Base):
	__tablename__ = 'faqs'
	faqid = Column(Integer,primary_key=True,index=True)
	questions = Column(String)
	answers = Column(String)

Base.metadata.create_all(bind=engine)

class FAQ(BaseModel):
	question: str
	answer: str

	class Config:
		orm_mode = True

app = FastAPI()

def get_questions_all(db:Session):
	return db.query(faqtable).all()

def get_questions_id(db:Session,question_id:int):
	return db.query(faqtable).where(faqtable.faqid == question_id).first()

def create_faq(db:faqtable,sets: FAQ):
	db_faq = faqtable(**sets.dict())
	db.add(db_faq)
	db.commit()
	db.refresh(db_faq)
	return db_faq

@app.get('/')
async def root():
	return{'message':'Server is Running!!'}

@app.get('/faqs/',response_model=List[FAQ])
def get_qs(db:Session=Depends(get_db)):
	return get_questions_all(db)

@app.get('/faqs/{qid}')
def get_qs_id(qid:int,db:Session = Depends(get_db)):
	return get_questions_id(db,qid)

@app.post('/faqs/',response_model=FAQ)
def create_question_answer(sets:FAQ,db:Session = Depends(get_db)):
	db_faq = create_faq(db,sets)
	return db_faq





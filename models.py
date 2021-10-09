from sqlalchemy import Column, Integer, String

from database import Base


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    Address = Column(String)
    Email = Column(String)
    Location = Column(String)
    Mobile = Column(String)
    Name = Column(String)
    UID = Column(String)


class faqtable(Base):
	__tablename__ = 'faqs'
	faqid = Column(Integer,primary_key=True,index=True)
	questions = Column(String)
	answers = Column(String)

class Categories(Base):
    __tablename__ = 'categories'
    id = Column(Integer,primary_key=True)
    category_name = Column(String)
    category_icon = Column(String)
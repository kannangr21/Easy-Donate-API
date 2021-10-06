from pydantic import BaseModel


class USERS(BaseModel):
    Address : str
    Email : str
    Location : str
    Mobile : str
    Name : str

    class Config:
        orm_mode = True

class FAQ(BaseModel):
	questions: str
	answers: str

	class Config:
		orm_mode = True

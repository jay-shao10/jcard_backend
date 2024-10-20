from sqlalchemy.orm import relationship
from app.db.connect_db import Base, get_session
from sqlalchemy import Column, Integer, String, Identity
from app.db.article import Article

class User(Base):
    __tablename__ = "USER"
    u_id = Column(Integer, Identity(start=1, increment=1, always=True), primary_key=True)
    u_name = Column(String, nullable=False)
    email=Column(String, nullable=False)
    password=Column(String, nullable=False)
    articles = relationship("Article", back_populates="user")

    def __init__(self, u_name,email,password):
        self.u_name = u_name
        self.email = email
        self.password =password

def insert_user_indb(insert_user:str,insert_email:str,insert_password:str):
    session = get_session()
    try:
        insert_user_todb = User(u_name=insert_user,email=insert_email,password=insert_password)
        session.add(insert_user_todb)
        session.commit()
        
    finally:
        # Close the session
        session.close()

def query_user_indb(query_email:str,query_password:str):
    session=get_session()
    try:
        user=session.query(User).filter_by(email=query_email,password=query_password).first()
        return user

    finally:
        session.close()



  
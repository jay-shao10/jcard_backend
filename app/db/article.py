from sqlalchemy import Column, Integer, String, Identity,Text, TIMESTAMP,func, ForeignKey
from sqlalchemy.orm import relationship, joinedload
from app.db.connect_db import Base, get_session


class Article(Base):
    __tablename__ = "ARTICLE"
    a_id = Column(Integer, Identity(start=1, increment=1, always=True), primary_key=True)
    a_title= Column(String, nullable=False)
    a_content=Column(Text, nullable=False)
    create_time=Column(TIMESTAMP,server_default=func.now(),nullable=False)
    t_id = Column(Integer, ForeignKey('TOPIC.t_id'), nullable=False)
    u_id = Column(Integer, ForeignKey('USER.u_id'), nullable=False)

    # Define relationship to Topic (optional but useful for ORM queries)
    topic = relationship("Topic", back_populates="articles")
    user = relationship("User", back_populates="articles")

    def __init__(self, a_title,a_content,t_id,u_id):
        self.a_title = a_title
        self.a_content=a_content
        self.t_id=t_id
        self.u_id=u_id

def insert_article_indb(insert_title:str,insert_content:str,insert_tid:int,insert_uid:int):

    session = get_session()
    try:
        insert_article_todb = Article(a_title=insert_title,a_content=insert_content,t_id=insert_tid,u_id=insert_uid)
        session.add(insert_article_todb)
        session.commit()
        
    finally:
        # Close the session
        session.close()

def get_article_indb(insert_id:int):

    session=get_session()
    try:
        article=session.query(Article).options(joinedload(Article.user)).filter_by(a_id=insert_id).first()
        return article

    finally:
        session.close()
       
def get_titles_indb(insert_id:int):

    session=get_session()
    try:
        titles=session.query(Article).filter_by(t_id=insert_id).all()
        return titles

    finally:
        session.close()
          
    
    
    
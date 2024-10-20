from sqlalchemy import Column, Integer, String, Identity
from app.db.connect_db import Base, get_session
from sqlalchemy.orm import relationship
from app.db.article import Article

class Topic(Base):
    __tablename__ = "TOPIC"
    t_id = Column(Integer, Identity(start=1, increment=1, always=True), primary_key=True)
    t_name = Column(String, nullable=False)
     # Define relationship to Article
    articles = relationship("Article", back_populates="topic")

    def __init__(self, t_name):
        self.t_name = t_name

def get_all_topic_indb():
    session = get_session()
    try:
        # Query all topics and select only t_id and t_name
        topics = session.query(Topic).all()
        for item in topics:
            print(f'Value:{item},Type:{type(item)}')
        return topics
    finally:
        # Close the session
        session.close()

def insert_topic_indb(insert_topic:str):
    session = get_session()
    try:
        insert_topic_todb = Topic(t_name=insert_topic)
        session.add(insert_topic_todb)
        session.commit()
        
    finally:
        # Close the session
        session.close()
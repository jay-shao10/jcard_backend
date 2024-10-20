# python -m app.db.init_db
from  app.db.connect_db import Base, engine
from  app.db.topic import Topic
from  app.db.user import User
from  app.db.article import Article

def create_tables():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_tables()

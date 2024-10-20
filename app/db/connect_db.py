from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Database connection information
load_dotenv()
db_host =os.getenv('DB_HOST')
db_port =os.getenv('DB_PORT')
db_name =os.getenv('DB_NAME')
db_user =os.getenv('DB_USER')
db_password =os.getenv('DB_PASSWORD')

# PostgreSQL connection string
connection_string = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Create an engine
engine = create_engine(connection_string, echo=True)

# Create a base class for declarative models
Base = declarative_base()

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a new session instance
def get_session():
    return Session()

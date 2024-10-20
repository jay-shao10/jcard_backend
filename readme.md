run python -m app.db.init_db ->create tables(user, topic) 
uvicorn app.main:app --reload  
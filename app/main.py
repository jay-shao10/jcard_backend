from fastapi import FastAPI
from app.api.user import view as user_view
from app.api.topic import view as topic_view
from app.api.article import view as article_view
from app.middleware.log import LoggingMiddleware

app = FastAPI()
app.include_router(user_view.router)
app.include_router(topic_view.router)
app.include_router(article_view.router)
app.add_middleware(LoggingMiddleware)
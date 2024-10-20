from typing import Optional,List
from fastapi import APIRouter, Depends
from app.api.article.model import get_article_response, get_titles_response, insert_article_request
from app.api.user.model import TokenData
from app.api.user.view import get_current_user
from app.db.article import get_article_indb, get_titles_indb,insert_article_indb

router = APIRouter(
    prefix="/article",
    tags=["articles"],
)

@router.post("/create_article")
def insert_article(rq: insert_article_request, current_user: TokenData = Depends(get_current_user)) -> None:
    insert_article_indb(rq.a_title,rq.a_content,rq.t_id,rq.u_id)
   

@router.get("")
def get_article(article_id:int)->Optional[get_article_response]:
    article=get_article_indb(article_id)
    if article is not None:
        response=get_article_response(
            a_id=article.a_id,
            a_title=article.a_title,
            a_content=article.a_content,
            create_time=article.create_time,
            u_id=article.u_id,
            u_name=article.user.u_name,
        )
    else:
        response = get_article_response(
            a_title=None,
            a_content=None,
            create_time=None,
            u_id=None,
        )
        return None
    
    return response



@router.get("/titles")
def get_tilie_by_topic_id(topic_id:int)->List[get_titles_response]| None:
    titles=get_titles_indb(topic_id)
    res=[]
    if titles is not None:
        for item in titles:
            temp=get_titles_response(a_id=item.a_id,a_title=item.a_title,create_time=item.create_time,u_id=item.u_id)
            res.append(temp)

    else:
        return None
    
    return res

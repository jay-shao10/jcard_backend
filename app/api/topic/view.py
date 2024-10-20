from typing import List
from fastapi import APIRouter
from app.api.topic.model import get_all_topic_response, insert_topic_request
from app.db.topic import Topic, get_all_topic_indb, insert_topic_indb
from app.utils.helper import get_topic_rating_by_id
from app.utils.s3_helper import get_topic_icon_by_topic_name

router = APIRouter(
    prefix="/topic",
    tags=["topics"],
)


@router.get("/all")
def get_all_topic()->List[get_all_topic_response]:
    topics = get_all_topic_indb()
    res=[]
    for item in topics:
        rating = get_topic_rating_by_id(item.t_id)
        icon=get_topic_icon_by_topic_name(item.t_name)
        temp = get_all_topic_response(t_id=item.t_id,t_name=item.t_name,t_rating=rating,t_icon=icon)
        res.append(temp)
    return res

@router.post("")
def insert_topic(rq:insert_topic_request)->None:
    # Insert the Topic object into the database
    insert_topic_indb(rq.t_name)
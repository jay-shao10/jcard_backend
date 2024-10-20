from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class insert_article_request(BaseModel):
    a_title:str
    a_content:str
    t_id :int
    u_id:int

class get_article_response(BaseModel):
    a_id:Optional[int]=None
    a_title:Optional[str]=None
    a_content:Optional[str]=None
    create_time:Optional[datetime]=None
    u_id:Optional[int]=None
    u_name:Optional[str]=None

class get_titles_response(BaseModel):
    a_id:int
    a_title:str
    create_time:datetime
    u_id:int

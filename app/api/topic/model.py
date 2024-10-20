from pydantic import BaseModel

class get_all_topic_response(BaseModel):
    t_id: int
    t_name: str
    t_rating: int
    t_icon: str

class insert_topic_request(BaseModel):
    t_name:str
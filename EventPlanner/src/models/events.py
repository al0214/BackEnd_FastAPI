from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from sqlmodel import JSON, SQLModel, Field, Column

# SQL을 사용한 이벤트 처리용 모델을 정의
class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str
    
    model_config = ConfigDict(arbitrary_types_allowed = True,
            json_schema_extra = {
                "example" : [
                    {
                    "title" : "FastAPI Book Launch",
                    "image" : "https://linktomyimage.com/image.png",
                    "description" : "We will be discussing the contents of the FastAPI book in the event. Ensure to come with your own copy to win gifts!",
                    "tags" : ["python", "fastapi", "book", "launch"],
                    "location" : "Google Meet"
                    }
                            ]
            }
        
    )

# # 이벤트 처리용 모델을 정의
# class Event(BaseModel):
#     id: int
#     title: str
#     description: str
#     tags: List[str]
#     location: str
    
#     model_config = {
#         "json_schema_extra": {
#             "example" : [
#                 {
#                 "title" : "FastAPI Book Launch",
#                 "image" : "https://linktomyimage.com/image.png",
#                 "description" : "We will be discussing the contents of the FastAPI book in the event. Ensure to come with your own copy to win gifts!",
#                 "tags" : ["python", "fastapi", "book", "launch"],
#                 "location" : "Google Meet"
#                 }
#                          ]
#         }
#     }

class EventUpdate(SQLModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]
    
    model_config = {
         "json_schema_extra" : {
                "example" : [
                    {
                    "title" : "FastAPI Book Launch",
                    "image" : "https://linktomyimage.com/image.png",
                    "description" : "We will be discussing the contents of the FastAPI book in the event. Ensure to come with your own copy to win gifts!",
                    "tags" : ["python", "fastapi", "book", "launch"],
                    "location" : "Google Meet"
                    }
                            ]
            }
    }
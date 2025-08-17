from pydantic import BaseModel
from typing import List

# 이벤트 처리용 모델을 정의
class Event(BaseModel):
    id: int
    title: str
    description: str
    tag: List[str]
    location: str
    
    model_config = {
        "json_schema_extra": {
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
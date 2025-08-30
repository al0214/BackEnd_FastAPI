from typing import Optional, List
from beanie import Document, Link
from pydantic import BaseModel, EmailStr, ConfigDict
from models.events import Event

# 사용자 처리용 모델을 정의

class User(Document):
    email : EmailStr
    password : str
    events : Optional[List[Event]]
    
    model_config = ConfigDict(
        json_schema_extra = {
            "example" : [
                {
                    "email" : "fastapi@packet.com",
                    "username" : "string!!!",
                    "events" : [],
                }
            ]
        }
    )

class UserSiginIn(BaseModel):
    email : EmailStr
    password : str
    
    model_config = ConfigDict(
        json_schema_config = {
            "example" : [
                {
                    "email" : "fastapi@packet.com",
                    "username" : "string!!!",
                    "events" : [],
                }
            ]
        }
    )
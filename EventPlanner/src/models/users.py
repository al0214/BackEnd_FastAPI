from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event

# 사용자 처리용 모델을 정의

class User(BaseModel):
    email : EmailStr
    password : str
    events : Optional[List[Event]]
    
    model_config = {
        "json_schema_extra" : {
            "example" : [
                {
                    "email" : "fastapi@packet.com",
                    "username" : "string!!!",
                    "events" : [],
                }
            ]
        }
    }

class UserSiginIn(BaseModel):
    email : EmailStr
    password : str
    
    model_config = {
        "json_schema_config" : {
            "example" : [
                {
                    "email" : "fastapi@packet.com",
                    "username" : "string!!!",
                    "events" : [],
                }
            ]
        }
    }
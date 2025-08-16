from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form

class Item(BaseModel):
    item: str
    status: str

class Todo(BaseModel):
    id: Optional[int]
    item: str
    
    @classmethod
    def as_form(
        cls,
        item: str = Form(...)
    ):
        return cls(item=item)
    
    class Config:
        model_config = {
            "example": {
                "id": 1,
                "item" : "Example Schema!"
            }
        }
        
class TodoItem(BaseModel):
    item: str
    
    class Config:
        model_config= {
            "example":{
                "item" : "Read the ext chapter of the book."
            }
        }
        
class TodoItems(BaseModel):
    todos: List[TodoItem]
    
    class Config:
        model_config = {
            "example" : {
                "todos" : [
                    {
                        "item" : "Example schema 1!"
                    },
                    {
                        "item" : "Example schema 2!"
                    },
                ]
            }
        }
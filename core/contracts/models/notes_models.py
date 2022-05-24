from pydantic import BaseModel

class NoteBase(BaseModel):
    text:str

class NoteCreate(NoteBase):
    id: int

class Note(NoteCreate):
    class Config:
        orm_mode = True
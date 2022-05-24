from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
DatabaseDtoBase = declarative_base()

class NotesDto(DatabaseDtoBase):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
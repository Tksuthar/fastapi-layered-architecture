from typing import List

from core.contracts.dtos.notes_dtos import NotesDto
from sqlalchemy import update
from sqlalchemy.orm import Session


class NotesData:
    def __init__(self, database_session: Session) -> None:
        self._session = database_session

    async def get_notes(self, skip: int, limit: int) -> List[NotesDto]:
        return self._session.query(NotesDto).offset(skip).limit(limit).all()

    async def get_note(self, note_id: int) -> NotesDto:
        return self._session.query(NotesDto).filter(NotesDto.id == note_id).first()

    async def create_note(self, note: NotesDto) -> None:
        self._session.add(note)
        self._session.commit()

    async def update_note(self, note: NotesDto) -> None:
        self._session.execute(
            update(NotesDto).where(NotesDto.id == note.id).values(text=note.text)
        )

    async def delete_note(self, note_id: int) -> None:
        note = self.get_note(note_id)
        if note:
            self._session.delete(note)
            self._session.commit()

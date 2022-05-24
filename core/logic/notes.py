from core.data.notes_data import NotesData, NotesDto
from typing import List

class NotesLogics:
    def __init__(self, notes_data: NotesData) -> None:
        self._notes_data = notes_data

    async def get_notes(self, skip: int = 0, limit: int = 100) -> List[NotesDto]:
        return await self._notes_data.get_notes(skip=skip, limit=limit)

    async def get_note(self, note_id: int) -> NotesDto:
        return await self._notes_data.get_note(note_id=note_id)

    async def create_note(self, note: NotesDto) -> None:
        await self._notes_data.create_note(note=note)

    async def update_note(self, note: NotesDto) -> None:
        await self._notes_data.update_note(note=note)

    async def delete_note(self, note_id: int) -> None:
        await self._notes_data.delete_note(note_id=note_id)
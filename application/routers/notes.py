from core.contracts.dtos.notes_dtos import NotesDto
from typing import List, Optional

from application import NotesData, NotesLogics, _sql_session_maker
from core.contracts.models.notes_models import NoteBase, Note
from fastapi import APIRouter
from fastapi.params import Depends

router = APIRouter()


def get_logics_session():
    db = _sql_session_maker()
    try:
        yield NotesLogics(notes_data=NotesData(database_session=db))
    finally:
        db.close()


@router.get(
    "/",
    response_model=List[Note],
)
async def get_notes(
    skip: Optional[int] = 0,
    limit: Optional[int] = 100,
    notes_logics: NotesLogics = Depends(get_logics_session),
):
    return await notes_logics.get_notes(skip=skip, limit=limit)


@router.get("/{note_id}", response_model=Note)
async def get_note(
    note_id: int, notes_logics: NotesLogics = Depends(get_logics_session)
):
    return await notes_logics.get_note(note_id)


@router.post("/", response_model=int)
async def create_note(
    new_note: NoteBase, notes_logics: NotesLogics = Depends(get_logics_session)
):
    return await notes_logics.create_note(NotesDto(text=new_note.text))


@router.put("/{note_id}")
async def update_note(
    note_id: int,
    new_note: NoteBase,
    notes_logics: NotesLogics = Depends(get_logics_session),
):
    await notes_logics.update_note(note=NotesDto(id=note_id, text=new_note.text))


@router.delete("/{note_id}")
async def delete_note(
    note_id: int, notes_logics: NotesLogics = Depends(get_logics_session)
):
    await notes_logics.delete_note(note_id)

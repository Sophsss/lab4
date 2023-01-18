from pydantic import BaseModel
from datetime import datetime
from typing import List

class NoteInfoResponse(BaseModel):
    created_at: datetime
    updated_at: datetime

class NoteTextResponse(BaseModel):
    id: int
    text: str

class NoteCreateResponse(BaseModel):
    id: int

class NoteListResponse(BaseModel):
    note_list: List[int]

class NoteDeleteResponse(BaseModel):
    id: int

class NoteUpdateResponse(BaseModel):
    id: int
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class NoteDetailResponseSchema(BaseModel):
    """Schema for note detail response."""

    id: int
    content: str
    created_at: datetime
    updated_at: datetime
    versions: List["NoteVersionDetailResponseSchema"]


class NoteListResponseSchema(BaseModel):
    """Schema for paginated note list response."""

    notes: List[NoteDetailResponseSchema]
    prev_page: Optional[str] = Field(None, description="URL for previous page")
    next_page: Optional[str] = Field(None, description="URL for next page")
    total_pages: int = Field(..., description="Total number of pages")
    total_items: int = Field(..., description="Total number of notes")


class NoteCreateRequestSchema(BaseModel):
    """Schema for creating a new note."""

    content: str = Field(..., description="The content of the note")


class NoteUpdateRequestSchema(BaseModel):
    """Schema for updating an existing note."""

    content: str = Field(..., description="The updated content of the note")


class NoteVersionDetailResponseSchema(BaseModel):
    """Schema for note version detail response."""

    id: int
    note_id: int
    version: int
    content: str
    created_at: datetime


class NoteVersionListResponseSchema(BaseModel):
    """Schema for paginated note version list response."""

    versions: List[NoteVersionDetailResponseSchema]
    prev_page: Optional[str] = Field(None, description="URL for previous page")
    next_page: Optional[str] = Field(None, description="URL for next page")
    total_pages: int = Field(..., description="Total number of pages")
    total_items: int = Field(..., description="Total number of versions")
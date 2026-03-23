from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class FeedbackCreate(BaseModel):
    user_name: str = Field(..., min_length=2, max_length=100)
    # Keep this as a simple string for Step 1 to avoid extra dependencies.
    email: Optional[str] = None
    message: str = Field(..., min_length=5)


class FeedbackRead(BaseModel):
    id: int
    user_name: str
    email: Optional[str] = None
    message: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


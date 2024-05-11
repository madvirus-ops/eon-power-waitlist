import sys

sys.path.append("./")

from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid
import pytz


tz = pytz.timezone("Africa/Lagos")


class AbstractModel(SQLModel):
    """abstract model"""

    pkid: int = Field(primary_key=True)
    id: str = Field(default=uuid.uuid4, unique=True, index=True)
    created_at: datetime = Field(default=datetime.now(tz))
    updated_at: datetime = Field(default=datetime.now(tz))


class WebWaitList(AbstractModel, table=True):

    __tablename__ = "web_waitlist"

    name: Optional[str] = Field(index=True)
    email: str = Field(index=True)

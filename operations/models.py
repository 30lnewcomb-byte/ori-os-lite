from __future__ import annotations

from datetime import date, datetime, timezone
from enum import StrEnum

from pydantic import BaseModel, Field, EmailStr


class ContactRole(StrEnum):
    PERSONAL = "personal"
    SCHOOL = "school"


class Contact(BaseModel):
    role: ContactRole
    email: EmailStr
    enabled: bool = True
    label: str | None = None
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class DeliveryChannel(StrEnum):
    EMAIL = "email"
    CHAT = "chat"


class CalendarMode(StrEnum):
    SCHOOL_DAY = "school_day"
    NON_SCHOOL_DAY = "non_school_day"
    UNKNOWN = "unknown"


class NotificationPolicy(BaseModel):
    school_day_email_role: ContactRole = ContactRole.SCHOOL
    school_day_message_role: ContactRole = ContactRole.SCHOOL
    non_school_day_email_role: ContactRole = ContactRole.SCHOOL
    non_school_day_message_role: ContactRole = ContactRole.PERSONAL
    calendar_timezone: str = "America/New_York"
    require_contact_confirmation: bool = True


class CalendarStatus(BaseModel):
    mode: CalendarMode
    date: date
    source: str | None = None
    reason: str | None = None

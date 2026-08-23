from __future__ import annotations

from datetime import datetime, timezone
from enum import StrEnum
from uuid import uuid4

from pydantic import BaseModel, Field


class Severity(StrEnum):
    INFO = "info"
    MODERATE = "moderate"
    SIGNIFICANT = "significant"
    CRITICAL = "critical"


class OperationEvent(BaseModel):
    event_id: str = Field(default_factory=lambda: f"evt-{uuid4().hex[:12]}")
    title: str
    detail: str
    severity: Severity = Severity.INFO
    requires_approval: bool = False
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    def requires_human_attention(self) -> bool:
        return self.requires_approval or self.severity in {
            Severity.SIGNIFICANT,
            Severity.CRITICAL,
        }

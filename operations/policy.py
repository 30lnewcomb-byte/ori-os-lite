from __future__ import annotations

from .models import CalendarMode, Contact, ContactRole, NotificationPolicy


class ContactBook:
    def __init__(self) -> None:
        self._contacts: dict[ContactRole, Contact] = {}

    def set(self, contact: Contact) -> None:
        self._contacts[contact.role] = contact

    def remove(self, role: ContactRole) -> None:
        self._contacts.pop(role, None)

    def get(self, role: ContactRole) -> Contact | None:
        return self._contacts.get(role)


class NotificationRouter:
    """Resolve where an event should go without sending anything itself."""

    def __init__(self, contacts: ContactBook, policy: NotificationPolicy) -> None:
        self.contacts = contacts
        self.policy = policy

    def resolve(self, mode: CalendarMode, channel: str) -> Contact | None:
        if mode == CalendarMode.SCHOOL_DAY:
            role = (
                self.policy.school_day_email_role
                if channel == "email"
                else self.policy.school_day_message_role
            )
        else:
            role = (
                self.policy.non_school_day_email_role
                if channel == "email"
                else self.policy.non_school_day_message_role
            )

        contact = self.contacts.get(role)
        if contact is None or not contact.enabled:
            return None
        return contact

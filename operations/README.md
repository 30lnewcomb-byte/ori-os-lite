# Ori Operations

This package defines the communication policy for Ori. It is configuration and routing logic only; it does not connect to Gmail or Google Chat yet.

## Contact roles

Contacts are role-based rather than hard-coded addresses:

- `personal` — the user's personal email/contact.
- `school` — the current school email/contact.

A school address can be removed or replaced later without changing application code.

## Current intended policy

### School day

- Email → `school`
- Message → `school`

The school-day message route is intentionally represented as a contact destination. A future delivery adapter can deliver it through email when Google Chat is unavailable during school.

### Non-school day

- Email → `school`
- Message → `personal`

The shared Google Chat destination belongs to the personal communication path.

## Calendar

The policy is designed to consume a calendar-derived mode rather than assuming that every Monday–Friday is a school day. This allows school holidays, breaks, snow days, and other calendar events to affect routing.

The calendar integration is **not connected yet**.

## Safety/configuration rules

- No real email addresses are stored in the repository.
- No Gmail or Google Chat credentials are stored here.
- Contact changes should require explicit confirmation before becoming active.
- Routing resolves contact roles at send time, so an expiring school account can be replaced without changing code.
- Delivery adapters are intentionally separate from routing logic.

## Planned architecture

```text
School Calendar
      |
      v
Calendar Mode
      |
      v
Notification Router
      |
      +--> Email Adapter
      |
      +--> Google Chat Adapter
      |
      v
Configured Contact Role
```

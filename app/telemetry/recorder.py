
from datetime import datetime, timezone


class TraceRecorder:
    """Records agent execution events."""

    def __init__(self):
        self.events = []

    def record(self, event_type: str, data: dict):
        event = {
            "sequence": len(self.events) + 1,
            "event_type": event_type,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "data": data,
        }

        self.events.append(event)
        return event

    def get_events(self):
        return self.events

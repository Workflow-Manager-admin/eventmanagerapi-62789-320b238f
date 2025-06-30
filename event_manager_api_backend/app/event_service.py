from .models import Event


# In-memory event "database"
EVENT_STORE = {}


# PUBLIC_INTERFACE
def create_event(data):
    """Create a new event and store it in memory."""
    event = Event(**data)
    EVENT_STORE[event.id] = event
    return event


# PUBLIC_INTERFACE
def get_event(event_id):
    """Retrieve an event by ID."""
    return EVENT_STORE.get(event_id)


# PUBLIC_INTERFACE
def update_event(event_id, data):
    """Update an existing event."""
    event = EVENT_STORE.get(event_id)
    if not event:
        return None
    event.update(data)
    return event


# PUBLIC_INTERFACE
def delete_event(event_id):
    """Delete an event by ID."""
    return EVENT_STORE.pop(event_id, None)


# PUBLIC_INTERFACE
def list_events():
    """List all events."""
    return [event for event in EVENT_STORE.values()]

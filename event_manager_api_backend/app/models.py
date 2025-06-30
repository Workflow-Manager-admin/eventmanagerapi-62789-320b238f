# Event model for in-memory storage
import uuid
from datetime import datetime


class Event:
    """Event object for in-memory storage."""

    def __init__(self, title, description, start_time, end_time, location):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.start_time = start_time  # ISO 8601 string
        self.end_time = end_time      # ISO 8601 string
        self.location = location
        self.created_at = datetime.utcnow().isoformat()
        self.updated_at = self.created_at

    def update(self, data: dict):
        """Update properties of the event with the new data."""
        for attr in ['title', 'description', 'start_time', 'end_time', 'location']:
            if attr in data:
                setattr(self, attr, data[attr])
        self.updated_at = datetime.utcnow().isoformat()

    def to_dict(self):
        """Convert Event object to dict for JSON response"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "location": self.location,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

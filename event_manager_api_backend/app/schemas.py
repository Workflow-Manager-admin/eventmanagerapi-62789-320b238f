from marshmallow import Schema, fields, validate


# PUBLIC_INTERFACE
class EventSchema(Schema):
    """Schema for an Event object (output)."""
    id = fields.Str(dump_only=True, description="Unique event identifier")
    title = fields.Str(required=True, description="Title of the event")
    description = fields.Str(required=True, description="Event description")
    start_time = fields.Str(required=True, description="Event start time (ISO 8601)")
    end_time = fields.Str(required=True, description="Event end time (ISO 8601)")
    location = fields.Str(required=True, description="Event location")
    created_at = fields.Str(
        dump_only=True,
        description="Record creation datetime (ISO 8601)"
    )
    updated_at = fields.Str(
        dump_only=True,
        description="Last updated datetime (ISO 8601)"
    )


# PUBLIC_INTERFACE
class EventCreateSchema(Schema):
    """Schema for event creation request (input)."""
    title = fields.Str(
        required=True,
        validate=validate.Length(min=1),
        description="Title of the event"
    )
    description = fields.Str(
        required=True,
        validate=validate.Length(min=1),
        description="Event description"
    )
    start_time = fields.Str(
        required=True,
        description="Event start time (ISO 8601)"
    )
    end_time = fields.Str(
        required=True,
        description="Event end time (ISO 8601)"
    )
    location = fields.Str(
        required=True,
        validate=validate.Length(min=1),
        description="Event location"
    )


# PUBLIC_INTERFACE
class EventUpdateSchema(Schema):
    """Schema for partial or full event update (input)."""
    title = fields.Str(
        validate=validate.Length(min=1),
        description="Title of the event"
    )
    description = fields.Str(
        validate=validate.Length(min=1),
        description="Event description"
    )
    start_time = fields.Str(description="Event start time (ISO 8601)")
    end_time = fields.Str(description="Event end time (ISO 8601)")
    location = fields.Str(
        validate=validate.Length(min=1),
        description="Event location"
    )

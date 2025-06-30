from flask_smorest import Blueprint
from flask.views import MethodView

from ..schemas import EventSchema, EventCreateSchema, EventUpdateSchema
from .. import event_service


blp = Blueprint(
    "Events",
    "events",
    url_prefix="/events",
    description="Endpoints for managing events"
)


@blp.route("/")
class EventsList(MethodView):

    # PUBLIC_INTERFACE
    @blp.response(200, EventSchema(many=True), description="List all events")
    def get(self):
        """Get all events"""
        return [e.to_dict() for e in event_service.list_events()]

    # PUBLIC_INTERFACE
    @blp.arguments(EventCreateSchema)
    @blp.response(201, EventSchema, description="Event successfully created")
    def post(self, new_event_data):
        """Create a new event"""
        event = event_service.create_event(new_event_data)
        return event.to_dict()


@blp.route("/<string:event_id>")
class EventDetail(MethodView):

    # PUBLIC_INTERFACE
    @blp.response(200, EventSchema, description="Get an event by ID")
    @blp.alt_response(404, description="Event not found")
    def get(self, event_id):
        """Get event by ID"""
        event = event_service.get_event(event_id)
        if not event:
            blp.abort(404, message="Event not found")
        return event.to_dict()

    # PUBLIC_INTERFACE
    @blp.arguments(EventUpdateSchema)
    @blp.response(200, EventSchema, description="Event updated")
    @blp.alt_response(404, description="Event not found")
    def put(self, update_data, event_id):
        """Update an existing event by ID"""
        event = event_service.update_event(event_id, update_data)
        if not event:
            blp.abort(404, message="Event not found")
        return event.to_dict()

    # PUBLIC_INTERFACE
    @blp.response(204, description="Event deleted successfully")
    @blp.alt_response(404, description="Event not found")
    def delete(self, event_id):
        """Delete an event by ID"""
        deleted = event_service.delete_event(event_id)
        if not deleted:
            blp.abort(404, message="Event not found")
        return '', 204

from app import db
from datetime import datetime

class Event(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime)
    type = db.Column(db.String)
    notes = db.Column(db.String)

    pet_id = db.Column(db.Integer, db.ForeignKey("pet.id"))
    pet = db.relationship("Pet", back_populates = "events")

    @classmethod
    def from_dict(cls, event_data, pet_id):
        new_event = Event(
            type = event_data["type"],
            notes = event_data["notes"],
            timestamp = datetime.utcnow(),
            pet_id = pet_id

        )
        return new_event
    
    def to_dict(self):
        event_dict = {}
        event_dict["id"] = self.id
        event_dict["type"] = self.type
        event_dict["timestamp"] = self.timestamp
        event_dict["notes"] = self.notes

        return event_dict
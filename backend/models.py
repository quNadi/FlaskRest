from backend.db import db
from sqlalchemy import func

class NoteModel(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    text=db.Column(db.String(250))
    timestamp=db.Column(db.DateTime, server_default=func.now())

    def serialize(self):
        return {
            'id': self.id,
            'name' : self.name,
            'text': self.text
        }
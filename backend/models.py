from app import db,mm
from sqlalchemy import func


class NoteModel(db.Model):
    __tablename__='notes'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    content=db.Column(db.String(250))
    timestamp=db.Column(db.DateTime, server_default=func.now())

   # def serialize(self):
   #     return {
   #         'id': self.id,
   #         'name' : self.name,
   #         'content': self.content
   #     }

class NoteSchema(mm.Schema):
    class Meta:
        fields=('id', 'name', 'content','_links')

    _links=mm.Hyperlinks({'self':mm.URLFor('note', id="<id>"), "collection":mm.URLFor('notes')})

notes_schema=NoteSchema(many=True)
note_schema=NoteSchema()

db.create_all()
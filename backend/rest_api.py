from flask import jsonify
from flask_restful import abort,reqparse, Resource
from backend.models import NoteModel,note_schema,notes_schema
from app import db
from flask_cors import cross_origin

parser=reqparse.RequestParser(bundle_errors=True)
parser.add_argument('name', type=str,required=True,help="name is necessary")
parser.add_argument('content',type=str,required=False)

class NotesList(Resource):
    def get(self):
        notes= NoteModel.query.all()
        return {'notes': notes_schema.dump(notes)}
        # return jsonify([NoteModel.serialize(note) for note in notes])

    @cross_origin()
    def post(self):
        args=parser.parse_args()
        note_record=NoteModel(name=args['name'], content=args['content'])       # note_record=NoteModel(**data) ???
        db.session.add(note_record)
        db.session.commit()
        return {'note_record': note_schema.dump(note_record)},201

class NoteRecord(Resource):
    def get(self,note_id):
        note_one=NoteModel.query.filter_by(id=note_id).first_or_404(description="this note is not avaiable")
        return {'note_one':note_schema.dump(note_one)}

    def put(self, note_id):
        args=parser.parse_args()
        note_record=NoteModel.query.filter_by(id=note_id)\
        .first_or_404(description="this not is unavaiable")
        note_record.name=args['name']
        note_record.content=args['content']
        #db.session()
        return {'note_record': note_schema.dump(note_record)},201

    def delete(self,note_id):
        note_record=NoteModel.query.filter_by(id=note_id)\
        .first_or_404(description="note is not avaiable")
        db.session.delete(note_record)
        db.session.commit()
        return {'message': 'note deleted'},204




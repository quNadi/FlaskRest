from flask import jsonify
from flask_restful import abort,reqparse, Resource
from backend.models import NoteModel
from backend.db import db

parser=reqparse.RequestParser(bundle_errors=True)
parser.add_argument('name', type=str,required=True,help="name is necessary")

class NotesList(Resource)
    def get(self):
        notes= NoteModel.query.all()
        return jsonify([NoteModel.serialize(note) for note in notes])

    def post(self):
        args=parser.parse_args()
        note_record=NoteModel(name=args['name'], text=args['text'])
        db.session.add(note_record)
        db.session.commit()
        return NoteModel.serialize(note_record),201

class NoteRecord(Resource):
    def get(self,note_id):
        return jsonify(NoteModel.serialize(NoteModel.query.filter_by(id=note_id).first_or_404(description="this note is not avaiable")))

    def put(self, note_id):
        args=parser.parse_args()
        note_record=

    def delete(self,note_id):
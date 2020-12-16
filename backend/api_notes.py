from flask  import jsonify,request,current_app,url_for ,g
from app import api
from models import NoteModel

@api.route('/notes/')
def get_posts():


@api.route('/notes/<int:id>')
def get_note(id):
    note=NoteModel.query.get_or_404(id)
    return jsonify(note.to_json())
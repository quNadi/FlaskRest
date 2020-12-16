from app import db
from sqlalchemy import func
from flask import current_app,request,url_for
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class NoteModel(db.Model):
    __tablename__='notes'
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    content=db.Column(db.String(250))
    timestamp=db.Column(db.DateTime, server_default=func.now())



    def to_json(self):
        json_note={
            'url':url_for('api.get_note', id=self.id),
            'user_url':url_for('api.get_user',id=self.user_id)
            'content': self.content,
            'timestamp': self.timestamp
        }
        return json_note

    @staticmethod
    def from_json(json_note):
        content=json_note.get('content')
        if content is None or content =="":
            raise ValueError('note doesnt have content')
        return NoteModel(content=content)



class UserModel(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    notes=db.relationship('NoteModel',backref='user')

    def generate_confirm_token(self,exp=3600):
        s=Serializer(current_app.config['SECRET_KEY'],exp)
        return s.dumps({'confirm':self.id}).decode('utf-8')

    def confirm(self,token):
        s=Serializer(current_app.config['SECRET_KEY'])
        try:
            data=s.loads(token.encode('utf-8'))
        except:
            return False
        if data.get('confirm')!=self.id:
            return False
        self.confirmed=True
        db.session.add(self)
        return True

    def generate_reset_token(self,exp=3600):
        s=Serializer(current_app.config['SECRET_KEY'],exp)
        return s.dumps({'reset':self.id}).decode('utf-8')


    def to_json(self):
        json_user ={
            'url':url_for('api.get_user',id=self.id),
            'username':self.username,
            'notes_url':url_for('api.get_user_notes',id=self.id)
            'notes_count':self.notes.count()
        }
        return json_user

    def generate_auth_token(self,exp):
        s=Serializer(current_app.config['SECRET_KEY'],expires_in=exp)
        return s.dumps({'id':self.id}).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        s=Serializer(current_app.config['SECRET_KEY'])
        try:
            data=s.loads(token)
        except:
            return None
        return UserModel.query.get[data['id']]

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()
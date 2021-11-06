from . import db

class Pitch:
  __tablename__ = 'pitches'
  
  pitch_id = db.Column(db.Integer, primary_key=True)
  pitch_message = db.Column(db.String(1000))
  upvotes = db.Column(db.Integer())
  downvotes = db.Column(db.Integer())
  user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
  comment_id = db.Column(db.Integer, db.ForeignKey('comments.comment_id'))
  
  def __repr__(self):
    return f'Pitch {self.pitch_message}'
  
class User:
  __tablename__ = 'users'
  
  user_id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255))
  pitches = db.relationship('Pitch', backref='user', lazy="dynamic")
  comments = db.relationship('Comment', backref='user', lazy="dynamic")
  
  def __repr__(self):
    return f'User {self.username}'
  
class Comment:
  __tablename__ = 'comments'
  
  comment_id = db.Column(db.Integer, primary_key=True)
  comment_message =db.Column(db.String(250))
  user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
  pitches = db.relationship('Pitch', backref = 'comment', lazy ="dynamic")
  
  def __repr__(self):
    return f'Comment {self.comment_message}'
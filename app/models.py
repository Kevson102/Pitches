from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class Pitch(db.Model):
  __tablename__ = 'pitches'
  
  pitch_id = db.Column(db.Integer, primary_key=True)
  pitch_author = db.Column(db.String(255))
  pitch_title = db.Column(db.String(350))
  pitch_category = db.Column(db.String(255))
  pitch_message = db.Column(db.String(2000))
  date_published = db.Column(db.DateTime, default=datetime.utcnow)
  upvotes = db.Column(db.Integer)
  downvotes = db.Column(db.Integer)
  user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
  comments =   db.relationship('Comment', backref = 'pitch', lazy ="dynamic")
  
  def __repr__(self):
    return f'Pitch {self.pitch_message}'
  
class User(UserMixin ,db.Model):
  __tablename__ = 'users'
  
  user_id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255), unique = True, index = True)
  user_bio = db.Column(db.String(600))
  user_profile_pic_path = db.Column(db.String)
  pass_secure = db.Column(db.String(255))
  pitches = db.relationship('Pitch', backref='user', lazy="dynamic")
  comments = db.relationship('Comment', backref='user', lazy="dynamic")
  
  @property
  def password(self):
    raise AttributeError('You are not authorized to read password attribute')
  
  @password.setter
  def password(self, password):
    self.pass_secure = generate_password_hash(password)
    
  def verify_password(self, password):
    return check_password_hash(self.pass_secure, password)
  
  def __repr__(self):
    return f'User {self.username}'
  
class Comment(db.Model):
  __tablename__ = 'comments'
  
  comment_id = db.Column(db.Integer, primary_key=True)
  comment_message =db.Column(db.String(1000))
  date_posted = db.Column(db.DateTime, default=datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
  pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.pitch_id'))
  
  def __repr__(self):
    return f'Comment {self.comment_message}'
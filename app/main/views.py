from flask import render_template, redirect, url_for, abort, request
from . import main
from flask_login import login_required
from ..models import User, Pitch, Comment
from .forms import PitchForm, UserProfileUpdate, EnterCommentForm
from .. import db, photos

# Views
@main.route('/')

def index():
  '''
  Root page function that returns the index page and its content
  '''
  title = "Phoenix Pitches"
  pickup_lines = Pitch.query.filter_by(pitch_category = "pickup-lines").all()
  interview_pitch = Pitch.query.filter_by(pitch_category = "interview-pitch").all()
  product_pitch = Pitch.query.filter_by(pitch_category = "product-pitch").all()
  promotion_pitch = Pitch.query.filter_by(pitch_category = "promotion-pitch").all()
  
  return render_template('index.html', title = title, pickup_lines=pickup_lines, interview_pitch = interview_pitch, product_pitch=product_pitch, promotion_pitch=promotion_pitch)

@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by (username = uname).first()
  
  if user is None:
    abort(404)
    
  return render_template('profile/profile.html', user = user)

@main.route('/user/<uname>/update', methods = ['GET', 'POST'])
@login_required
def update_user_profile(uname):
  user = User.query.filter_by(username = uname).first()
  if user is None:
    abort(404)
    
  form = UserProfileUpdate()
  
  if form.validate_on_submit():
    user.user_bio = form.user_bio.data
    
    db.session.add(user)
    db.session.commit()
    
    return redirect(url_for('.profile', uname = user.username))
  return render_template('profile/update.html', form = form)

@main.route('/user/<uname>/update/profilepicture', methods = ['POST'])
def update_userprofile_pic(uname):
  user = User.query.filter_by(username = uname).first()
  
  if 'photo' in request.files:
    filename = photos.save(request.files['photo'])
    path = f'photos/{filename}'
    user.user_profile_pic_path = path
    db.session.commit()
    
  return redirect(url_for('main.profile', uname = uname))

@main.route('/pitch/new_pitch', methods = ['GET', 'POST'])
@login_required
def new_pitch():
  pitch_form = PitchForm()
  
  if pitch_form.validate_on_submit():
    pitch = Pitch(pitch_category = pitch_form.pitch_category.data, pitch_title = pitch_form.pitch_title.data, pitch_author = pitch_form.pitch_author.data, pitch_message = pitch_form.pitch_message.data)
    
    db.session.add(pitch)
    db.session.commit()
    
    return redirect(url_for('main.index'))
  
  return render_template('new_pitch.html', pitch_form = pitch_form)

@main.route('/pitch/comments', methods = ['GET', 'POST'])
@login_required
def comments():
  comment_form = EnterCommentForm()
  
  comments = Comment.query.all()
  
  if comment_form.validate_on_submit():
    
    new_comment = Comment(comment_message = comment_form.comment.data)
    new_comment.save_comment()
    
    return redirect(url_for('main.comments'))
  
  return render_template('comments.html', comment_form = comment_form, comments = comments)
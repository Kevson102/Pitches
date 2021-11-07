from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField ,TextAreaField, SubmitField
from wtforms.validators import Required

from app.models import Pitch

class PitchForm(FlaskForm):
  pitch_category = SelectField('Select Pitch Category', choices=[('pickup-lines', 'Pickup Lines'), ('interview-pitch', 'Interview Pitch'), ('product-pitch', 'Product Pitch'), ('promotion-pitch', 'Promotion Pitch')], validators=[Required()])
  pitch_title = StringField('Title of the pitch', validators=[Required()])
  pitch_author = StringField('Author', validators=[Required()])
  pitch_message = TextAreaField('One minute pitch...', validators=[Required()])
  submit = SubmitField('Submit')
  
class UserProfileUpdate(FlaskForm):
  user_bio = TextAreaField('Enter Your Bio info Here...', validators=[Required()])
  submit = SubmitField('Submit')
  
class EnterCommentForm(FlaskForm):
  comment = TextAreaField('Enter your comment here...', validators=[Required()])
  submit = SubmitField('Submit')
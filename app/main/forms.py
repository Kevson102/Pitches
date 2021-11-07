from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField ,TextAreaField, SubmitField
from wtforms.validators import Required

from app.models import Pitch

class PitchForm(FlaskForm):
  pitch_category = SelectField('Pitch category', choices=[('pickup-lines', 'Pickup Lines'), ('interview-pitch', 'Interview Pitch'), ('product-pitch', 'Product Pitch'), ('promotion-pitch', 'Promotion Pitch')], validators=[Required()])
  # StringField('Pitch category', validators=[Required()])
  pitch_message = StringField('One minute pitch', validators=[Required()])
  upvotes = IntegerField('Upvotes')
  downvotes = IntegerField('Downvotes')
  submit = SubmitField('Submit')
  
class User(FlaskForm):
  
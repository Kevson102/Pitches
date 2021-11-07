from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Email, EqualTo, ValidationError
from ..models import User

class RegistrationForm(FlaskForm):
  email = StringField('user123@gmail.com', validators=[Required(), Email()])
  username = StringField('Preferred Username', validators=[Required()])
  password = PasswordField('password', validators=[Required(), EqualTo('confirm_password', message="The password and Confirm password MUST match")])
  confirm_password = PasswordField('Confirm Password', validators=[Required()])
  submit = SubmitField('Sign Up')
  
  # Custom Validation for the registration email address
  def validate_email(self, data_field):
    if User.query.filter_by(email=data_field.data).first():
      raise ValidationError('An account with that email address exists')
    
  # Custom Validation for registration username
  def validate_username(self, data_field):
    if User.query.filter_by(username=data_field).first():
      raise ValidationError('That username is already taken. Please pick a different username')
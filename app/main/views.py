from flask import render_template, redirect, url_for, abort
from . import main
from flask_login import login_required
from ..models import User, Pitch, Comment
from .. import db

# Views
@main.route('/')
def index():
  '''
  Root page function that returns the index page and its content
  '''
  
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
  app = Flask(__name__)
  
  
  # Initializing flask extensions
  db.init_app(app)
from app import create_app, db
from flask_script import Manager, Server
from app.models import User, Comment, Pitch

# Creating app instances
# app = create_app('development')
app = create_app()

manager = Manager(app)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
  return dict(app = app, db=db, User = User, Comment = Comment, Pitch = Pitch)

if __name__ == '__main__':
  manager.run()
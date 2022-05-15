from datetime import datetime 
from flask_script import Manager, Server
from app import pitch_app,db
from app.models import User,Pitch,Comment
from  flask_migrate import Migrate, MigrateCommand




#app=pitch_app('development')
app=pitch_app('production')


migrate = Migrate(app,db)
manager =  Manager(app)
manager.add_command('server',Server(use_debugger=True))
manager.add_command('db',MigrateCommand)


@manager.shell
def  add_shell_context():
    return dict(db=db,app=app,User=User,Pitch=Pitch,Comment=Comment)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('Tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__== "__main__":
    manager.run()

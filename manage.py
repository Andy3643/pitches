import os
from datetime import datetime 
from app import pitch_app,db
from flask_script import Manager, Server
from app.models import User




app=pitch_app()
migrate = Migrate(app,db)
manager =  Manager(app)
manager.add_command('server',Server(use_debugger=True))
manager.add_command('db',MigrateCommand)


@manager.shell
def  add_shell_context():
    return {'db':db, 'User':User}

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('Tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__== "__main__":
    db.create_all()
    manager.run()

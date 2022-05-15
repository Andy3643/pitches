from flask import Flask
from config import config_options
import os
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail




bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)
mail = Mail()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def  pitch_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    # app.config.from_object(os.environ['APP_SETTINGS'])

    # initialize extensions
    login_manager.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)

     # configure UploadSet
    configure_uploads(app,photos)
    # registering main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    # registering auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    #heroku database
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://sxonldexavnrpe:0741ac59b66b35841fa6bc5f79d8e1c4e6dfa4c4e965416ed5d51290c3f0bd79@ec2-54-165-184-219.compute-1.amazonaws.com:5432/d9t415rp1vba1c'
    #postgresql-clean-92959
    return app
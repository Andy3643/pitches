import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):   
     DEBUG = False
     TESTING = False
    
     SECRET_KEY = 'secretkey1'
     SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
     UPLOADED_PHOTOS_DEST ='app/static/photos'

     MAIL_SERVER = 'smtp.gmail.com'
     MAIL_PORT = 465
     MAIL_USE_TLS = False
     MAIL_USE_SSL = True
     MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
     MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config_options = {
'test':TestingConfig
}
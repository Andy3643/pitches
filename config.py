import os
class Config():   
    
     SECRET_KEY ='secretkey1'
     SQLALCHEMY_DATABASE_URI='postgres://sxonldexavnrpe:0741ac59b66b35841fa6bc5f79d8e1c4e6dfa4c4e965416ed5d51290c3f0bd79@ec2-54-165-184-219.compute-1.amazonaws.com:5432/d9t415rp1vba1c'
    # SQLALCHEMY_DATABASE_URI='postgresql://moringa:pass123@localhost/pitches'
     UPLOADED_PHOTOS_DEST ='app/static/photos'

     MAIL_SERVER = 'smtp.gmail.com'
     MAIL_PORT = 465
     MAIL_USE_TLS = False
     MAIL_USE_SSL = True
     MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
     MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

class ProdConfig(Config):
    DEBUG = False


# class StagingConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True


class DevConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
   # SQLALCHEMY_DATABASE_URI='postgresql://moringa:pass123@localhost/pitches'
    SQLALCHEMY_DATABASE_URI='postgres://sxonldexavnrpe:0741ac59b66b35841fa6bc5f79d8e1c4e6dfa4c4e965416ed5d51290c3f0bd79@ec2-54-165-184-219.compute-1.amazonaws.com:5432/d9t415rp1vba1c'


class TestingConfig(Config):
    TESTING = True


config_options = {
'test':TestingConfig,
'development':DevConfig,
'production':ProdConfig
}
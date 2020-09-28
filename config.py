class Config():
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sandys:Stanford1*@localhost/blogs'
    SECRET_KEY = 'Stanford'

    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'dancan.oruko99@gmail.com'
    MAIL_PASSWORD = 'Stanford1*'

    

    @staticmethod   
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

config_options = {
    'development': DevConfig,
    'production' : ProdConfig,
    'test' : TestConfig
}
import os
class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY')

   
        #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")

class ProdConfig(Config):

    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass
    
    


class DevConfig(Config):
   
    DEBUG= True
    ENV = 'development'

config_options = {
    'production': ProdConfig,
    'development': DevConfig
}

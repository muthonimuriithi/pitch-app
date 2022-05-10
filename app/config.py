import os
class Config:
    

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')



class ProdConfig(Config):

    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    



class DevConfig(Config):

    DEBUG= True

config_options = {
    'production': ProdConfig,
    'development': DevConfig
}

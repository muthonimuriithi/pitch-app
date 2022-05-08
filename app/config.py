class Config:
    

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/watchlist'



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

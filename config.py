class Config:
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kevson:Antidolofinomonoligasta102@localhost/pitches'


class ProdConfig(Config):
  '''
  Production Configuration child class
  Args:
    Config: The parent configuration class with general configuration settings
  '''
  pass


class DevConfig(Config):
  '''
  Development configuration child class.
  Args:
    Config: The parent configuration class with general configuration settings
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kevson:Antidolofinomonoligasta102@localhost/watchlist'
  DEBUG = True
    
config_options = {
  'development': DevConfig,
  'production' : ProdConfig,
  # 'test' : TestConfig
}
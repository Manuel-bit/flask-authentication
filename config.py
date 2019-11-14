class Config:
  '''
  class that defines general configuarations
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://emmanuel:lilfranken@localhost/login'

class ProdConfig(Config):
  '''
  class that defines configuarations in production mode
  '''
  pass

class DevConfig(Config):
  '''
  class that defines configuarations in development stage
  '''
  DEBUG = True

config_options = {
  'production' : ProdConfig,
  'development'  : DevConfig

}

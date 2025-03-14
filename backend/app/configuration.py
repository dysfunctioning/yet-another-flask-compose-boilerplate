import os

class Base(object):
	APP_PORT = 9001
	DEBUG_SQL = True


class Development(Base):
	ENV = 'development'

class Testing(Base):
	ENV = 'testing'
	DEBUG_SQL = False


app_env = os.environ.get('APP_ENV', 'development')
config_class = {
	'development': Development,
    'testing': Testing,
}.get(app_env, Base)
config = config_class()

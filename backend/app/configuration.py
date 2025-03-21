import os

class Base(object):
	APP_PORT = 9001
	DEBUG_SQL = True
	DEFAULT_LOG_NAME = 'compose_backend'
	API_VERSION = 'v1'  # Change this for versioning
	EXTERNAL_API_ENABLED = False


class Development(Base):
	ENV = 'development'

class Testing(Base):
	ENV = 'testing'
	DEBUG_SQL = False
	EXTERNAL_API_ENABLED = True


app_env = os.environ.get('APP_ENV', 'development')
config_class = {
	'development': Development,
    'testing': Testing,
}.get(app_env, Base)
config = config_class()

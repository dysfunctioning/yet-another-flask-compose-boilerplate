# flake8: noqa
import os

# TODO: Move these values if needed!
user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
database = os.environ['POSTGRES_DB']
port = os.environ['POSTGRES_PORT']
if os.environ.get('ENV') == 'development':
	os.environ['DATABASE_CONNECTION_URI'] = f'postgresql+psycopg2://{user}:{password}@postgres:{port}/{database}'
else:
	os.environ['DATABASE_CONNECTION_URI'] = os.environ['DATABASE_URL'].replace("postgres://", "postgresql://", 1)  # Heroku fix

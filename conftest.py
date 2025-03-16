import os
import pytest
import subprocess
from sqlalchemy import create_engine, text
from sqlalchemy.engine.base import Connection
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from backend.db import base
from backend.db.base import Base  # Assuming your models are defined here
from backend.db.session import get_session

TEST_DB_NAME = 'test'
TEST_DB_SERVER_BASE_URL = 'postgresql+psycopg2://root:boilerplate1234@postgres:5432'


def pytest_addoption(parser):
    parser.addoption('--reset-db', action='store', default=False, help='Reset Test DB')


@pytest.fixture(scope='session')
def testdatabase(db_factory):
    _testdb = db_factory(base, TEST_DB_SERVER_BASE_URL)
    yield from _testdb


@pytest.fixture(scope='function')
def db(testdatabase):
    connection = testdatabase['connection']
    session = testdatabase['session']
    transaction = connection
    session.begin_nested()
    yield
    base.Session.remove()
    connection.rollback()


@pytest.fixture
def session(db):
    return get_session()


"""
Best to use a re-usable fixture for tests, but you can write individual DB tests using this guide:
https://docs.sqlalchemy.org/en/20/orm/session_transaction.html#joining-a-session-into-an-external-transaction-such-as-for-test-suites  # noqa
"""
@pytest.fixture(scope='session')
def db_factory(request):
    """
    Factoried from: https://gist.github.com/zzzeek/8443477
    """
    def _testdb_factory(base, database_url):
        def testdb():
            # Helper Function if extra hooks are needed
            def check_if_tables_exist(connection: Connection) -> bool:
                table_query = text("select count(*) from information_schema.tables where table_schema='public'")
                n_tables = list(connection.execute(table_query))[0][0]
                return n_tables > 0

            def recreate_db(db_name: str) -> bool:
                print('Dropping/creating test database')
                subprocess.run(f'dropdb {TEST_DB_NAME}', shell=True, check=True)
                subprocess.run(f'createdb {TEST_DB_NAME}', shell=True, check=True)
                return False

            # Helper function to check if the test db exists:
            def check_and_reset_existing_test_db(engine_url: str, reset_db: bool = True):
                # TODO: break this up
                temp_engine = create_engine(engine_url)
                temp_conn = temp_engine.connect()
                temp_conn.execute(text('commit'))  # end the already open transaction
                temp_query = text(
                   f'SELECT exists(SELECT 1 from pg_catalog.pg_database where datname = \'{TEST_DB_NAME}\')'
                )
                result_mapping = temp_conn.execute(temp_query).mappings().all()
                db_exists = False
                tables_exist = None

                if result_mapping and result_mapping[0]['exists']:
                    db_exists = True
                    print('Test database already exists')
                else:
                    # Make the test db
                    temp_conn.execute(text(f'create database {TEST_DB_NAME}'))
                    print(f'Creating test database: {TEST_DB_NAME}')
                    tables_exist = False

                temp_conn.close()

                if db_exists and reset_db:
                    tables_exist = recreate_db(TEST_DB_NAME)

                return db_exists, tables_exist

            reset_db = request.config.getoption("--reset-db") or False
            # TODO: move this to secrets/config and parametrize:
            TEST_ENGINE_URL = f'{TEST_DB_SERVER_BASE_URL}/{TEST_DB_NAME}'

            DEFAULT_DB_URL = TEST_ENGINE_URL.replace('/test', '/postgres')
            db_exists, tables_exist = check_and_reset_existing_test_db(DEFAULT_DB_URL, reset_db)

            base.initialize_database(TEST_ENGINE_URL)
            engine = base.engine
            connection = engine.connect()

            # Recreate sessions to bind to this new connection
            session_factory = sessionmaker(bind=connection)
            Session = scoped_session(session_factory)
            base.Session = Session

            Base.metadata.create_all(engine)
            print('Created all tables')

            session = Session

            db_params = {}
            db_params['engine'] = engine
            db_params['connection'] = connection
            db_params['session'] = session

            yield db_params
            connection.close()

        return testdb()
    return _testdb_factory

import pytest
from backend.db.models import User
from backend.db.repository import user as user_repo

pytestmark = pytest.mark.usefixtures('db', 'session')


@pytest.fixture
def user():
	return user_repo.create_user(name='Chris', email='foo123@bar.com')


def test_user_get(user):
	user_from_db = user_repo.get_user(user.id)
	assert user == user_from_db


def test_user_create():
	expected_user = User(name='Chris', email='test.create@foobar.com')
	user = user_repo.create_user(name='Chris', email='test.create@foobar.com')
	assert expected_user.name == user.name
	assert expected_user.email == user.email

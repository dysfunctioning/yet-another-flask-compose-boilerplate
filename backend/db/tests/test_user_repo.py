import pytest
from backend.db.models import User
from backend.db.repository import user as user_repo

pytestmark = pytest.mark.usefixtures('db', 'session')


def test_user_get():
	expected_user = user_repo.create_user(name='Chris', email='foo@bar.com')
	user = user_repo.get_user(expected_user.id)
	assert expected_user == user

def test_user_create():
	expected_user = User(name='Chris', email='test.create@foobar.com')
	user = user_repo.create_user(name='Chris', email='test.create@foobar.com')
	assert expected_user.name == user.name
	assert expected_user.email == user.email

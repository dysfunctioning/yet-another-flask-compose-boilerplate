from backend.db.models.user import User
from backend.db.session import get_session, session_commit
from backend.lib.logger import get_logger


logger = get_logger()

def get_user(id: int) -> User:
	session = get_session()
	user = session.get(User, id)
	return user


# validators would look nice as a decorator here:
def create_user(name: str, email: str) -> User:
	with session_commit() as session:
		user = User(name=name, email=email)
		session.add(user)

	return user


# and here:
def update_user(user: User, name: str, email: str):
	logger.info('TODO: lets update User')

def update_user_active_status(user: User, is_active: bool):
	logger.info('TODO: Add User Deactivation')

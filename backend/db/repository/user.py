from backend.db.models.user import User
from backend.db.session import get_session, session_commit


def get_user(id: int) -> User:
	session = get_session()
	user = session.get(User, id)
	return user


# validators would look nice as a decorator here:
def create_user(name: str, email: str) -> User:
	print('In repo, create_user:')
	with session_commit() as session:
		user = User(name=name, email=email)
		session.add(user)
		print(f'User id: {user.id}')

	return user


# and here:
def update_user(user: User, name: str, email: str):
	print('lets update')

def update_user_active_status(user: User, is_active: bool):
	print('lets make them deactivated')

from backend.lib.exceptions import BaseException


class DatabaseError(BaseException):
    pass


# Catch-all for any error involving a mutation to the DB
class MutationError(DatabaseError):
	pass

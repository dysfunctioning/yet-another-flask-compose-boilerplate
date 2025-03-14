class BaseException(Exception):
    def __init__(self, message=None, code=None, data=None):
        super().__init__(message)
        self.message = message
        self.code = code
        self.data = data

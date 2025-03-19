import base64
import secrets


# Helper function to generate keys:
def generate_secret_key(n_bytes: int) -> str:
	key = secrets.token_bytes(n_bytes)
	encoded = base64.b64encode(key).decode('utf-8')
	return encoded

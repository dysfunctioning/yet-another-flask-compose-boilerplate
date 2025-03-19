from flask import Blueprint  # quart works here as well

api = Blueprint('api', __name__)

from backend.api import user

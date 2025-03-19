from easydict import EasyDict
from flask import abort, jsonify

from backend.api import api
from backend.app.configuration import config
from backend.db.repository import user as user_repo
from backend.lib.logger import get_logger

logger = get_logger()


@api.route('/user/')
def get_user_heartbeat():
    return 'User Heartbeat Success!'



@api.route('/user/<int:id>')
def get_user(id):
    if not config.EXTERNAL_API_ENABLED:  # Change this in the app config file to enable
        logger.info(f'External API not enabled for: /user/<int:id>')
        abort(403)

    user = user_repo.get_user(id)
    # TODO: Add model serializer instead:
    return jsonify({'id': user.id, 'first_name': user.name, 'email': user.email})

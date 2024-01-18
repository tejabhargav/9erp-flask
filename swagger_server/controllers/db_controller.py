import connexion
import six

from swagger_server.models import (DbGetRequest, DbUpdateRequest)
from swagger_server.models.error import Error  # noqa: E501
from swagger_server import util

def db_get(body):  # noqa: E501
    """Get data from database

    Get data from database # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body = DbGetRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def db_update(body):  # noqa: E501
    """Update data in database

    Update data in database # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = DbUpdateRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


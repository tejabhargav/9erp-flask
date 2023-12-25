import connexion
import six

from swagger_server.models.bulk_update_request import BulkUpdateRequest  # noqa: E501
# from swagger_server.models.bulk_update_response import BulkUpdateResponse  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server import util


def bulk_update_student_post(body):  # noqa: E501
    """Bulk update students

    Update multiple students based on specified criteria. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: BulkUpdateResponse
    """
    if connexion.request.is_json:
        body = BulkUpdateRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

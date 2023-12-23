import connexion
import six

from swagger_server.models.approval_request import ApprovalRequest  # noqa: E501
from swagger_server.models.approval_response import ApprovalResponse  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server import util


def approvals_post(body):  # noqa: E501
    """Approve an entity

    Approve a student, employee, branch, or receipt. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ApprovalResponse
    """
    if connexion.request.is_json:
        body = ApprovalRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

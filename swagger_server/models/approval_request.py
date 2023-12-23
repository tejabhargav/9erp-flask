# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ApprovalRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, entity_id: str=None, entity_type: str=None, approval_status: str=None):  # noqa: E501
        """ApprovalRequest - a model defined in Swagger

        :param entity_id: The entity_id of this ApprovalRequest.  # noqa: E501
        :type entity_id: str
        :param entity_type: The entity_type of this ApprovalRequest.  # noqa: E501
        :type entity_type: str
        :param approval_status: The approval_status of this ApprovalRequest.  # noqa: E501
        :type approval_status: str
        """
        self.swagger_types = {
            'entity_id': str,
            'entity_type': str,
            'approval_status': str
        }

        self.attribute_map = {
            'entity_id': 'entity_id',
            'entity_type': 'entity_type',
            'approval_status': 'approval_status'
        }
        self._entity_id = entity_id
        self._entity_type = entity_type
        self._approval_status = approval_status

    @classmethod
    def from_dict(cls, dikt) -> 'ApprovalRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ApprovalRequest of this ApprovalRequest.  # noqa: E501
        :rtype: ApprovalRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entity_id(self) -> str:
        """Gets the entity_id of this ApprovalRequest.


        :return: The entity_id of this ApprovalRequest.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id: str):
        """Sets the entity_id of this ApprovalRequest.


        :param entity_id: The entity_id of this ApprovalRequest.
        :type entity_id: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self) -> str:
        """Gets the entity_type of this ApprovalRequest.


        :return: The entity_type of this ApprovalRequest.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type: str):
        """Sets the entity_type of this ApprovalRequest.


        :param entity_type: The entity_type of this ApprovalRequest.
        :type entity_type: str
        """
        allowed_values = ["student", "employee", "branch", "receipt"]  # noqa: E501
        if entity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `entity_type` ({0}), must be one of {1}"
                .format(entity_type, allowed_values)
            )

        self._entity_type = entity_type

    @property
    def approval_status(self) -> str:
        """Gets the approval_status of this ApprovalRequest.


        :return: The approval_status of this ApprovalRequest.
        :rtype: str
        """
        return self._approval_status

    @approval_status.setter
    def approval_status(self, approval_status: str):
        """Sets the approval_status of this ApprovalRequest.


        :param approval_status: The approval_status of this ApprovalRequest.
        :type approval_status: str
        """
        allowed_values = ["approved", "rejected"]  # noqa: E501
        if approval_status not in allowed_values:
            raise ValueError(
                "Invalid value for `approval_status` ({0}), must be one of {1}"
                .format(approval_status, allowed_values)
            )

        self._approval_status = approval_status
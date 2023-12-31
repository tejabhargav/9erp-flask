# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BulkUpdateResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, message: str=None, updated_count: int=None):  # noqa: E501
        """BulkUpdateResponse - a model defined in Swagger

        :param message: The message of this BulkUpdateResponse.  # noqa: E501
        :type message: str
        :param updated_count: The updated_count of this BulkUpdateResponse.  # noqa: E501
        :type updated_count: int
        """
        self.swagger_types = {
            'message': str,
            'updated_count': int
        }

        self.attribute_map = {
            'message': 'message',
            'updated_count': 'updatedCount'
        }
        self._message = message
        self._updated_count = updated_count

    @classmethod
    def from_dict(cls, dikt) -> 'BulkUpdateResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BulkUpdateResponse of this BulkUpdateResponse.  # noqa: E501
        :rtype: BulkUpdateResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self) -> str:
        """Gets the message of this BulkUpdateResponse.


        :return: The message of this BulkUpdateResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this BulkUpdateResponse.


        :param message: The message of this BulkUpdateResponse.
        :type message: str
        """

        self._message = message

    @property
    def updated_count(self) -> int:
        """Gets the updated_count of this BulkUpdateResponse.


        :return: The updated_count of this BulkUpdateResponse.
        :rtype: int
        """
        return self._updated_count

    @updated_count.setter
    def updated_count(self, updated_count: int):
        """Sets the updated_count of this BulkUpdateResponse.


        :param updated_count: The updated_count of this BulkUpdateResponse.
        :type updated_count: int
        """

        self._updated_count = updated_count

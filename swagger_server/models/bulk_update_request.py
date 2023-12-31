# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.bulk_update_request_filter_criteria import BulkUpdateRequestFilterCriteria  # noqa: F401,E501
from swagger_server.models.bulk_update_request_update_fields import BulkUpdateRequestUpdateFields  # noqa: F401,E501
from swagger_server import util


class BulkUpdateRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, filter_criteria: BulkUpdateRequestFilterCriteria=None, update_fields: BulkUpdateRequestUpdateFields=None):  # noqa: E501
        """BulkUpdateRequest - a model defined in Swagger

        :param filter_criteria: The filter_criteria of this BulkUpdateRequest.  # noqa: E501
        :type filter_criteria: BulkUpdateRequestFilterCriteria
        :param update_fields: The update_fields of this BulkUpdateRequest.  # noqa: E501
        :type update_fields: BulkUpdateRequestUpdateFields
        """
        self.swagger_types = {
            'filter_criteria': BulkUpdateRequestFilterCriteria,
            'update_fields': BulkUpdateRequestUpdateFields
        }

        self.attribute_map = {
            'filter_criteria': 'filterCriteria',
            'update_fields': 'updateFields'
        }
        self._filter_criteria = filter_criteria
        self._update_fields = update_fields

    @classmethod
    def from_dict(cls, dikt) -> 'BulkUpdateRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BulkUpdateRequest of this BulkUpdateRequest.  # noqa: E501
        :rtype: BulkUpdateRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def filter_criteria(self) -> BulkUpdateRequestFilterCriteria:
        """Gets the filter_criteria of this BulkUpdateRequest.


        :return: The filter_criteria of this BulkUpdateRequest.
        :rtype: BulkUpdateRequestFilterCriteria
        """
        return self._filter_criteria

    @filter_criteria.setter
    def filter_criteria(self, filter_criteria: BulkUpdateRequestFilterCriteria):
        """Sets the filter_criteria of this BulkUpdateRequest.


        :param filter_criteria: The filter_criteria of this BulkUpdateRequest.
        :type filter_criteria: BulkUpdateRequestFilterCriteria
        """

        self._filter_criteria = filter_criteria

    @property
    def update_fields(self) -> BulkUpdateRequestUpdateFields:
        """Gets the update_fields of this BulkUpdateRequest.


        :return: The update_fields of this BulkUpdateRequest.
        :rtype: BulkUpdateRequestUpdateFields
        """
        return self._update_fields

    @update_fields.setter
    def update_fields(self, update_fields: BulkUpdateRequestUpdateFields):
        """Sets the update_fields of this BulkUpdateRequest.


        :param update_fields: The update_fields of this BulkUpdateRequest.
        :type update_fields: BulkUpdateRequestUpdateFields
        """

        self._update_fields = update_fields

# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BulkUpdateRequestFilterCriteria(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, branch: str=None, batch: str=None, year_of_joining: str=None):  # noqa: E501
        """BulkUpdateRequestFilterCriteria - a model defined in Swagger

        :param branch: The branch of this BulkUpdateRequestFilterCriteria.  # noqa: E501
        :type branch: str
        :param batch: The batch of this BulkUpdateRequestFilterCriteria.  # noqa: E501
        :type batch: str
        :param year_of_joining: The year_of_joining of this BulkUpdateRequestFilterCriteria.  # noqa: E501
        :type year_of_joining: str
        """
        self.swagger_types = {
            'branch': str,
            'batch': str,
            'year_of_joining': str
        }

        self.attribute_map = {
            'branch': 'branch',
            'batch': 'batch',
            'year_of_joining': 'yearOfJoining'
        }
        self._branch = branch
        self._batch = batch
        self._year_of_joining = year_of_joining

    @classmethod
    def from_dict(cls, dikt) -> 'BulkUpdateRequestFilterCriteria':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BulkUpdateRequest_filterCriteria of this BulkUpdateRequestFilterCriteria.  # noqa: E501
        :rtype: BulkUpdateRequestFilterCriteria
        """
        return util.deserialize_model(dikt, cls)

    @property
    def branch(self) -> str:
        """Gets the branch of this BulkUpdateRequestFilterCriteria.

        Branch name for filtering  # noqa: E501

        :return: The branch of this BulkUpdateRequestFilterCriteria.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch: str):
        """Sets the branch of this BulkUpdateRequestFilterCriteria.

        Branch name for filtering  # noqa: E501

        :param branch: The branch of this BulkUpdateRequestFilterCriteria.
        :type branch: str
        """

        self._branch = branch

    @property
    def batch(self) -> str:
        """Gets the batch of this BulkUpdateRequestFilterCriteria.

        Batch name for filtering  # noqa: E501

        :return: The batch of this BulkUpdateRequestFilterCriteria.
        :rtype: str
        """
        return self._batch

    @batch.setter
    def batch(self, batch: str):
        """Sets the batch of this BulkUpdateRequestFilterCriteria.

        Batch name for filtering  # noqa: E501

        :param batch: The batch of this BulkUpdateRequestFilterCriteria.
        :type batch: str
        """

        self._batch = batch

    @property
    def year_of_joining(self) -> str:
        """Gets the year_of_joining of this BulkUpdateRequestFilterCriteria.

        Year of joining for filtering  # noqa: E501

        :return: The year_of_joining of this BulkUpdateRequestFilterCriteria.
        :rtype: str
        """
        return self._year_of_joining

    @year_of_joining.setter
    def year_of_joining(self, year_of_joining: str):
        """Sets the year_of_joining of this BulkUpdateRequestFilterCriteria.

        Year of joining for filtering  # noqa: E501

        :param year_of_joining: The year_of_joining of this BulkUpdateRequestFilterCriteria.
        :type year_of_joining: str
        """

        self._year_of_joining = year_of_joining
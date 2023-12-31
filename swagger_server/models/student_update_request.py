# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class StudentUpdateRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, application_number: str=None, date_of_joining: date=None, name: str=None, parent_name: str=None, primary_number: str=None, secondary_number: str=None, gender: str=None, batch: str=None, year_of_joining: str=None, section: str=None, fee_structure_for_one_year: float=None):  # noqa: E501
        """StudentUpdateRequest - a model defined in Swagger

        :param application_number: The application_number of this StudentUpdateRequest.  # noqa: E501
        :type application_number: str
        :param date_of_joining: The date_of_joining of this StudentUpdateRequest.  # noqa: E501
        :type date_of_joining: date
        :param name: The name of this StudentUpdateRequest.  # noqa: E501
        :type name: str
        :param parent_name: The parent_name of this StudentUpdateRequest.  # noqa: E501
        :type parent_name: str
        :param primary_number: The primary_number of this StudentUpdateRequest.  # noqa: E501
        :type primary_number: str
        :param secondary_number: The secondary_number of this StudentUpdateRequest.  # noqa: E501
        :type secondary_number: str
        :param gender: The gender of this StudentUpdateRequest.  # noqa: E501
        :type gender: str
        :param batch: The batch of this StudentUpdateRequest.  # noqa: E501
        :type batch: str
        :param year_of_joining: The year_of_joining of this StudentUpdateRequest.  # noqa: E501
        :type year_of_joining: str
        :param section: The section of this StudentUpdateRequest.  # noqa: E501
        :type section: str
        :param fee_structure_for_one_year: The fee_structure_for_one_year of this StudentUpdateRequest.  # noqa: E501
        :type fee_structure_for_one_year: float
        """
        self.swagger_types = {
            'application_number': str,
            'date_of_joining': date,
            'name': str,
            'parent_name': str,
            'primary_number': str,
            'secondary_number': str,
            'gender': str,
            'batch': str,
            'year_of_joining': str,
            'section': str,
            'fee_structure_for_one_year': float
        }

        self.attribute_map = {
            'application_number': 'applicationNumber',
            'date_of_joining': 'dateOfJoining',
            'name': 'name',
            'parent_name': 'parentName',
            'primary_number': 'primaryNumber',
            'secondary_number': 'secondaryNumber',
            'gender': 'gender',
            'batch': 'batch',
            'year_of_joining': 'yearOfJoining',
            'section': 'section',
            'fee_structure_for_one_year': 'feeStructureForOneYear'
        }
        self._application_number = application_number
        self._date_of_joining = date_of_joining
        self._name = name
        self._parent_name = parent_name
        self._primary_number = primary_number
        self._secondary_number = secondary_number
        self._gender = gender
        self._batch = batch
        self._year_of_joining = year_of_joining
        self._section = section
        self._fee_structure_for_one_year = fee_structure_for_one_year

    @classmethod
    def from_dict(cls, dikt) -> 'StudentUpdateRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StudentUpdateRequest of this StudentUpdateRequest.  # noqa: E501
        :rtype: StudentUpdateRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def application_number(self) -> str:
        """Gets the application_number of this StudentUpdateRequest.


        :return: The application_number of this StudentUpdateRequest.
        :rtype: str
        """
        return self._application_number

    @application_number.setter
    def application_number(self, application_number: str):
        """Sets the application_number of this StudentUpdateRequest.


        :param application_number: The application_number of this StudentUpdateRequest.
        :type application_number: str
        """

        self._application_number = application_number

    @property
    def date_of_joining(self) -> date:
        """Gets the date_of_joining of this StudentUpdateRequest.


        :return: The date_of_joining of this StudentUpdateRequest.
        :rtype: date
        """
        return self._date_of_joining

    @date_of_joining.setter
    def date_of_joining(self, date_of_joining: date):
        """Sets the date_of_joining of this StudentUpdateRequest.


        :param date_of_joining: The date_of_joining of this StudentUpdateRequest.
        :type date_of_joining: date
        """

        self._date_of_joining = date_of_joining

    @property
    def name(self) -> str:
        """Gets the name of this StudentUpdateRequest.


        :return: The name of this StudentUpdateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this StudentUpdateRequest.


        :param name: The name of this StudentUpdateRequest.
        :type name: str
        """

        self._name = name

    @property
    def parent_name(self) -> str:
        """Gets the parent_name of this StudentUpdateRequest.


        :return: The parent_name of this StudentUpdateRequest.
        :rtype: str
        """
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name: str):
        """Sets the parent_name of this StudentUpdateRequest.


        :param parent_name: The parent_name of this StudentUpdateRequest.
        :type parent_name: str
        """

        self._parent_name = parent_name

    @property
    def primary_number(self) -> str:
        """Gets the primary_number of this StudentUpdateRequest.


        :return: The primary_number of this StudentUpdateRequest.
        :rtype: str
        """
        return self._primary_number

    @primary_number.setter
    def primary_number(self, primary_number: str):
        """Sets the primary_number of this StudentUpdateRequest.


        :param primary_number: The primary_number of this StudentUpdateRequest.
        :type primary_number: str
        """

        self._primary_number = primary_number

    @property
    def secondary_number(self) -> str:
        """Gets the secondary_number of this StudentUpdateRequest.


        :return: The secondary_number of this StudentUpdateRequest.
        :rtype: str
        """
        return self._secondary_number

    @secondary_number.setter
    def secondary_number(self, secondary_number: str):
        """Sets the secondary_number of this StudentUpdateRequest.


        :param secondary_number: The secondary_number of this StudentUpdateRequest.
        :type secondary_number: str
        """

        self._secondary_number = secondary_number

    @property
    def gender(self) -> str:
        """Gets the gender of this StudentUpdateRequest.


        :return: The gender of this StudentUpdateRequest.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender: str):
        """Sets the gender of this StudentUpdateRequest.


        :param gender: The gender of this StudentUpdateRequest.
        :type gender: str
        """
        allowed_values = ["Male", "Female", "Other"]  # noqa: E501
        if gender not in allowed_values:
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"
                .format(gender, allowed_values)
            )

        self._gender = gender

    @property
    def batch(self) -> str:
        """Gets the batch of this StudentUpdateRequest.


        :return: The batch of this StudentUpdateRequest.
        :rtype: str
        """
        return self._batch

    @batch.setter
    def batch(self, batch: str):
        """Sets the batch of this StudentUpdateRequest.


        :param batch: The batch of this StudentUpdateRequest.
        :type batch: str
        """

        self._batch = batch

    @property
    def year_of_joining(self) -> str:
        """Gets the year_of_joining of this StudentUpdateRequest.


        :return: The year_of_joining of this StudentUpdateRequest.
        :rtype: str
        """
        return self._year_of_joining

    @year_of_joining.setter
    def year_of_joining(self, year_of_joining: str):
        """Sets the year_of_joining of this StudentUpdateRequest.


        :param year_of_joining: The year_of_joining of this StudentUpdateRequest.
        :type year_of_joining: str
        """

        self._year_of_joining = year_of_joining

    @property
    def section(self) -> str:
        """Gets the section of this StudentUpdateRequest.


        :return: The section of this StudentUpdateRequest.
        :rtype: str
        """
        return self._section

    @section.setter
    def section(self, section: str):
        """Sets the section of this StudentUpdateRequest.


        :param section: The section of this StudentUpdateRequest.
        :type section: str
        """

        self._section = section

    @property
    def fee_structure_for_one_year(self) -> float:
        """Gets the fee_structure_for_one_year of this StudentUpdateRequest.


        :return: The fee_structure_for_one_year of this StudentUpdateRequest.
        :rtype: float
        """
        return self._fee_structure_for_one_year

    @fee_structure_for_one_year.setter
    def fee_structure_for_one_year(self, fee_structure_for_one_year: float):
        """Sets the fee_structure_for_one_year of this StudentUpdateRequest.


        :param fee_structure_for_one_year: The fee_structure_for_one_year of this StudentUpdateRequest.
        :type fee_structure_for_one_year: float
        """

        self._fee_structure_for_one_year = fee_structure_for_one_year

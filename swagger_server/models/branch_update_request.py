# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BranchUpdateRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, branch_name: str=None, address: str=None, contact: str=None, courses_offered: List[str]=None, batches: List[str]=None, year_of_joining: List[str]=None, sections: List[str]=None, accounts: List[str]=None):  # noqa: E501
        """BranchUpdateRequest - a model defined in Swagger

        :param branch_name: The branch_name of this BranchUpdateRequest.  # noqa: E501
        :type branch_name: str
        :param address: The address of this BranchUpdateRequest.  # noqa: E501
        :type address: str
        :param contact: The contact of this BranchUpdateRequest.  # noqa: E501
        :type contact: str
        :param courses_offered: The courses_offered of this BranchUpdateRequest.  # noqa: E501
        :type courses_offered: List[str]
        :param batches: The batches of this BranchUpdateRequest.  # noqa: E501
        :type batches: List[str]
        :param year_of_joining: The year_of_joining of this BranchUpdateRequest.  # noqa: E501
        :type year_of_joining: List[str]
        :param sections: The sections of this BranchUpdateRequest.  # noqa: E501
        :type sections: List[str]
        :param accounts: The accounts of this BranchUpdateRequest.  # noqa: E501
        :type accounts: List[str]
        """
        self.swagger_types = {
            'branch_name': str,
            'address': str,
            'contact': str,
            'courses_offered': List[str],
            'batches': List[str],
            'year_of_joining': List[str],
            'sections': List[str],
            'accounts': List[str]
        }

        self.attribute_map = {
            'branch_name': 'branchName',
            'address': 'address',
            'contact': 'contact',
            'courses_offered': 'coursesOffered',
            'batches': 'batches',
            'year_of_joining': 'yearOfJoining',
            'sections': 'sections',
            'accounts': 'accounts'
        }
        self._branch_name = branch_name
        self._address = address
        self._contact = contact
        self._courses_offered = courses_offered
        self._batches = batches
        self._year_of_joining = year_of_joining
        self._sections = sections
        self._accounts = accounts

    @classmethod
    def from_dict(cls, dikt) -> 'BranchUpdateRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BranchUpdateRequest of this BranchUpdateRequest.  # noqa: E501
        :rtype: BranchUpdateRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def branch_name(self) -> str:
        """Gets the branch_name of this BranchUpdateRequest.


        :return: The branch_name of this BranchUpdateRequest.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name: str):
        """Sets the branch_name of this BranchUpdateRequest.


        :param branch_name: The branch_name of this BranchUpdateRequest.
        :type branch_name: str
        """

        self._branch_name = branch_name

    @property
    def address(self) -> str:
        """Gets the address of this BranchUpdateRequest.


        :return: The address of this BranchUpdateRequest.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """Sets the address of this BranchUpdateRequest.


        :param address: The address of this BranchUpdateRequest.
        :type address: str
        """

        self._address = address

    @property
    def contact(self) -> str:
        """Gets the contact of this BranchUpdateRequest.


        :return: The contact of this BranchUpdateRequest.
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact: str):
        """Sets the contact of this BranchUpdateRequest.


        :param contact: The contact of this BranchUpdateRequest.
        :type contact: str
        """

        self._contact = contact

    @property
    def courses_offered(self) -> List[str]:
        """Gets the courses_offered of this BranchUpdateRequest.


        :return: The courses_offered of this BranchUpdateRequest.
        :rtype: List[str]
        """
        return self._courses_offered

    @courses_offered.setter
    def courses_offered(self, courses_offered: List[str]):
        """Sets the courses_offered of this BranchUpdateRequest.


        :param courses_offered: The courses_offered of this BranchUpdateRequest.
        :type courses_offered: List[str]
        """

        self._courses_offered = courses_offered

    @property
    def batches(self) -> List[str]:
        """Gets the batches of this BranchUpdateRequest.


        :return: The batches of this BranchUpdateRequest.
        :rtype: List[str]
        """
        return self._batches

    @batches.setter
    def batches(self, batches: List[str]):
        """Sets the batches of this BranchUpdateRequest.


        :param batches: The batches of this BranchUpdateRequest.
        :type batches: List[str]
        """

        self._batches = batches

    @property
    def year_of_joining(self) -> List[str]:
        """Gets the year_of_joining of this BranchUpdateRequest.


        :return: The year_of_joining of this BranchUpdateRequest.
        :rtype: List[str]
        """
        return self._year_of_joining

    @year_of_joining.setter
    def year_of_joining(self, year_of_joining: List[str]):
        """Sets the year_of_joining of this BranchUpdateRequest.


        :param year_of_joining: The year_of_joining of this BranchUpdateRequest.
        :type year_of_joining: List[str]
        """

        self._year_of_joining = year_of_joining

    @property
    def sections(self) -> List[str]:
        """Gets the sections of this BranchUpdateRequest.


        :return: The sections of this BranchUpdateRequest.
        :rtype: List[str]
        """
        return self._sections

    @sections.setter
    def sections(self, sections: List[str]):
        """Sets the sections of this BranchUpdateRequest.


        :param sections: The sections of this BranchUpdateRequest.
        :type sections: List[str]
        """

        self._sections = sections

    @property
    def accounts(self) -> List[str]:
        """Gets the accounts of this BranchUpdateRequest.


        :return: The accounts of this BranchUpdateRequest.
        :rtype: List[str]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts: List[str]):
        """Sets the accounts of this BranchUpdateRequest.


        :param accounts: The accounts of this BranchUpdateRequest.
        :type accounts: List[str]
        """

        self._accounts = accounts

# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Employee(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, employee_id: str=None, name: str=None, role: str=None, branch: str=None, username: str=None, password: str=None):  # noqa: E501
        """Employee - a model defined in Swagger

        :param employee_id: The employee_id of this Employee.  # noqa: E501
        :type employee_id: str
        :param name: The name of this Employee.  # noqa: E501
        :type name: str
        :param role: The role of this Employee.  # noqa: E501
        :type role: str
        :param branch: The branch of this Employee.  # noqa: E501
        :type branch: str
        :param username: The username of this Employee.  # noqa: E501
        :type username: str
        :param password: The password of this Employee.  # noqa: E501
        :type password: str
        """
        self.swagger_types = {
            'employee_id': str,
            'name': str,
            'role': str,
            'branch': str,
            'username': str,
            'password': str
        }

        self.attribute_map = {
            'employee_id': 'employeeId',
            'name': 'name',
            'role': 'role',
            'branch': 'branch',
            'username': 'username',
            'password': 'password'
        }
        self._employee_id = employee_id
        self._name = name
        self._role = role
        self._branch = branch
        self._username = username
        self._password = password

    @classmethod
    def from_dict(cls, dikt) -> 'Employee':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Employee of this Employee.  # noqa: E501
        :rtype: Employee
        """
        return util.deserialize_model(dikt, cls)

    @property
    def employee_id(self) -> str:
        """Gets the employee_id of this Employee.


        :return: The employee_id of this Employee.
        :rtype: str
        """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id: str):
        """Sets the employee_id of this Employee.


        :param employee_id: The employee_id of this Employee.
        :type employee_id: str
        """

        self._employee_id = employee_id

    @property
    def name(self) -> str:
        """Gets the name of this Employee.


        :return: The name of this Employee.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Employee.


        :param name: The name of this Employee.
        :type name: str
        """

        self._name = name

    @property
    def role(self) -> str:
        """Gets the role of this Employee.


        :return: The role of this Employee.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role: str):
        """Sets the role of this Employee.


        :param role: The role of this Employee.
        :type role: str
        """

        self._role = role

    @property
    def branch(self) -> str:
        """Gets the branch of this Employee.


        :return: The branch of this Employee.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch: str):
        """Sets the branch of this Employee.


        :param branch: The branch of this Employee.
        :type branch: str
        """

        self._branch = branch

    @property
    def username(self) -> str:
        """Gets the username of this Employee.


        :return: The username of this Employee.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this Employee.


        :param username: The username of this Employee.
        :type username: str
        """

        self._username = username

    @property
    def password(self) -> str:
        """Gets the password of this Employee.


        :return: The password of this Employee.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this Employee.


        :param password: The password of this Employee.
        :type password: str
        """

        self._password = password

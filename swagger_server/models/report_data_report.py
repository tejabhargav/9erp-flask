# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ReportDataReport(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, student_name: str=None, roll_number: str=None, branch: str=None, batch: str=None, year: str=None, paid: float=None, mode_of_payment: str=None, date_of_payment: str=None, receipt_number: str=None, approval_status: str=None):  # noqa: E501
        """ReportDataReport - a model defined in Swagger

        :param student_name: The student_name of this ReportDataReport.  # noqa: E501
        :type student_name: str
        :param roll_number: The roll_number of this ReportDataReport.  # noqa: E501
        :type roll_number: str
        :param branch: The branch of this ReportDataReport.  # noqa: E501
        :type branch: str
        :param batch: The batch of this ReportDataReport.  # noqa: E501
        :type batch: str
        :param year: The year of this ReportDataReport.  # noqa: E501
        :type year: str
        :param paid: The paid of this ReportDataReport.  # noqa: E501
        :type paid: float
        :param mode_of_payment: The mode_of_payment of this ReportDataReport.  # noqa: E501
        :type mode_of_payment: str
        :param date_of_payment: The date_of_payment of this ReportDataReport.  # noqa: E501
        :type date_of_payment: str
        :param receipt_number: The receipt_number of this ReportDataReport.  # noqa: E501
        :type receipt_number: str
        :param approval_status: The approval_status of this ReportDataReport.  # noqa: E501
        :type approval_status: str
        """
        self.swagger_types = {
            'student_name': str,
            'roll_number': str,
            'branch': str,
            'batch': str,
            'year': str,
            'paid': float,
            'mode_of_payment': str,
            'date_of_payment': str,
            'receipt_number': str,
            'approval_status': str
        }

        self.attribute_map = {
            'student_name': 'studentName',
            'roll_number': 'rollNumber',
            'branch': 'branch',
            'batch': 'batch',
            'year': 'year',
            'paid': 'paid',
            'mode_of_payment': 'modeOfPayment',
            'date_of_payment': 'dateOfPayment',
            'receipt_number': 'receiptNumber',
            'approval_status': 'approvalStatus'
        }
        self._student_name = student_name
        self._roll_number = roll_number
        self._branch = branch
        self._batch = batch
        self._year = year
        self._paid = paid
        self._mode_of_payment = mode_of_payment
        self._date_of_payment = date_of_payment
        self._receipt_number = receipt_number
        self._approval_status = approval_status

    @classmethod
    def from_dict(cls, dikt) -> 'ReportDataReport':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ReportData_report of this ReportDataReport.  # noqa: E501
        :rtype: ReportDataReport
        """
        return util.deserialize_model(dikt, cls)

    @property
    def student_name(self) -> str:
        """Gets the student_name of this ReportDataReport.


        :return: The student_name of this ReportDataReport.
        :rtype: str
        """
        return self._student_name

    @student_name.setter
    def student_name(self, student_name: str):
        """Sets the student_name of this ReportDataReport.


        :param student_name: The student_name of this ReportDataReport.
        :type student_name: str
        """

        self._student_name = student_name

    @property
    def roll_number(self) -> str:
        """Gets the roll_number of this ReportDataReport.


        :return: The roll_number of this ReportDataReport.
        :rtype: str
        """
        return self._roll_number

    @roll_number.setter
    def roll_number(self, roll_number: str):
        """Sets the roll_number of this ReportDataReport.


        :param roll_number: The roll_number of this ReportDataReport.
        :type roll_number: str
        """

        self._roll_number = roll_number

    @property
    def branch(self) -> str:
        """Gets the branch of this ReportDataReport.


        :return: The branch of this ReportDataReport.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch: str):
        """Sets the branch of this ReportDataReport.


        :param branch: The branch of this ReportDataReport.
        :type branch: str
        """

        self._branch = branch

    @property
    def batch(self) -> str:
        """Gets the batch of this ReportDataReport.


        :return: The batch of this ReportDataReport.
        :rtype: str
        """
        return self._batch

    @batch.setter
    def batch(self, batch: str):
        """Sets the batch of this ReportDataReport.


        :param batch: The batch of this ReportDataReport.
        :type batch: str
        """

        self._batch = batch

    @property
    def year(self) -> str:
        """Gets the year of this ReportDataReport.


        :return: The year of this ReportDataReport.
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year: str):
        """Sets the year of this ReportDataReport.


        :param year: The year of this ReportDataReport.
        :type year: str
        """

        self._year = year

    @property
    def paid(self) -> float:
        """Gets the paid of this ReportDataReport.


        :return: The paid of this ReportDataReport.
        :rtype: float
        """
        return self._paid

    @paid.setter
    def paid(self, paid: float):
        """Sets the paid of this ReportDataReport.


        :param paid: The paid of this ReportDataReport.
        :type paid: float
        """

        self._paid = paid

    @property
    def mode_of_payment(self) -> str:
        """Gets the mode_of_payment of this ReportDataReport.


        :return: The mode_of_payment of this ReportDataReport.
        :rtype: str
        """
        return self._mode_of_payment

    @mode_of_payment.setter
    def mode_of_payment(self, mode_of_payment: str):
        """Sets the mode_of_payment of this ReportDataReport.


        :param mode_of_payment: The mode_of_payment of this ReportDataReport.
        :type mode_of_payment: str
        """

        self._mode_of_payment = mode_of_payment

    @property
    def date_of_payment(self) -> str:
        """Gets the date_of_payment of this ReportDataReport.


        :return: The date_of_payment of this ReportDataReport.
        :rtype: str
        """
        return self._date_of_payment

    @date_of_payment.setter
    def date_of_payment(self, date_of_payment: str):
        """Sets the date_of_payment of this ReportDataReport.


        :param date_of_payment: The date_of_payment of this ReportDataReport.
        :type date_of_payment: str
        """

        self._date_of_payment = date_of_payment

    @property
    def receipt_number(self) -> str:
        """Gets the receipt_number of this ReportDataReport.


        :return: The receipt_number of this ReportDataReport.
        :rtype: str
        """
        return self._receipt_number

    @receipt_number.setter
    def receipt_number(self, receipt_number: str):
        """Sets the receipt_number of this ReportDataReport.


        :param receipt_number: The receipt_number of this ReportDataReport.
        :type receipt_number: str
        """

        self._receipt_number = receipt_number

    @property
    def approval_status(self) -> str:
        """Gets the approval_status of this ReportDataReport.


        :return: The approval_status of this ReportDataReport.
        :rtype: str
        """
        return self._approval_status

    @approval_status.setter
    def approval_status(self, approval_status: str):
        """Sets the approval_status of this ReportDataReport.


        :param approval_status: The approval_status of this ReportDataReport.
        :type approval_status: str
        """

        self._approval_status = approval_status

# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SendEmailRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, subject: str=None, message: str=None):  # noqa: E501
        """SendEmailRequest - a model defined in Swagger

        :param subject: The subject of this SendEmailRequest.  # noqa: E501
        :type subject: str
        :param message: The message of this SendEmailRequest.  # noqa: E501
        :type message: str
        """
        self.swagger_types = {
            'subject': str,
            'message': str
        }

        self.attribute_map = {
            'subject': 'subject',
            'message': 'message'
        }
        self._subject = subject
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'SendEmailRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SendEmailRequest of this SendEmailRequest.  # noqa: E501
        :rtype: SendEmailRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def subject(self) -> str:
        """Gets the subject of this SendEmailRequest.


        :return: The subject of this SendEmailRequest.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject: str):
        """Sets the subject of this SendEmailRequest.


        :param subject: The subject of this SendEmailRequest.
        :type subject: str
        """

        self._subject = subject

    @property
    def message(self) -> str:
        """Gets the message of this SendEmailRequest.


        :return: The message of this SendEmailRequest.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this SendEmailRequest.


        :param message: The message of this SendEmailRequest.
        :type message: str
        """

        self._message = message
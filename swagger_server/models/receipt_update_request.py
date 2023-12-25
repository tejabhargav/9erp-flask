# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ReceiptUpdateRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, fee_amount: float=None, mode_of_payment: str=None, letter_head_on_receipt: str=None):  # noqa: E501
        """ReceiptUpdateRequest - a model defined in Swagger

        :param fee_amount: The fee_amount of this ReceiptUpdateRequest.  # noqa: E501
        :type fee_amount: float
        :param mode_of_payment: The mode_of_payment of this ReceiptUpdateRequest.  # noqa: E501
        :type mode_of_payment: str
        :param letter_head_on_receipt: The letter_head_on_receipt of this ReceiptUpdateRequest.  # noqa: E501
        :type letter_head_on_receipt: str
        """
        self.swagger_types = {
            'fee_amount': float,
            'mode_of_payment': str,
            'letter_head_on_receipt': str
        }

        self.attribute_map = {
            'fee_amount': 'feeAmount',
            'mode_of_payment': 'modeOfPayment',
            'letter_head_on_receipt': 'letterHeadOnReceipt'
        }
        self._fee_amount = fee_amount
        self._mode_of_payment = mode_of_payment
        self._letter_head_on_receipt = letter_head_on_receipt

    @classmethod
    def from_dict(cls, dikt) -> 'ReceiptUpdateRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ReceiptUpdateRequest of this ReceiptUpdateRequest.  # noqa: E501
        :rtype: ReceiptUpdateRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def fee_amount(self) -> float:
        """Gets the fee_amount of this ReceiptUpdateRequest.


        :return: The fee_amount of this ReceiptUpdateRequest.
        :rtype: float
        """
        return self._fee_amount

    @fee_amount.setter
    def fee_amount(self, fee_amount: float):
        """Sets the fee_amount of this ReceiptUpdateRequest.


        :param fee_amount: The fee_amount of this ReceiptUpdateRequest.
        :type fee_amount: float
        """

        self._fee_amount = fee_amount

    @property
    def mode_of_payment(self) -> str:
        """Gets the mode_of_payment of this ReceiptUpdateRequest.


        :return: The mode_of_payment of this ReceiptUpdateRequest.
        :rtype: str
        """
        return self._mode_of_payment

    @mode_of_payment.setter
    def mode_of_payment(self, mode_of_payment: str):
        """Sets the mode_of_payment of this ReceiptUpdateRequest.


        :param mode_of_payment: The mode_of_payment of this ReceiptUpdateRequest.
        :type mode_of_payment: str
        """
        allowed_values = ["Cash", "Card", "Cheque", "Bank Transfer/UPI", "Concession"]  # noqa: E501
        if mode_of_payment not in allowed_values:
            raise ValueError(
                "Invalid value for `mode_of_payment` ({0}), must be one of {1}"
                .format(mode_of_payment, allowed_values)
            )

        self._mode_of_payment = mode_of_payment

    @property
    def letter_head_on_receipt(self) -> str:
        """Gets the letter_head_on_receipt of this ReceiptUpdateRequest.


        :return: The letter_head_on_receipt of this ReceiptUpdateRequest.
        :rtype: str
        """
        return self._letter_head_on_receipt

    @letter_head_on_receipt.setter
    def letter_head_on_receipt(self, letter_head_on_receipt: str):
        """Sets the letter_head_on_receipt of this ReceiptUpdateRequest.


        :param letter_head_on_receipt: The letter_head_on_receipt of this ReceiptUpdateRequest.
        :type letter_head_on_receipt: str
        """

        self._letter_head_on_receipt = letter_head_on_receipt

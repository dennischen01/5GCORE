# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.sm_context_create_error import SmContextCreateError  # noqa: F401,E501
from swagger_server import util


class InlineResponse400(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, json_data=None, binary_data_n1_sm_message=None):  # noqa: E501
        """InlineResponse400 - a model defined in Swagger

        :param json_data: The json_data of this InlineResponse400.  # noqa: E501
        :type json_data: SmContextCreateError
        :param binary_data_n1_sm_message: The binary_data_n1_sm_message of this InlineResponse400.  # noqa: E501
        :type binary_data_n1_sm_message: str
        """
        self.swagger_types = {
            'json_data': SmContextCreateError,
            'binary_data_n1_sm_message': str
        }

        self.attribute_map = {
            'json_data': 'jsonData',
            'binary_data_n1_sm_message': 'binaryDataN1SmMessage'
        }
        self._json_data = json_data
        self._binary_data_n1_sm_message = binary_data_n1_sm_message

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_400 of this InlineResponse400.  # noqa: E501
        :rtype: InlineResponse400
        """
        return util.deserialize_model(dikt, cls)

    @property
    def json_data(self):
        """Gets the json_data of this InlineResponse400.


        :return: The json_data of this InlineResponse400.
        :rtype: SmContextCreateError
        """
        return self._json_data

    @json_data.setter
    def json_data(self, json_data):
        """Sets the json_data of this InlineResponse400.


        :param json_data: The json_data of this InlineResponse400.
        :type json_data: SmContextCreateError
        """

        self._json_data = json_data

    @property
    def binary_data_n1_sm_message(self):
        """Gets the binary_data_n1_sm_message of this InlineResponse400.


        :return: The binary_data_n1_sm_message of this InlineResponse400.
        :rtype: str
        """
        return self._binary_data_n1_sm_message

    @binary_data_n1_sm_message.setter
    def binary_data_n1_sm_message(self, binary_data_n1_sm_message):
        """Sets the binary_data_n1_sm_message of this InlineResponse400.


        :param binary_data_n1_sm_message: The binary_data_n1_sm_message of this InlineResponse400.
        :type binary_data_n1_sm_message: str
        """

        self._binary_data_n1_sm_message = binary_data_n1_sm_message
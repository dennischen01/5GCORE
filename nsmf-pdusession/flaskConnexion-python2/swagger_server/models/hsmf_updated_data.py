# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.ref_to_binary_data import RefToBinaryData  # noqa: F401,E501
from swagger_server import util


class HsmfUpdatedData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, n1_sm_info_to_ue=None):  # noqa: E501
        """HsmfUpdatedData - a model defined in Swagger

        :param n1_sm_info_to_ue: The n1_sm_info_to_ue of this HsmfUpdatedData.  # noqa: E501
        :type n1_sm_info_to_ue: RefToBinaryData
        """
        self.swagger_types = {
            'n1_sm_info_to_ue': RefToBinaryData
        }

        self.attribute_map = {
            'n1_sm_info_to_ue': 'n1SmInfoToUe'
        }
        self._n1_sm_info_to_ue = n1_sm_info_to_ue

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HsmfUpdatedData of this HsmfUpdatedData.  # noqa: E501
        :rtype: HsmfUpdatedData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def n1_sm_info_to_ue(self):
        """Gets the n1_sm_info_to_ue of this HsmfUpdatedData.


        :return: The n1_sm_info_to_ue of this HsmfUpdatedData.
        :rtype: RefToBinaryData
        """
        return self._n1_sm_info_to_ue

    @n1_sm_info_to_ue.setter
    def n1_sm_info_to_ue(self, n1_sm_info_to_ue):
        """Sets the n1_sm_info_to_ue of this HsmfUpdatedData.


        :param n1_sm_info_to_ue: The n1_sm_info_to_ue of this HsmfUpdatedData.
        :type n1_sm_info_to_ue: RefToBinaryData
        """

        self._n1_sm_info_to_ue = n1_sm_info_to_ue
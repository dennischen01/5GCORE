# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.global_ran_node_id import GlobalRanNodeId  # noqa: F401,E501
from swagger_server.models.ncgi import Ncgi  # noqa: F401,E501
from swagger_server.models.tai import Tai  # noqa: F401,E501
import re  # noqa: F401,E501
from swagger_server import util


class NrLocation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, tai=None, ncgi=None, age_of_location_information=None, ue_location_timestamp=None, geographical_information=None, geodetic_information=None, global_gnb_id=None):  # noqa: E501
        """NrLocation - a model defined in Swagger

        :param tai: The tai of this NrLocation.  # noqa: E501
        :type tai: Tai
        :param ncgi: The ncgi of this NrLocation.  # noqa: E501
        :type ncgi: Ncgi
        :param age_of_location_information: The age_of_location_information of this NrLocation.  # noqa: E501
        :type age_of_location_information: int
        :param ue_location_timestamp: The ue_location_timestamp of this NrLocation.  # noqa: E501
        :type ue_location_timestamp: datetime
        :param geographical_information: The geographical_information of this NrLocation.  # noqa: E501
        :type geographical_information: str
        :param geodetic_information: The geodetic_information of this NrLocation.  # noqa: E501
        :type geodetic_information: str
        :param global_gnb_id: The global_gnb_id of this NrLocation.  # noqa: E501
        :type global_gnb_id: GlobalRanNodeId
        """
        self.swagger_types = {
            'tai': Tai,
            'ncgi': Ncgi,
            'age_of_location_information': int,
            'ue_location_timestamp': datetime,
            'geographical_information': str,
            'geodetic_information': str,
            'global_gnb_id': GlobalRanNodeId
        }

        self.attribute_map = {
            'tai': 'tai',
            'ncgi': 'ncgi',
            'age_of_location_information': 'ageOfLocationInformation',
            'ue_location_timestamp': 'ueLocationTimestamp',
            'geographical_information': 'geographicalInformation',
            'geodetic_information': 'geodeticInformation',
            'global_gnb_id': 'globalGnbId'
        }
        self._tai = tai
        self._ncgi = ncgi
        self._age_of_location_information = age_of_location_information
        self._ue_location_timestamp = ue_location_timestamp
        self._geographical_information = geographical_information
        self._geodetic_information = geodetic_information
        self._global_gnb_id = global_gnb_id

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NrLocation of this NrLocation.  # noqa: E501
        :rtype: NrLocation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tai(self):
        """Gets the tai of this NrLocation.


        :return: The tai of this NrLocation.
        :rtype: Tai
        """
        return self._tai

    @tai.setter
    def tai(self, tai):
        """Sets the tai of this NrLocation.


        :param tai: The tai of this NrLocation.
        :type tai: Tai
        """
        if tai is None:
            raise ValueError("Invalid value for `tai`, must not be `None`")  # noqa: E501

        self._tai = tai

    @property
    def ncgi(self):
        """Gets the ncgi of this NrLocation.


        :return: The ncgi of this NrLocation.
        :rtype: Ncgi
        """
        return self._ncgi

    @ncgi.setter
    def ncgi(self, ncgi):
        """Sets the ncgi of this NrLocation.


        :param ncgi: The ncgi of this NrLocation.
        :type ncgi: Ncgi
        """
        if ncgi is None:
            raise ValueError("Invalid value for `ncgi`, must not be `None`")  # noqa: E501

        self._ncgi = ncgi

    @property
    def age_of_location_information(self):
        """Gets the age_of_location_information of this NrLocation.


        :return: The age_of_location_information of this NrLocation.
        :rtype: int
        """
        return self._age_of_location_information

    @age_of_location_information.setter
    def age_of_location_information(self, age_of_location_information):
        """Sets the age_of_location_information of this NrLocation.


        :param age_of_location_information: The age_of_location_information of this NrLocation.
        :type age_of_location_information: int
        """

        self._age_of_location_information = age_of_location_information

    @property
    def ue_location_timestamp(self):
        """Gets the ue_location_timestamp of this NrLocation.


        :return: The ue_location_timestamp of this NrLocation.
        :rtype: datetime
        """
        return self._ue_location_timestamp

    @ue_location_timestamp.setter
    def ue_location_timestamp(self, ue_location_timestamp):
        """Sets the ue_location_timestamp of this NrLocation.


        :param ue_location_timestamp: The ue_location_timestamp of this NrLocation.
        :type ue_location_timestamp: datetime
        """

        self._ue_location_timestamp = ue_location_timestamp

    @property
    def geographical_information(self):
        """Gets the geographical_information of this NrLocation.


        :return: The geographical_information of this NrLocation.
        :rtype: str
        """
        return self._geographical_information

    @geographical_information.setter
    def geographical_information(self, geographical_information):
        """Sets the geographical_information of this NrLocation.


        :param geographical_information: The geographical_information of this NrLocation.
        :type geographical_information: str
        """

        self._geographical_information = geographical_information

    @property
    def geodetic_information(self):
        """Gets the geodetic_information of this NrLocation.


        :return: The geodetic_information of this NrLocation.
        :rtype: str
        """
        return self._geodetic_information

    @geodetic_information.setter
    def geodetic_information(self, geodetic_information):
        """Sets the geodetic_information of this NrLocation.


        :param geodetic_information: The geodetic_information of this NrLocation.
        :type geodetic_information: str
        """

        self._geodetic_information = geodetic_information

    @property
    def global_gnb_id(self):
        """Gets the global_gnb_id of this NrLocation.


        :return: The global_gnb_id of this NrLocation.
        :rtype: GlobalRanNodeId
        """
        return self._global_gnb_id

    @global_gnb_id.setter
    def global_gnb_id(self, global_gnb_id):
        """Sets the global_gnb_id of this NrLocation.


        :param global_gnb_id: The global_gnb_id of this NrLocation.
        :type global_gnb_id: GlobalRanNodeId
        """

        self._global_gnb_id = global_gnb_id
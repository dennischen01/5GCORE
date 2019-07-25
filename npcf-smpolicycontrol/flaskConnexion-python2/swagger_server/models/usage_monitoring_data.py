# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.date_time_rm import DateTimeRm  # noqa: F401,E501
from swagger_server.models.duration_sec_rm import DurationSecRm  # noqa: F401,E501
from swagger_server.models.volume_rm import VolumeRm  # noqa: F401,E501
from swagger_server import util


class UsageMonitoringData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, um_id=None, volume_threshold=None, volume_threshold_uplink=None, volume_threshold_downlink=None, time_threshold=None, monitoring_time=None, next_vol_threshold=None, next_vol_threshold_uplink=None, next_vol_threshold_downlink=None, next_time_threshold=None, inactivity_time=None, ex_usage_pcc_rule_ids=None):  # noqa: E501
        """UsageMonitoringData - a model defined in Swagger

        :param um_id: The um_id of this UsageMonitoringData.  # noqa: E501
        :type um_id: str
        :param volume_threshold: The volume_threshold of this UsageMonitoringData.  # noqa: E501
        :type volume_threshold: VolumeRm
        :param volume_threshold_uplink: The volume_threshold_uplink of this UsageMonitoringData.  # noqa: E501
        :type volume_threshold_uplink: VolumeRm
        :param volume_threshold_downlink: The volume_threshold_downlink of this UsageMonitoringData.  # noqa: E501
        :type volume_threshold_downlink: VolumeRm
        :param time_threshold: The time_threshold of this UsageMonitoringData.  # noqa: E501
        :type time_threshold: DurationSecRm
        :param monitoring_time: The monitoring_time of this UsageMonitoringData.  # noqa: E501
        :type monitoring_time: DateTimeRm
        :param next_vol_threshold: The next_vol_threshold of this UsageMonitoringData.  # noqa: E501
        :type next_vol_threshold: VolumeRm
        :param next_vol_threshold_uplink: The next_vol_threshold_uplink of this UsageMonitoringData.  # noqa: E501
        :type next_vol_threshold_uplink: VolumeRm
        :param next_vol_threshold_downlink: The next_vol_threshold_downlink of this UsageMonitoringData.  # noqa: E501
        :type next_vol_threshold_downlink: VolumeRm
        :param next_time_threshold: The next_time_threshold of this UsageMonitoringData.  # noqa: E501
        :type next_time_threshold: DurationSecRm
        :param inactivity_time: The inactivity_time of this UsageMonitoringData.  # noqa: E501
        :type inactivity_time: DurationSecRm
        :param ex_usage_pcc_rule_ids: The ex_usage_pcc_rule_ids of this UsageMonitoringData.  # noqa: E501
        :type ex_usage_pcc_rule_ids: List[str]
        """
        self.swagger_types = {
            'um_id': str,
            'volume_threshold': VolumeRm,
            'volume_threshold_uplink': VolumeRm,
            'volume_threshold_downlink': VolumeRm,
            'time_threshold': DurationSecRm,
            'monitoring_time': DateTimeRm,
            'next_vol_threshold': VolumeRm,
            'next_vol_threshold_uplink': VolumeRm,
            'next_vol_threshold_downlink': VolumeRm,
            'next_time_threshold': DurationSecRm,
            'inactivity_time': DurationSecRm,
            'ex_usage_pcc_rule_ids': List[str]
        }

        self.attribute_map = {
            'um_id': 'umId',
            'volume_threshold': 'volumeThreshold',
            'volume_threshold_uplink': 'volumeThresholdUplink',
            'volume_threshold_downlink': 'volumeThresholdDownlink',
            'time_threshold': 'timeThreshold',
            'monitoring_time': 'monitoringTime',
            'next_vol_threshold': 'nextVolThreshold',
            'next_vol_threshold_uplink': 'nextVolThresholdUplink',
            'next_vol_threshold_downlink': 'nextVolThresholdDownlink',
            'next_time_threshold': 'nextTimeThreshold',
            'inactivity_time': 'inactivityTime',
            'ex_usage_pcc_rule_ids': 'exUsagePccRuleIds'
        }
        self._um_id = um_id
        self._volume_threshold = volume_threshold
        self._volume_threshold_uplink = volume_threshold_uplink
        self._volume_threshold_downlink = volume_threshold_downlink
        self._time_threshold = time_threshold
        self._monitoring_time = monitoring_time
        self._next_vol_threshold = next_vol_threshold
        self._next_vol_threshold_uplink = next_vol_threshold_uplink
        self._next_vol_threshold_downlink = next_vol_threshold_downlink
        self._next_time_threshold = next_time_threshold
        self._inactivity_time = inactivity_time
        self._ex_usage_pcc_rule_ids = ex_usage_pcc_rule_ids

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UsageMonitoringData of this UsageMonitoringData.  # noqa: E501
        :rtype: UsageMonitoringData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def um_id(self):
        """Gets the um_id of this UsageMonitoringData.

        Univocally identifies the usage monitoring policy data within a PDU session.  # noqa: E501

        :return: The um_id of this UsageMonitoringData.
        :rtype: str
        """
        return self._um_id

    @um_id.setter
    def um_id(self, um_id):
        """Sets the um_id of this UsageMonitoringData.

        Univocally identifies the usage monitoring policy data within a PDU session.  # noqa: E501

        :param um_id: The um_id of this UsageMonitoringData.
        :type um_id: str
        """
        if um_id is None:
            raise ValueError("Invalid value for `um_id`, must not be `None`")  # noqa: E501

        self._um_id = um_id

    @property
    def volume_threshold(self):
        """Gets the volume_threshold of this UsageMonitoringData.


        :return: The volume_threshold of this UsageMonitoringData.
        :rtype: VolumeRm
        """
        return self._volume_threshold

    @volume_threshold.setter
    def volume_threshold(self, volume_threshold):
        """Sets the volume_threshold of this UsageMonitoringData.


        :param volume_threshold: The volume_threshold of this UsageMonitoringData.
        :type volume_threshold: VolumeRm
        """

        self._volume_threshold = volume_threshold

    @property
    def volume_threshold_uplink(self):
        """Gets the volume_threshold_uplink of this UsageMonitoringData.


        :return: The volume_threshold_uplink of this UsageMonitoringData.
        :rtype: VolumeRm
        """
        return self._volume_threshold_uplink

    @volume_threshold_uplink.setter
    def volume_threshold_uplink(self, volume_threshold_uplink):
        """Sets the volume_threshold_uplink of this UsageMonitoringData.


        :param volume_threshold_uplink: The volume_threshold_uplink of this UsageMonitoringData.
        :type volume_threshold_uplink: VolumeRm
        """

        self._volume_threshold_uplink = volume_threshold_uplink

    @property
    def volume_threshold_downlink(self):
        """Gets the volume_threshold_downlink of this UsageMonitoringData.


        :return: The volume_threshold_downlink of this UsageMonitoringData.
        :rtype: VolumeRm
        """
        return self._volume_threshold_downlink

    @volume_threshold_downlink.setter
    def volume_threshold_downlink(self, volume_threshold_downlink):
        """Sets the volume_threshold_downlink of this UsageMonitoringData.


        :param volume_threshold_downlink: The volume_threshold_downlink of this UsageMonitoringData.
        :type volume_threshold_downlink: VolumeRm
        """

        self._volume_threshold_downlink = volume_threshold_downlink

    @property
    def time_threshold(self):
        """Gets the time_threshold of this UsageMonitoringData.


        :return: The time_threshold of this UsageMonitoringData.
        :rtype: DurationSecRm
        """
        return self._time_threshold

    @time_threshold.setter
    def time_threshold(self, time_threshold):
        """Sets the time_threshold of this UsageMonitoringData.


        :param time_threshold: The time_threshold of this UsageMonitoringData.
        :type time_threshold: DurationSecRm
        """

        self._time_threshold = time_threshold

    @property
    def monitoring_time(self):
        """Gets the monitoring_time of this UsageMonitoringData.


        :return: The monitoring_time of this UsageMonitoringData.
        :rtype: DateTimeRm
        """
        return self._monitoring_time

    @monitoring_time.setter
    def monitoring_time(self, monitoring_time):
        """Sets the monitoring_time of this UsageMonitoringData.


        :param monitoring_time: The monitoring_time of this UsageMonitoringData.
        :type monitoring_time: DateTimeRm
        """

        self._monitoring_time = monitoring_time

    @property
    def next_vol_threshold(self):
        """Gets the next_vol_threshold of this UsageMonitoringData.


        :return: The next_vol_threshold of this UsageMonitoringData.
        :rtype: VolumeRm
        """
        return self._next_vol_threshold

    @next_vol_threshold.setter
    def next_vol_threshold(self, next_vol_threshold):
        """Sets the next_vol_threshold of this UsageMonitoringData.


        :param next_vol_threshold: The next_vol_threshold of this UsageMonitoringData.
        :type next_vol_threshold: VolumeRm
        """

        self._next_vol_threshold = next_vol_threshold

    @property
    def next_vol_threshold_uplink(self):
        """Gets the next_vol_threshold_uplink of this UsageMonitoringData.


        :return: The next_vol_threshold_uplink of this UsageMonitoringData.
        :rtype: VolumeRm
        """
        return self._next_vol_threshold_uplink

    @next_vol_threshold_uplink.setter
    def next_vol_threshold_uplink(self, next_vol_threshold_uplink):
        """Sets the next_vol_threshold_uplink of this UsageMonitoringData.


        :param next_vol_threshold_uplink: The next_vol_threshold_uplink of this UsageMonitoringData.
        :type next_vol_threshold_uplink: VolumeRm
        """

        self._next_vol_threshold_uplink = next_vol_threshold_uplink

    @property
    def next_vol_threshold_downlink(self):
        """Gets the next_vol_threshold_downlink of this UsageMonitoringData.


        :return: The next_vol_threshold_downlink of this UsageMonitoringData.
        :rtype: VolumeRm
        """
        return self._next_vol_threshold_downlink

    @next_vol_threshold_downlink.setter
    def next_vol_threshold_downlink(self, next_vol_threshold_downlink):
        """Sets the next_vol_threshold_downlink of this UsageMonitoringData.


        :param next_vol_threshold_downlink: The next_vol_threshold_downlink of this UsageMonitoringData.
        :type next_vol_threshold_downlink: VolumeRm
        """

        self._next_vol_threshold_downlink = next_vol_threshold_downlink

    @property
    def next_time_threshold(self):
        """Gets the next_time_threshold of this UsageMonitoringData.


        :return: The next_time_threshold of this UsageMonitoringData.
        :rtype: DurationSecRm
        """
        return self._next_time_threshold

    @next_time_threshold.setter
    def next_time_threshold(self, next_time_threshold):
        """Sets the next_time_threshold of this UsageMonitoringData.


        :param next_time_threshold: The next_time_threshold of this UsageMonitoringData.
        :type next_time_threshold: DurationSecRm
        """

        self._next_time_threshold = next_time_threshold

    @property
    def inactivity_time(self):
        """Gets the inactivity_time of this UsageMonitoringData.


        :return: The inactivity_time of this UsageMonitoringData.
        :rtype: DurationSecRm
        """
        return self._inactivity_time

    @inactivity_time.setter
    def inactivity_time(self, inactivity_time):
        """Sets the inactivity_time of this UsageMonitoringData.


        :param inactivity_time: The inactivity_time of this UsageMonitoringData.
        :type inactivity_time: DurationSecRm
        """

        self._inactivity_time = inactivity_time

    @property
    def ex_usage_pcc_rule_ids(self):
        """Gets the ex_usage_pcc_rule_ids of this UsageMonitoringData.

        Contains the PCC rule identifier(s) which corresponding service data flow(s) shall be excluded from PDU Session usage monitoring. It is only included in the UsageMonitoringData instance for session level usage monitoring.  # noqa: E501

        :return: The ex_usage_pcc_rule_ids of this UsageMonitoringData.
        :rtype: List[str]
        """
        return self._ex_usage_pcc_rule_ids

    @ex_usage_pcc_rule_ids.setter
    def ex_usage_pcc_rule_ids(self, ex_usage_pcc_rule_ids):
        """Sets the ex_usage_pcc_rule_ids of this UsageMonitoringData.

        Contains the PCC rule identifier(s) which corresponding service data flow(s) shall be excluded from PDU Session usage monitoring. It is only included in the UsageMonitoringData instance for session level usage monitoring.  # noqa: E501

        :param ex_usage_pcc_rule_ids: The ex_usage_pcc_rule_ids of this UsageMonitoringData.
        :type ex_usage_pcc_rule_ids: List[str]
        """

        self._ex_usage_pcc_rule_ids = ex_usage_pcc_rule_ids
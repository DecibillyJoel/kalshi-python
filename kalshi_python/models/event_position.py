# coding: utf-8

"""
    Kalshi Trade API

    This documentation describes Kalshi's trading API (known as Trade API v2). By using this API, you agree to Kalshi's Developer Agreement (https://kalshi.com/developer-agreement).  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@kalshi.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EventPosition(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'event_exposure': 'Cent',
        'event_ticker': 'str',
        'fees_paid': 'Cent',
        'realized_pnl': 'Cent',
        'resting_order_count': 'int',
        'total_cost': 'Cent'
    }

    attribute_map = {
        'event_exposure': 'event_exposure',
        'event_ticker': 'event_ticker',
        'fees_paid': 'fees_paid',
        'realized_pnl': 'realized_pnl',
        'resting_order_count': 'resting_order_count',
        'total_cost': 'total_cost'
    }

    def __init__(self, event_exposure=None, event_ticker=None, fees_paid=None, realized_pnl=None, resting_order_count=None, total_cost=None):  # noqa: E501
        """EventPosition - a model defined in Swagger"""  # noqa: E501
        self._event_exposure = None
        self._event_ticker = None
        self._fees_paid = None
        self._realized_pnl = None
        self._resting_order_count = None
        self._total_cost = None
        self.discriminator = None
        self.event_exposure = event_exposure
        self.event_ticker = event_ticker
        self.fees_paid = fees_paid
        self.realized_pnl = realized_pnl
        self.resting_order_count = resting_order_count
        self.total_cost = total_cost

    @property
    def event_exposure(self):
        """Gets the event_exposure of this EventPosition.  # noqa: E501


        :return: The event_exposure of this EventPosition.  # noqa: E501
        :rtype: Cent
        """
        return self._event_exposure

    @event_exposure.setter
    def event_exposure(self, event_exposure):
        """Sets the event_exposure of this EventPosition.


        :param event_exposure: The event_exposure of this EventPosition.  # noqa: E501
        :type: Cent
        """
        if event_exposure is None:
            raise ValueError("Invalid value for `event_exposure`, must not be `None`")  # noqa: E501

        self._event_exposure = event_exposure

    @property
    def event_ticker(self):
        """Gets the event_ticker of this EventPosition.  # noqa: E501

        Unique identifier for events.  # noqa: E501

        :return: The event_ticker of this EventPosition.  # noqa: E501
        :rtype: str
        """
        return self._event_ticker

    @event_ticker.setter
    def event_ticker(self, event_ticker):
        """Sets the event_ticker of this EventPosition.

        Unique identifier for events.  # noqa: E501

        :param event_ticker: The event_ticker of this EventPosition.  # noqa: E501
        :type: str
        """
        if event_ticker is None:
            raise ValueError("Invalid value for `event_ticker`, must not be `None`")  # noqa: E501

        self._event_ticker = event_ticker

    @property
    def fees_paid(self):
        """Gets the fees_paid of this EventPosition.  # noqa: E501


        :return: The fees_paid of this EventPosition.  # noqa: E501
        :rtype: Cent
        """
        return self._fees_paid

    @fees_paid.setter
    def fees_paid(self, fees_paid):
        """Sets the fees_paid of this EventPosition.


        :param fees_paid: The fees_paid of this EventPosition.  # noqa: E501
        :type: Cent
        """
        if fees_paid is None:
            raise ValueError("Invalid value for `fees_paid`, must not be `None`")  # noqa: E501

        self._fees_paid = fees_paid

    @property
    def realized_pnl(self):
        """Gets the realized_pnl of this EventPosition.  # noqa: E501


        :return: The realized_pnl of this EventPosition.  # noqa: E501
        :rtype: Cent
        """
        return self._realized_pnl

    @realized_pnl.setter
    def realized_pnl(self, realized_pnl):
        """Sets the realized_pnl of this EventPosition.


        :param realized_pnl: The realized_pnl of this EventPosition.  # noqa: E501
        :type: Cent
        """
        if realized_pnl is None:
            raise ValueError("Invalid value for `realized_pnl`, must not be `None`")  # noqa: E501

        self._realized_pnl = realized_pnl

    @property
    def resting_order_count(self):
        """Gets the resting_order_count of this EventPosition.  # noqa: E501

        Aggregate size of resting orders in contract units.  # noqa: E501

        :return: The resting_order_count of this EventPosition.  # noqa: E501
        :rtype: int
        """
        return self._resting_order_count

    @resting_order_count.setter
    def resting_order_count(self, resting_order_count):
        """Sets the resting_order_count of this EventPosition.

        Aggregate size of resting orders in contract units.  # noqa: E501

        :param resting_order_count: The resting_order_count of this EventPosition.  # noqa: E501
        :type: int
        """
        if resting_order_count is None:
            raise ValueError("Invalid value for `resting_order_count`, must not be `None`")  # noqa: E501

        self._resting_order_count = resting_order_count

    @property
    def total_cost(self):
        """Gets the total_cost of this EventPosition.  # noqa: E501


        :return: The total_cost of this EventPosition.  # noqa: E501
        :rtype: Cent
        """
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        """Sets the total_cost of this EventPosition.


        :param total_cost: The total_cost of this EventPosition.  # noqa: E501
        :type: Cent
        """
        if total_cost is None:
            raise ValueError("Invalid value for `total_cost`, must not be `None`")  # noqa: E501

        self._total_cost = total_cost

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(EventPosition, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EventPosition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

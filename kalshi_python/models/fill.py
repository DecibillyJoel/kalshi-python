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

class Fill(object):
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
        'action': 'str',
        'count': 'int',
        'created_time': 'OutputTime',
        'is_taker': 'bool',
        'no_price': 'Cent',
        'order_id': 'str',
        'side': 'str',
        'ticker': 'str',
        'trade_id': 'str',
        'yes_price': 'Cent'
    }

    attribute_map = {
        'action': 'action',
        'count': 'count',
        'created_time': 'created_time',
        'is_taker': 'is_taker',
        'no_price': 'no_price',
        'order_id': 'order_id',
        'side': 'side',
        'ticker': 'ticker',
        'trade_id': 'trade_id',
        'yes_price': 'yes_price'
    }

    def __init__(self, action=None, count=None, created_time=None, is_taker=None, no_price=None, order_id=None, side=None, ticker=None, trade_id=None, yes_price=None):  # noqa: E501
        """Fill - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._count = None
        self._created_time = None
        self._is_taker = None
        self._no_price = None
        self._order_id = None
        self._side = None
        self._ticker = None
        self._trade_id = None
        self._yes_price = None
        self.discriminator = None
        self.action = action
        self.count = count
        self.created_time = created_time
        self.is_taker = is_taker
        self.no_price = no_price
        self.order_id = order_id
        self.side = side
        self.ticker = ticker
        self.trade_id = trade_id
        self.yes_price = yes_price

    @property
    def action(self):
        """Gets the action of this Fill.  # noqa: E501

        Specifies if this is a buy or sell order.  # noqa: E501

        :return: The action of this Fill.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this Fill.

        Specifies if this is a buy or sell order.  # noqa: E501

        :param action: The action of this Fill.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        allowed_values = ["buy", "sell", ""]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def count(self):
        """Gets the count of this Fill.  # noqa: E501

        Number of contracts to be bought or sold.  # noqa: E501

        :return: The count of this Fill.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Fill.

        Number of contracts to be bought or sold.  # noqa: E501

        :param count: The count of this Fill.  # noqa: E501
        :type: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def created_time(self):
        """Gets the created_time of this Fill.  # noqa: E501


        :return: The created_time of this Fill.  # noqa: E501
        :rtype: OutputTime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Fill.


        :param created_time: The created_time of this Fill.  # noqa: E501
        :type: OutputTime
        """
        if created_time is None:
            raise ValueError("Invalid value for `created_time`, must not be `None`")  # noqa: E501

        self._created_time = created_time

    @property
    def is_taker(self):
        """Gets the is_taker of this Fill.  # noqa: E501

        If true then this fill was a taker.  # noqa: E501

        :return: The is_taker of this Fill.  # noqa: E501
        :rtype: bool
        """
        return self._is_taker

    @is_taker.setter
    def is_taker(self, is_taker):
        """Sets the is_taker of this Fill.

        If true then this fill was a taker.  # noqa: E501

        :param is_taker: The is_taker of this Fill.  # noqa: E501
        :type: bool
        """
        if is_taker is None:
            raise ValueError("Invalid value for `is_taker`, must not be `None`")  # noqa: E501

        self._is_taker = is_taker

    @property
    def no_price(self):
        """Gets the no_price of this Fill.  # noqa: E501


        :return: The no_price of this Fill.  # noqa: E501
        :rtype: Cent
        """
        return self._no_price

    @no_price.setter
    def no_price(self, no_price):
        """Sets the no_price of this Fill.


        :param no_price: The no_price of this Fill.  # noqa: E501
        :type: Cent
        """
        if no_price is None:
            raise ValueError("Invalid value for `no_price`, must not be `None`")  # noqa: E501

        self._no_price = no_price

    @property
    def order_id(self):
        """Gets the order_id of this Fill.  # noqa: E501

        Unique identifier for orders.  # noqa: E501

        :return: The order_id of this Fill.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Fill.

        Unique identifier for orders.  # noqa: E501

        :param order_id: The order_id of this Fill.  # noqa: E501
        :type: str
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def side(self):
        """Gets the side of this Fill.  # noqa: E501

        Specifies if this is a 'yes' or 'no' fill.  # noqa: E501

        :return: The side of this Fill.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this Fill.

        Specifies if this is a 'yes' or 'no' fill.  # noqa: E501

        :param side: The side of this Fill.  # noqa: E501
        :type: str
        """
        if side is None:
            raise ValueError("Invalid value for `side`, must not be `None`")  # noqa: E501
        allowed_values = ["yes", "no", "invalid", ""]  # noqa: E501
        if side not in allowed_values:
            raise ValueError(
                "Invalid value for `side` ({0}), must be one of {1}"  # noqa: E501
                .format(side, allowed_values)
            )

        self._side = side

    @property
    def ticker(self):
        """Gets the ticker of this Fill.  # noqa: E501

        Unique identifier for markets.  # noqa: E501

        :return: The ticker of this Fill.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this Fill.

        Unique identifier for markets.  # noqa: E501

        :param ticker: The ticker of this Fill.  # noqa: E501
        :type: str
        """
        if ticker is None:
            raise ValueError("Invalid value for `ticker`, must not be `None`")  # noqa: E501

        self._ticker = ticker

    @property
    def trade_id(self):
        """Gets the trade_id of this Fill.  # noqa: E501

        Unique identifier for fills.  # noqa: E501

        :return: The trade_id of this Fill.  # noqa: E501
        :rtype: str
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        """Sets the trade_id of this Fill.

        Unique identifier for fills.  # noqa: E501

        :param trade_id: The trade_id of this Fill.  # noqa: E501
        :type: str
        """
        if trade_id is None:
            raise ValueError("Invalid value for `trade_id`, must not be `None`")  # noqa: E501

        self._trade_id = trade_id

    @property
    def yes_price(self):
        """Gets the yes_price of this Fill.  # noqa: E501


        :return: The yes_price of this Fill.  # noqa: E501
        :rtype: Cent
        """
        return self._yes_price

    @yes_price.setter
    def yes_price(self, yes_price):
        """Sets the yes_price of this Fill.


        :param yes_price: The yes_price of this Fill.  # noqa: E501
        :type: Cent
        """
        if yes_price is None:
            raise ValueError("Invalid value for `yes_price`, must not be `None`")  # noqa: E501

        self._yes_price = yes_price

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
        if issubclass(Fill, dict):
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
        if not isinstance(other, Fill):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

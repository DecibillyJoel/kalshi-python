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

class Order(object):
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
        'client_order_id': 'str',
        'close_cancel_count': 'int',
        'created_time': 'OutputTime',
        'decrease_count': 'int',
        'expiration_time': 'OutputTime',
        'fcc_cancel_count': 'int',
        'last_update_time': 'OutputTime',
        'maker_fill_count': 'int',
        'no_price': 'Cent',
        'order_id': 'str',
        'place_count': 'int',
        'queue_position': 'int',
        'remaining_count': 'int',
        'side': 'str',
        'status': 'OrderStatus',
        'taker_fees': 'Cent',
        'taker_fill_cost': 'Cent',
        'taker_fill_count': 'int',
        'ticker': 'str',
        'type': 'OrderType',
        'user_id': 'str',
        'yes_price': 'Cent'
    }

    attribute_map = {
        'action': 'action',
        'client_order_id': 'client_order_id',
        'close_cancel_count': 'close_cancel_count',
        'created_time': 'created_time',
        'decrease_count': 'decrease_count',
        'expiration_time': 'expiration_time',
        'fcc_cancel_count': 'fcc_cancel_count',
        'last_update_time': 'last_update_time',
        'maker_fill_count': 'maker_fill_count',
        'no_price': 'no_price',
        'order_id': 'order_id',
        'place_count': 'place_count',
        'queue_position': 'queue_position',
        'remaining_count': 'remaining_count',
        'side': 'side',
        'status': 'status',
        'taker_fees': 'taker_fees',
        'taker_fill_cost': 'taker_fill_cost',
        'taker_fill_count': 'taker_fill_count',
        'ticker': 'ticker',
        'type': 'type',
        'user_id': 'user_id',
        'yes_price': 'yes_price'
    }

    def __init__(self, action=None, client_order_id=None, close_cancel_count=None, created_time=None, decrease_count=None, expiration_time=None, fcc_cancel_count=None, last_update_time=None, maker_fill_count=None, no_price=None, order_id=None, place_count=None, queue_position=None, remaining_count=None, side=None, status=None, taker_fees=None, taker_fill_cost=None, taker_fill_count=None, ticker=None, type=None, user_id=None, yes_price=None):  # noqa: E501
        """Order - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._client_order_id = None
        self._close_cancel_count = None
        self._created_time = None
        self._decrease_count = None
        self._expiration_time = None
        self._fcc_cancel_count = None
        self._last_update_time = None
        self._maker_fill_count = None
        self._no_price = None
        self._order_id = None
        self._place_count = None
        self._queue_position = None
        self._remaining_count = None
        self._side = None
        self._status = None
        self._taker_fees = None
        self._taker_fill_cost = None
        self._taker_fill_count = None
        self._ticker = None
        self._type = None
        self._user_id = None
        self._yes_price = None
        self.discriminator = None
        self.action = action
        self.client_order_id = client_order_id
        if close_cancel_count is not None:
            self.close_cancel_count = close_cancel_count
        if created_time is not None:
            self.created_time = created_time
        if decrease_count is not None:
            self.decrease_count = decrease_count
        if expiration_time is not None:
            self.expiration_time = expiration_time
        if fcc_cancel_count is not None:
            self.fcc_cancel_count = fcc_cancel_count
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if maker_fill_count is not None:
            self.maker_fill_count = maker_fill_count
        self.no_price = no_price
        if order_id is not None:
            self.order_id = order_id
        if place_count is not None:
            self.place_count = place_count
        if queue_position is not None:
            self.queue_position = queue_position
        if remaining_count is not None:
            self.remaining_count = remaining_count
        self.side = side
        self.status = status
        if taker_fees is not None:
            self.taker_fees = taker_fees
        if taker_fill_cost is not None:
            self.taker_fill_cost = taker_fill_cost
        if taker_fill_count is not None:
            self.taker_fill_count = taker_fill_count
        self.ticker = ticker
        self.type = type
        if user_id is not None:
            self.user_id = user_id
        self.yes_price = yes_price

    @property
    def action(self):
        """Gets the action of this Order.  # noqa: E501

        Representing trade action; currently supports buy and sell.  # noqa: E501

        :return: The action of this Order.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this Order.

        Representing trade action; currently supports buy and sell.  # noqa: E501

        :param action: The action of this Order.  # noqa: E501
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
    def client_order_id(self):
        """Gets the client_order_id of this Order.  # noqa: E501

        Optional unique identifier for order placement.  # noqa: E501

        :return: The client_order_id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._client_order_id

    @client_order_id.setter
    def client_order_id(self, client_order_id):
        """Sets the client_order_id of this Order.

        Optional unique identifier for order placement.  # noqa: E501

        :param client_order_id: The client_order_id of this Order.  # noqa: E501
        :type: str
        """
        if client_order_id is None:
            raise ValueError("Invalid value for `client_order_id`, must not be `None`")  # noqa: E501

        self._client_order_id = client_order_id

    @property
    def close_cancel_count(self):
        """Gets the close_cancel_count of this Order.  # noqa: E501

        The size of resting orders canceled because of market close (contract units).  # noqa: E501

        :return: The close_cancel_count of this Order.  # noqa: E501
        :rtype: int
        """
        return self._close_cancel_count

    @close_cancel_count.setter
    def close_cancel_count(self, close_cancel_count):
        """Sets the close_cancel_count of this Order.

        The size of resting orders canceled because of market close (contract units).  # noqa: E501

        :param close_cancel_count: The close_cancel_count of this Order.  # noqa: E501
        :type: int
        """

        self._close_cancel_count = close_cancel_count

    @property
    def created_time(self):
        """Gets the created_time of this Order.  # noqa: E501


        :return: The created_time of this Order.  # noqa: E501
        :rtype: OutputTime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Order.


        :param created_time: The created_time of this Order.  # noqa: E501
        :type: OutputTime
        """

        self._created_time = created_time

    @property
    def decrease_count(self):
        """Gets the decrease_count of this Order.  # noqa: E501

        The reduction in the size of resting for orders (contract units).  # noqa: E501

        :return: The decrease_count of this Order.  # noqa: E501
        :rtype: int
        """
        return self._decrease_count

    @decrease_count.setter
    def decrease_count(self, decrease_count):
        """Sets the decrease_count of this Order.

        The reduction in the size of resting for orders (contract units).  # noqa: E501

        :param decrease_count: The decrease_count of this Order.  # noqa: E501
        :type: int
        """

        self._decrease_count = decrease_count

    @property
    def expiration_time(self):
        """Gets the expiration_time of this Order.  # noqa: E501


        :return: The expiration_time of this Order.  # noqa: E501
        :rtype: OutputTime
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        """Sets the expiration_time of this Order.


        :param expiration_time: The expiration_time of this Order.  # noqa: E501
        :type: OutputTime
        """

        self._expiration_time = expiration_time

    @property
    def fcc_cancel_count(self):
        """Gets the fcc_cancel_count of this Order.  # noqa: E501

        The size of resting contracts canceled because of exchange operations (contract units).  # noqa: E501

        :return: The fcc_cancel_count of this Order.  # noqa: E501
        :rtype: int
        """
        return self._fcc_cancel_count

    @fcc_cancel_count.setter
    def fcc_cancel_count(self, fcc_cancel_count):
        """Sets the fcc_cancel_count of this Order.

        The size of resting contracts canceled because of exchange operations (contract units).  # noqa: E501

        :param fcc_cancel_count: The fcc_cancel_count of this Order.  # noqa: E501
        :type: int
        """

        self._fcc_cancel_count = fcc_cancel_count

    @property
    def last_update_time(self):
        """Gets the last_update_time of this Order.  # noqa: E501


        :return: The last_update_time of this Order.  # noqa: E501
        :rtype: OutputTime
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this Order.


        :param last_update_time: The last_update_time of this Order.  # noqa: E501
        :type: OutputTime
        """

        self._last_update_time = last_update_time

    @property
    def maker_fill_count(self):
        """Gets the maker_fill_count of this Order.  # noqa: E501

        The size of filled maker orders (contract units).  # noqa: E501

        :return: The maker_fill_count of this Order.  # noqa: E501
        :rtype: int
        """
        return self._maker_fill_count

    @maker_fill_count.setter
    def maker_fill_count(self, maker_fill_count):
        """Sets the maker_fill_count of this Order.

        The size of filled maker orders (contract units).  # noqa: E501

        :param maker_fill_count: The maker_fill_count of this Order.  # noqa: E501
        :type: int
        """

        self._maker_fill_count = maker_fill_count

    @property
    def no_price(self):
        """Gets the no_price of this Order.  # noqa: E501


        :return: The no_price of this Order.  # noqa: E501
        :rtype: Cent
        """
        return self._no_price

    @no_price.setter
    def no_price(self, no_price):
        """Sets the no_price of this Order.


        :param no_price: The no_price of this Order.  # noqa: E501
        :type: Cent
        """
        if no_price is None:
            raise ValueError("Invalid value for `no_price`, must not be `None`")  # noqa: E501

        self._no_price = no_price

    @property
    def order_id(self):
        """Gets the order_id of this Order.  # noqa: E501


        :return: The order_id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Order.


        :param order_id: The order_id of this Order.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def place_count(self):
        """Gets the place_count of this Order.  # noqa: E501

        the size of placed maker orders (contract units).  # noqa: E501

        :return: The place_count of this Order.  # noqa: E501
        :rtype: int
        """
        return self._place_count

    @place_count.setter
    def place_count(self, place_count):
        """Sets the place_count of this Order.

        the size of placed maker orders (contract units).  # noqa: E501

        :param place_count: The place_count of this Order.  # noqa: E501
        :type: int
        """

        self._place_count = place_count

    @property
    def queue_position(self):
        """Gets the queue_position of this Order.  # noqa: E501

        Position in the priority queue at a given price level  # noqa: E501

        :return: The queue_position of this Order.  # noqa: E501
        :rtype: int
        """
        return self._queue_position

    @queue_position.setter
    def queue_position(self, queue_position):
        """Sets the queue_position of this Order.

        Position in the priority queue at a given price level  # noqa: E501

        :param queue_position: The queue_position of this Order.  # noqa: E501
        :type: int
        """

        self._queue_position = queue_position

    @property
    def remaining_count(self):
        """Gets the remaining_count of this Order.  # noqa: E501

        The size of the remaining resting orders (contract units).  # noqa: E501

        :return: The remaining_count of this Order.  # noqa: E501
        :rtype: int
        """
        return self._remaining_count

    @remaining_count.setter
    def remaining_count(self, remaining_count):
        """Sets the remaining_count of this Order.

        The size of the remaining resting orders (contract units).  # noqa: E501

        :param remaining_count: The remaining_count of this Order.  # noqa: E501
        :type: int
        """

        self._remaining_count = remaining_count

    @property
    def side(self):
        """Gets the side of this Order.  # noqa: E501

        Representing direction of the order; currently supports yes and no.  # noqa: E501

        :return: The side of this Order.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this Order.

        Representing direction of the order; currently supports yes and no.  # noqa: E501

        :param side: The side of this Order.  # noqa: E501
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
    def status(self):
        """Gets the status of this Order.  # noqa: E501


        :return: The status of this Order.  # noqa: E501
        :rtype: OrderStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Order.


        :param status: The status of this Order.  # noqa: E501
        :type: OrderStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def taker_fees(self):
        """Gets the taker_fees of this Order.  # noqa: E501


        :return: The taker_fees of this Order.  # noqa: E501
        :rtype: Cent
        """
        return self._taker_fees

    @taker_fees.setter
    def taker_fees(self, taker_fees):
        """Sets the taker_fees of this Order.


        :param taker_fees: The taker_fees of this Order.  # noqa: E501
        :type: Cent
        """

        self._taker_fees = taker_fees

    @property
    def taker_fill_cost(self):
        """Gets the taker_fill_cost of this Order.  # noqa: E501


        :return: The taker_fill_cost of this Order.  # noqa: E501
        :rtype: Cent
        """
        return self._taker_fill_cost

    @taker_fill_cost.setter
    def taker_fill_cost(self, taker_fill_cost):
        """Sets the taker_fill_cost of this Order.


        :param taker_fill_cost: The taker_fill_cost of this Order.  # noqa: E501
        :type: Cent
        """

        self._taker_fill_cost = taker_fill_cost

    @property
    def taker_fill_count(self):
        """Gets the taker_fill_count of this Order.  # noqa: E501

        The size of filled taker orders (contract units)  # noqa: E501

        :return: The taker_fill_count of this Order.  # noqa: E501
        :rtype: int
        """
        return self._taker_fill_count

    @taker_fill_count.setter
    def taker_fill_count(self, taker_fill_count):
        """Sets the taker_fill_count of this Order.

        The size of filled taker orders (contract units)  # noqa: E501

        :param taker_fill_count: The taker_fill_count of this Order.  # noqa: E501
        :type: int
        """

        self._taker_fill_count = taker_fill_count

    @property
    def ticker(self):
        """Gets the ticker of this Order.  # noqa: E501

        Unique identifier for markets.  # noqa: E501

        :return: The ticker of this Order.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this Order.

        Unique identifier for markets.  # noqa: E501

        :param ticker: The ticker of this Order.  # noqa: E501
        :type: str
        """
        if ticker is None:
            raise ValueError("Invalid value for `ticker`, must not be `None`")  # noqa: E501

        self._ticker = ticker

    @property
    def type(self):
        """Gets the type of this Order.  # noqa: E501


        :return: The type of this Order.  # noqa: E501
        :rtype: OrderType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Order.


        :param type: The type of this Order.  # noqa: E501
        :type: OrderType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def user_id(self):
        """Gets the user_id of this Order.  # noqa: E501


        :return: The user_id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Order.


        :param user_id: The user_id of this Order.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def yes_price(self):
        """Gets the yes_price of this Order.  # noqa: E501


        :return: The yes_price of this Order.  # noqa: E501
        :rtype: Cent
        """
        return self._yes_price

    @yes_price.setter
    def yes_price(self, yes_price):
        """Sets the yes_price of this Order.


        :param yes_price: The yes_price of this Order.  # noqa: E501
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
        if issubclass(Order, dict):
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
        if not isinstance(other, Order):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

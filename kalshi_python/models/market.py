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

class Market(object):
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
        'can_close_early': 'bool',
        'category': 'str',
        'close_time': 'OutputTime',
        'event_ticker': 'str',
        'expiration_time': 'OutputTime',
        'expiration_value': 'str',
        'last_price': 'Cent',
        'liquidity': 'Cent',
        'no_ask': 'Cent',
        'no_bid': 'Cent',
        'open_interest': 'int',
        'open_time': 'OutputTime',
        'previous_price': 'Cent',
        'previous_yes_ask': 'Cent',
        'previous_yes_bid': 'Cent',
        'result': 'str',
        'risk_limit_cents': 'Cent',
        'status': 'object',
        'subtitle': 'str',
        'ticker': 'str',
        'volume': 'int',
        'volume_24h': 'int',
        'yes_ask': 'Cent',
        'yes_bid': 'Cent'
    }

    attribute_map = {
        'can_close_early': 'can_close_early',
        'category': 'category',
        'close_time': 'close_time',
        'event_ticker': 'event_ticker',
        'expiration_time': 'expiration_time',
        'expiration_value': 'expiration_value',
        'last_price': 'last_price',
        'liquidity': 'liquidity',
        'no_ask': 'no_ask',
        'no_bid': 'no_bid',
        'open_interest': 'open_interest',
        'open_time': 'open_time',
        'previous_price': 'previous_price',
        'previous_yes_ask': 'previous_yes_ask',
        'previous_yes_bid': 'previous_yes_bid',
        'result': 'result',
        'risk_limit_cents': 'risk_limit_cents',
        'status': 'status',
        'subtitle': 'subtitle',
        'ticker': 'ticker',
        'volume': 'volume',
        'volume_24h': 'volume_24h',
        'yes_ask': 'yes_ask',
        'yes_bid': 'yes_bid'
    }

    def __init__(self, can_close_early=None, category=None, close_time=None, event_ticker=None, expiration_time=None, expiration_value=None, last_price=None, liquidity=None, no_ask=None, no_bid=None, open_interest=None, open_time=None, previous_price=None, previous_yes_ask=None, previous_yes_bid=None, result=None, risk_limit_cents=None, status=None, subtitle=None, ticker=None, volume=None, volume_24h=None, yes_ask=None, yes_bid=None):  # noqa: E501
        """Market - a model defined in Swagger"""  # noqa: E501
        self._can_close_early = None
        self._category = None
        self._close_time = None
        self._event_ticker = None
        self._expiration_time = None
        self._expiration_value = None
        self._last_price = None
        self._liquidity = None
        self._no_ask = None
        self._no_bid = None
        self._open_interest = None
        self._open_time = None
        self._previous_price = None
        self._previous_yes_ask = None
        self._previous_yes_bid = None
        self._result = None
        self._risk_limit_cents = None
        self._status = None
        self._subtitle = None
        self._ticker = None
        self._volume = None
        self._volume_24h = None
        self._yes_ask = None
        self._yes_bid = None
        self.discriminator = None
        self.can_close_early = can_close_early
        self.category = category
        self.close_time = close_time
        self.event_ticker = event_ticker
        self.expiration_time = expiration_time
        self.expiration_value = expiration_value
        self.last_price = last_price
        self.liquidity = liquidity
        self.no_ask = no_ask
        self.no_bid = no_bid
        self.open_interest = open_interest
        self.open_time = open_time
        self.previous_price = previous_price
        self.previous_yes_ask = previous_yes_ask
        self.previous_yes_bid = previous_yes_bid
        self.result = result
        self.risk_limit_cents = risk_limit_cents
        self.status = status
        self.subtitle = subtitle
        self.ticker = ticker
        self.volume = volume
        self.volume_24h = volume_24h
        self.yes_ask = yes_ask
        self.yes_bid = yes_bid

    @property
    def can_close_early(self):
        """Gets the can_close_early of this Market.  # noqa: E501

        If true then this market can close earlier then the time provided on close_time.  # noqa: E501

        :return: The can_close_early of this Market.  # noqa: E501
        :rtype: bool
        """
        return self._can_close_early

    @can_close_early.setter
    def can_close_early(self, can_close_early):
        """Sets the can_close_early of this Market.

        If true then this market can close earlier then the time provided on close_time.  # noqa: E501

        :param can_close_early: The can_close_early of this Market.  # noqa: E501
        :type: bool
        """
        if can_close_early is None:
            raise ValueError("Invalid value for `can_close_early`, must not be `None`")  # noqa: E501

        self._can_close_early = can_close_early

    @property
    def category(self):
        """Gets the category of this Market.  # noqa: E501

        Category for this market.  # noqa: E501

        :return: The category of this Market.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Market.

        Category for this market.  # noqa: E501

        :param category: The category of this Market.  # noqa: E501
        :type: str
        """
        if category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501

        self._category = category

    @property
    def close_time(self):
        """Gets the close_time of this Market.  # noqa: E501


        :return: The close_time of this Market.  # noqa: E501
        :rtype: OutputTime
        """
        return self._close_time

    @close_time.setter
    def close_time(self, close_time):
        """Sets the close_time of this Market.


        :param close_time: The close_time of this Market.  # noqa: E501
        :type: OutputTime
        """
        if close_time is None:
            raise ValueError("Invalid value for `close_time`, must not be `None`")  # noqa: E501

        self._close_time = close_time

    @property
    def event_ticker(self):
        """Gets the event_ticker of this Market.  # noqa: E501

        Unique identifier for events.  # noqa: E501

        :return: The event_ticker of this Market.  # noqa: E501
        :rtype: str
        """
        return self._event_ticker

    @event_ticker.setter
    def event_ticker(self, event_ticker):
        """Sets the event_ticker of this Market.

        Unique identifier for events.  # noqa: E501

        :param event_ticker: The event_ticker of this Market.  # noqa: E501
        :type: str
        """
        if event_ticker is None:
            raise ValueError("Invalid value for `event_ticker`, must not be `None`")  # noqa: E501

        self._event_ticker = event_ticker

    @property
    def expiration_time(self):
        """Gets the expiration_time of this Market.  # noqa: E501


        :return: The expiration_time of this Market.  # noqa: E501
        :rtype: OutputTime
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        """Sets the expiration_time of this Market.


        :param expiration_time: The expiration_time of this Market.  # noqa: E501
        :type: OutputTime
        """
        if expiration_time is None:
            raise ValueError("Invalid value for `expiration_time`, must not be `None`")  # noqa: E501

        self._expiration_time = expiration_time

    @property
    def expiration_value(self):
        """Gets the expiration_value of this Market.  # noqa: E501

        The value that was considered for the settlement.  # noqa: E501

        :return: The expiration_value of this Market.  # noqa: E501
        :rtype: str
        """
        return self._expiration_value

    @expiration_value.setter
    def expiration_value(self, expiration_value):
        """Sets the expiration_value of this Market.

        The value that was considered for the settlement.  # noqa: E501

        :param expiration_value: The expiration_value of this Market.  # noqa: E501
        :type: str
        """
        if expiration_value is None:
            raise ValueError("Invalid value for `expiration_value`, must not be `None`")  # noqa: E501

        self._expiration_value = expiration_value

    @property
    def last_price(self):
        """Gets the last_price of this Market.  # noqa: E501


        :return: The last_price of this Market.  # noqa: E501
        :rtype: Cent
        """
        return self._last_price

    @last_price.setter
    def last_price(self, last_price):
        """Sets the last_price of this Market.


        :param last_price: The last_price of this Market.  # noqa: E501
        :type: Cent
        """
        if last_price is None:
            raise ValueError("Invalid value for `last_price`, must not be `None`")  # noqa: E501

        self._last_price = last_price

    @property
    def liquidity(self):
        """Gets the liquidity of this Market.  # noqa: E501


        :return: The liquidity of this Market.  # noqa: E501
        :rtype: Cent
        """
        return self._liquidity

    @liquidity.setter
    def liquidity(self, liquidity):
        """Sets the liquidity of this Market.


        :param liquidity: The liquidity of this Market.  # noqa: E501
        :type: Cent
        """
        if liquidity is None:
            raise ValueError("Invalid value for `liquidity`, must not be `None`")  # noqa: E501

        self._liquidity = liquidity

    @property
    def no_ask(self):
        """Gets the no_ask of this Market.  # noqa: E501


        :return: The no_ask of this Market.  # noqa: E501
        :rtype: Cent
        """
        return self._no_ask

    @no_ask.setter
    def no_ask(self, no_ask):
        """Sets the no_ask of this Market.


        :param no_ask: The no_ask of this Market.  # noqa: E501
        :type: Cent
        """
        if no_ask is None:
            raise ValueError("Invalid value for `no_ask`, must not be `None`")  # noqa: E501

        self._no_ask = no_ask

    @property
    def no_bid(self):
        """Gets the no_bid of this Market.  # noqa: E501


        :return: The no_bid of this Market.  # noqa: E501
        :rtype: Cent
        """
        return self._no_bid

    @no_bid.setter
    def no_bid(self, no_bid):
        """Sets the no_bid of this Market.


        :param no_bid: The no_bid of this Market.  # noqa: E501
        :type: Cent
        """
        if no_bid is None:
            raise ValueError("Invalid value for `no_bid`, must not be `None`")  # noqa: E501

        self._no_bid = no_bid

    @property
    def open_interest(self):
        """Gets the open_interest of this Market.  # noqa: E501

        Number of contracts bought on this market disconsidering netting.  # noqa: E501

        :return: The open_interest of this Market.  # noqa: E501
        :rtype: int
        """
        return self._open_interest

    @open_interest.setter
    def open_interest(self, open_interest):
        """Sets the open_interest of this Market.

        Number of contracts bought on this market disconsidering netting.  # noqa: E501

        :param open_interest: The open_interest of this Market.  # noqa: E501
        :type: int
        """
        if open_interest is None:
            raise ValueError("Invalid value for `open_interest`, must not be `None`")  # noqa: E501

        self._open_interest = open_interest

    @property
    def open_time(self):
        """Gets the open_time of this Market.  # noqa: E501


        :return: The open_time of this Market.  # noqa: E501
        :rtype: OutputTime
        """
        return self._open_time

    @open_time.setter
    def open_time(self, open_time):
        """Sets the open_time of this Market.


        :param open_time: The open_time of this Market.  # noqa: E501
        :type: OutputTime
        """
        if open_time is None:
            raise ValueError("Invalid value for `open_time`, must not be `None`")  # noqa: E501

        self._open_time = open_time

    @property
    def previous_price(self):
        """Gets the previous_price of this Market.  # noqa: E501


        :return: The previous_price of this Market.  # noqa: E501
        :rtype: Cent
        """
        return self._previous_price

    @previous_price.setter
    def previous_price(self, previous_price):
        """Sets the previous_price of this Market.


        :param previous_price: The previous_price of this Market.  # noqa: E501
        :type: Cent
        """
        if previous_price is None:
            raise ValueError("Invalid value for `previous_price`, must not be `None`")  # noqa: E501

        self._previous_price = previous_price

    @property
    def previous_yes_ask(self):
        """Gets the previous_yes_ask of this Market.  # noqa: E501


        :return: The previous_yes_ask of this Market.  # noqa: E501
        :rtype: Cent
        """
        return self._previous_yes_ask

    @previous_yes_ask.setter
    def previous_yes_ask(self, previous_yes_ask):
        """Sets the previous_yes_ask of this Market.


        :param previous_yes_ask: The previous_yes_ask of this Market.  # noqa: E501
        :type: Cent
        """
        if previous_yes_ask is None:
            raise ValueError("Invalid value for `previous_yes_ask`, must not be `None`")  # noqa: E501

        self._previous_yes_ask = previous_yes_ask

    @property
    def previous_yes_bid(self):
        """Gets the previous_yes_bid of this Market.  # noqa: E501


        :return: The previous_yes_bid of this Market.  # noqa: E501
        :rtype: Cent
        """
        return self._previous_yes_bid

    @previous_yes_bid.setter
    def previous_yes_bid(self, previous_yes_bid):
        """Sets the previous_yes_bid of this Market.


        :param previous_yes_bid: The previous_yes_bid of this Market.  # noqa: E501
        :type: Cent
        """
        if previous_yes_bid is None:
            raise ValueError("Invalid value for `previous_yes_bid`, must not be `None`")  # noqa: E501

        self._previous_yes_bid = previous_yes_bid

    @property
    def result(self):
        """Gets the result of this Market.  # noqa: E501

        Settlement result for this market.  # noqa: E501

        :return: The result of this Market.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this Market.

        Settlement result for this market.  # noqa: E501

        :param result: The result of this Market.  # noqa: E501
        :type: str
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501
        allowed_values = ["", "yes", "no", "void", "invalid", "all_no", "all_yes"]  # noqa: E501
        if result not in allowed_values:
            raise ValueError(
                "Invalid value for `result` ({0}), must be one of {1}"  # noqa: E501
                .format(result, allowed_values)
            )

        self._result = result

    @property
    def risk_limit_cents(self):
        """Gets the risk_limit_cents of this Market.  # noqa: E501


        :return: The risk_limit_cents of this Market.  # noqa: E501
        :rtype: Cent
        """
        return self._risk_limit_cents

    @risk_limit_cents.setter
    def risk_limit_cents(self, risk_limit_cents):
        """Sets the risk_limit_cents of this Market.


        :param risk_limit_cents: The risk_limit_cents of this Market.  # noqa: E501
        :type: Cent
        """
        if risk_limit_cents is None:
            raise ValueError("Invalid value for `risk_limit_cents`, must not be `None`")  # noqa: E501

        self._risk_limit_cents = risk_limit_cents

    @property
    def status(self):
        """Gets the status of this Market.  # noqa: E501

        Represents the current status of a market.  # noqa: E501

        :return: The status of this Market.  # noqa: E501
        :rtype: object
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Market.

        Represents the current status of a market.  # noqa: E501

        :param status: The status of this Market.  # noqa: E501
        :type: object
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def subtitle(self):
        """Gets the subtitle of this Market.  # noqa: E501

        Shortened title for this market.  # noqa: E501

        :return: The subtitle of this Market.  # noqa: E501
        :rtype: str
        """
        return self._subtitle

    @subtitle.setter
    def subtitle(self, subtitle):
        """Sets the subtitle of this Market.

        Shortened title for this market.  # noqa: E501

        :param subtitle: The subtitle of this Market.  # noqa: E501
        :type: str
        """
        if subtitle is None:
            raise ValueError("Invalid value for `subtitle`, must not be `None`")  # noqa: E501

        self._subtitle = subtitle

    @property
    def ticker(self):
        """Gets the ticker of this Market.  # noqa: E501

        Unique identifier for markets.  # noqa: E501

        :return: The ticker of this Market.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this Market.

        Unique identifier for markets.  # noqa: E501

        :param ticker: The ticker of this Market.  # noqa: E501
        :type: str
        """
        if ticker is None:
            raise ValueError("Invalid value for `ticker`, must not be `None`")  # noqa: E501

        self._ticker = ticker

    @property
    def volume(self):
        """Gets the volume of this Market.  # noqa: E501

        Number of contracts bought on this market.  # noqa: E501

        :return: The volume of this Market.  # noqa: E501
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this Market.

        Number of contracts bought on this market.  # noqa: E501

        :param volume: The volume of this Market.  # noqa: E501
        :type: int
        """
        if volume is None:
            raise ValueError("Invalid value for `volume`, must not be `None`")  # noqa: E501

        self._volume = volume

    @property
    def volume_24h(self):
        """Gets the volume_24h of this Market.  # noqa: E501

        Number of contracts bought on this market in the past day.  # noqa: E501

        :return: The volume_24h of this Market.  # noqa: E501
        :rtype: int
        """
        return self._volume_24h

    @volume_24h.setter
    def volume_24h(self, volume_24h):
        """Sets the volume_24h of this Market.

        Number of contracts bought on this market in the past day.  # noqa: E501

        :param volume_24h: The volume_24h of this Market.  # noqa: E501
        :type: int
        """
        if volume_24h is None:
            raise ValueError("Invalid value for `volume_24h`, must not be `None`")  # noqa: E501

        self._volume_24h = volume_24h

    @property
    def yes_ask(self):
        """Gets the yes_ask of this Market.  # noqa: E501


        :return: The yes_ask of this Market.  # noqa: E501
        :rtype: Cent
        """
        return self._yes_ask

    @yes_ask.setter
    def yes_ask(self, yes_ask):
        """Sets the yes_ask of this Market.


        :param yes_ask: The yes_ask of this Market.  # noqa: E501
        :type: Cent
        """
        if yes_ask is None:
            raise ValueError("Invalid value for `yes_ask`, must not be `None`")  # noqa: E501

        self._yes_ask = yes_ask

    @property
    def yes_bid(self):
        """Gets the yes_bid of this Market.  # noqa: E501


        :return: The yes_bid of this Market.  # noqa: E501
        :rtype: Cent
        """
        return self._yes_bid

    @yes_bid.setter
    def yes_bid(self, yes_bid):
        """Sets the yes_bid of this Market.


        :param yes_bid: The yes_bid of this Market.  # noqa: E501
        :type: Cent
        """
        if yes_bid is None:
            raise ValueError("Invalid value for `yes_bid`, must not be `None`")  # noqa: E501

        self._yes_bid = yes_bid

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
        if issubclass(Market, dict):
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
        if not isinstance(other, Market):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

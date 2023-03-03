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

class OrderBook(object):
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
        'no': 'list[PriceLevel]',
        'yes': 'list[PriceLevel]'
    }

    attribute_map = {
        'no': 'no',
        'yes': 'yes'
    }

    def __init__(self, no=None, yes=None):  # noqa: E501
        """OrderBook - a model defined in Swagger"""  # noqa: E501
        self._no = None
        self._yes = None
        self.discriminator = None
        self.no = no
        self.yes = yes

    @property
    def no(self):
        """Gets the no of this OrderBook.  # noqa: E501


        :return: The no of this OrderBook.  # noqa: E501
        :rtype: list[PriceLevel]
        """
        return self._no

    @no.setter
    def no(self, no):
        """Sets the no of this OrderBook.


        :param no: The no of this OrderBook.  # noqa: E501
        :type: list[PriceLevel]
        """
        if no is None:
            self._no = []
        else:
            self._no = no

    @property
    def yes(self):
        """Gets the yes of this OrderBook.  # noqa: E501


        :return: The yes of this OrderBook.  # noqa: E501
        :rtype: list[PriceLevel]
        """
        return self._yes

    @yes.setter
    def yes(self, yes):
        """Sets the yes of this OrderBook.


        :param yes: The yes of this OrderBook.  # noqa: E501
        :type: list[PriceLevel]
        """
        if yes is None:
            self._yes = []
        else:
            self._yes = yes

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
        if issubclass(OrderBook, dict):
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
        if not isinstance(other, OrderBook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.  # noqa: E501

    OpenAPI spec version: 1.4.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from pynifi_client.models.position_dto import PositionDTO  # noqa: F401,E501


class TenantDTO(object):
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
        'id': 'str',
        'parent_group_id': 'str',
        'position': 'PositionDTO',
        'identity': 'str',
        'configurable': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'parent_group_id': 'parentGroupId',
        'position': 'position',
        'identity': 'identity',
        'configurable': 'configurable'
    }

    def __init__(self, id=None, parent_group_id=None, position=None, identity=None, configurable=False):  # noqa: E501
        """TenantDTO - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._parent_group_id = None
        self._position = None
        self._identity = None
        self._configurable = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if parent_group_id is not None:
            self.parent_group_id = parent_group_id
        if position is not None:
            self.position = position
        if identity is not None:
            self.identity = identity
        if configurable is not None:
            self.configurable = configurable

    @property
    def id(self):
        """Gets the id of this TenantDTO.  # noqa: E501

        The id of the component.  # noqa: E501

        :return: The id of this TenantDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TenantDTO.

        The id of the component.  # noqa: E501

        :param id: The id of this TenantDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def parent_group_id(self):
        """Gets the parent_group_id of this TenantDTO.  # noqa: E501

        The id of parent process group of this component if applicable.  # noqa: E501

        :return: The parent_group_id of this TenantDTO.  # noqa: E501
        :rtype: str
        """
        return self._parent_group_id

    @parent_group_id.setter
    def parent_group_id(self, parent_group_id):
        """Sets the parent_group_id of this TenantDTO.

        The id of parent process group of this component if applicable.  # noqa: E501

        :param parent_group_id: The parent_group_id of this TenantDTO.  # noqa: E501
        :type: str
        """

        self._parent_group_id = parent_group_id

    @property
    def position(self):
        """Gets the position of this TenantDTO.  # noqa: E501

        The position of this component in the UI if applicable.  # noqa: E501

        :return: The position of this TenantDTO.  # noqa: E501
        :rtype: PositionDTO
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this TenantDTO.

        The position of this component in the UI if applicable.  # noqa: E501

        :param position: The position of this TenantDTO.  # noqa: E501
        :type: PositionDTO
        """

        self._position = position

    @property
    def identity(self):
        """Gets the identity of this TenantDTO.  # noqa: E501

        The identity of the tenant.  # noqa: E501

        :return: The identity of this TenantDTO.  # noqa: E501
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this TenantDTO.

        The identity of the tenant.  # noqa: E501

        :param identity: The identity of this TenantDTO.  # noqa: E501
        :type: str
        """

        self._identity = identity

    @property
    def configurable(self):
        """Gets the configurable of this TenantDTO.  # noqa: E501

        Whether this tenant is configurable.  # noqa: E501

        :return: The configurable of this TenantDTO.  # noqa: E501
        :rtype: bool
        """
        return self._configurable

    @configurable.setter
    def configurable(self, configurable):
        """Sets the configurable of this TenantDTO.

        Whether this tenant is configurable.  # noqa: E501

        :param configurable: The configurable of this TenantDTO.  # noqa: E501
        :type: bool
        """

        self._configurable = configurable

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TenantDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

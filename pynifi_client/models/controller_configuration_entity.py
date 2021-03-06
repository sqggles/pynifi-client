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

from pynifi_client.models.controller_configuration_dto import ControllerConfigurationDTO  # noqa: F401,E501
from pynifi_client.models.permissions_dto import PermissionsDTO  # noqa: F401,E501
from pynifi_client.models.revision_dto import RevisionDTO  # noqa: F401,E501


class ControllerConfigurationEntity(object):
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
        'revision': 'RevisionDTO',
        'permissions': 'PermissionsDTO',
        'component': 'ControllerConfigurationDTO'
    }

    attribute_map = {
        'revision': 'revision',
        'permissions': 'permissions',
        'component': 'component'
    }

    def __init__(self, revision=None, permissions=None, component=None):  # noqa: E501
        """ControllerConfigurationEntity - a model defined in Swagger"""  # noqa: E501

        self._revision = None
        self._permissions = None
        self._component = None
        self.discriminator = None

        if revision is not None:
            self.revision = revision
        if permissions is not None:
            self.permissions = permissions
        if component is not None:
            self.component = component

    @property
    def revision(self):
        """Gets the revision of this ControllerConfigurationEntity.  # noqa: E501

        The revision for this request/response. The revision is required for any mutable flow requests and is included in all responses.  # noqa: E501

        :return: The revision of this ControllerConfigurationEntity.  # noqa: E501
        :rtype: RevisionDTO
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this ControllerConfigurationEntity.

        The revision for this request/response. The revision is required for any mutable flow requests and is included in all responses.  # noqa: E501

        :param revision: The revision of this ControllerConfigurationEntity.  # noqa: E501
        :type: RevisionDTO
        """

        self._revision = revision

    @property
    def permissions(self):
        """Gets the permissions of this ControllerConfigurationEntity.  # noqa: E501

        The permissions for this component.  # noqa: E501

        :return: The permissions of this ControllerConfigurationEntity.  # noqa: E501
        :rtype: PermissionsDTO
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this ControllerConfigurationEntity.

        The permissions for this component.  # noqa: E501

        :param permissions: The permissions of this ControllerConfigurationEntity.  # noqa: E501
        :type: PermissionsDTO
        """

        self._permissions = permissions

    @property
    def component(self):
        """Gets the component of this ControllerConfigurationEntity.  # noqa: E501

        The controller configuration.  # noqa: E501

        :return: The component of this ControllerConfigurationEntity.  # noqa: E501
        :rtype: ControllerConfigurationDTO
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this ControllerConfigurationEntity.

        The controller configuration.  # noqa: E501

        :param component: The component of this ControllerConfigurationEntity.  # noqa: E501
        :type: ControllerConfigurationDTO
        """

        self._component = component

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
        if not isinstance(other, ControllerConfigurationEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

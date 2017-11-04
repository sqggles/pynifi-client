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


class VariableRegistryUpdateStepDTO(object):
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
        'description': 'str',
        'complete': 'bool',
        'failure_reason': 'str'
    }

    attribute_map = {
        'description': 'description',
        'complete': 'complete',
        'failure_reason': 'failureReason'
    }

    def __init__(self, description=None, complete=False, failure_reason=None):  # noqa: E501
        """VariableRegistryUpdateStepDTO - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._complete = None
        self._failure_reason = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if complete is not None:
            self.complete = complete
        if failure_reason is not None:
            self.failure_reason = failure_reason

    @property
    def description(self):
        """Gets the description of this VariableRegistryUpdateStepDTO.  # noqa: E501

        Explanation of what happens in this step  # noqa: E501

        :return: The description of this VariableRegistryUpdateStepDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VariableRegistryUpdateStepDTO.

        Explanation of what happens in this step  # noqa: E501

        :param description: The description of this VariableRegistryUpdateStepDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def complete(self):
        """Gets the complete of this VariableRegistryUpdateStepDTO.  # noqa: E501

        Whether or not this step has completed  # noqa: E501

        :return: The complete of this VariableRegistryUpdateStepDTO.  # noqa: E501
        :rtype: bool
        """
        return self._complete

    @complete.setter
    def complete(self, complete):
        """Sets the complete of this VariableRegistryUpdateStepDTO.

        Whether or not this step has completed  # noqa: E501

        :param complete: The complete of this VariableRegistryUpdateStepDTO.  # noqa: E501
        :type: bool
        """

        self._complete = complete

    @property
    def failure_reason(self):
        """Gets the failure_reason of this VariableRegistryUpdateStepDTO.  # noqa: E501

        An explanation of why this step failed, or null if this step did not fail  # noqa: E501

        :return: The failure_reason of this VariableRegistryUpdateStepDTO.  # noqa: E501
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this VariableRegistryUpdateStepDTO.

        An explanation of why this step failed, or null if this step did not fail  # noqa: E501

        :param failure_reason: The failure_reason of this VariableRegistryUpdateStepDTO.  # noqa: E501
        :type: str
        """

        self._failure_reason = failure_reason

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
        if not isinstance(other, VariableRegistryUpdateStepDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
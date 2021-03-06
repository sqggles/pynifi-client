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

from pynifi_client.models.node_status_snapshots_dto import NodeStatusSnapshotsDTO  # noqa: F401,E501
from pynifi_client.models.status_descriptor_dto import StatusDescriptorDTO  # noqa: F401,E501
from pynifi_client.models.status_snapshot_dto import StatusSnapshotDTO  # noqa: F401,E501


class StatusHistoryDTO(object):
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
        'generated': 'str',
        'component_details': 'dict(str, str)',
        'field_descriptors': 'list[StatusDescriptorDTO]',
        'aggregate_snapshots': 'list[StatusSnapshotDTO]',
        'node_snapshots': 'list[NodeStatusSnapshotsDTO]'
    }

    attribute_map = {
        'generated': 'generated',
        'component_details': 'componentDetails',
        'field_descriptors': 'fieldDescriptors',
        'aggregate_snapshots': 'aggregateSnapshots',
        'node_snapshots': 'nodeSnapshots'
    }

    def __init__(self, generated=None, component_details=None, field_descriptors=None, aggregate_snapshots=None, node_snapshots=None):  # noqa: E501
        """StatusHistoryDTO - a model defined in Swagger"""  # noqa: E501

        self._generated = None
        self._component_details = None
        self._field_descriptors = None
        self._aggregate_snapshots = None
        self._node_snapshots = None
        self.discriminator = None

        if generated is not None:
            self.generated = generated
        if component_details is not None:
            self.component_details = component_details
        if field_descriptors is not None:
            self.field_descriptors = field_descriptors
        if aggregate_snapshots is not None:
            self.aggregate_snapshots = aggregate_snapshots
        if node_snapshots is not None:
            self.node_snapshots = node_snapshots

    @property
    def generated(self):
        """Gets the generated of this StatusHistoryDTO.  # noqa: E501

        When the status history was generated.  # noqa: E501

        :return: The generated of this StatusHistoryDTO.  # noqa: E501
        :rtype: str
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """Sets the generated of this StatusHistoryDTO.

        When the status history was generated.  # noqa: E501

        :param generated: The generated of this StatusHistoryDTO.  # noqa: E501
        :type: str
        """

        self._generated = generated

    @property
    def component_details(self):
        """Gets the component_details of this StatusHistoryDTO.  # noqa: E501

        A Map of key/value pairs that describe the component that the status history belongs to  # noqa: E501

        :return: The component_details of this StatusHistoryDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._component_details

    @component_details.setter
    def component_details(self, component_details):
        """Sets the component_details of this StatusHistoryDTO.

        A Map of key/value pairs that describe the component that the status history belongs to  # noqa: E501

        :param component_details: The component_details of this StatusHistoryDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._component_details = component_details

    @property
    def field_descriptors(self):
        """Gets the field_descriptors of this StatusHistoryDTO.  # noqa: E501

        The Descriptors that provide information on each of the metrics provided in the status history  # noqa: E501

        :return: The field_descriptors of this StatusHistoryDTO.  # noqa: E501
        :rtype: list[StatusDescriptorDTO]
        """
        return self._field_descriptors

    @field_descriptors.setter
    def field_descriptors(self, field_descriptors):
        """Sets the field_descriptors of this StatusHistoryDTO.

        The Descriptors that provide information on each of the metrics provided in the status history  # noqa: E501

        :param field_descriptors: The field_descriptors of this StatusHistoryDTO.  # noqa: E501
        :type: list[StatusDescriptorDTO]
        """

        self._field_descriptors = field_descriptors

    @property
    def aggregate_snapshots(self):
        """Gets the aggregate_snapshots of this StatusHistoryDTO.  # noqa: E501

        A list of StatusSnapshotDTO objects that provide the actual metric values for the component. If the NiFi instance is clustered, this will represent the aggregate status across all nodes. If the NiFi instance is not clustered, this will represent the status of the entire NiFi instance.  # noqa: E501

        :return: The aggregate_snapshots of this StatusHistoryDTO.  # noqa: E501
        :rtype: list[StatusSnapshotDTO]
        """
        return self._aggregate_snapshots

    @aggregate_snapshots.setter
    def aggregate_snapshots(self, aggregate_snapshots):
        """Sets the aggregate_snapshots of this StatusHistoryDTO.

        A list of StatusSnapshotDTO objects that provide the actual metric values for the component. If the NiFi instance is clustered, this will represent the aggregate status across all nodes. If the NiFi instance is not clustered, this will represent the status of the entire NiFi instance.  # noqa: E501

        :param aggregate_snapshots: The aggregate_snapshots of this StatusHistoryDTO.  # noqa: E501
        :type: list[StatusSnapshotDTO]
        """

        self._aggregate_snapshots = aggregate_snapshots

    @property
    def node_snapshots(self):
        """Gets the node_snapshots of this StatusHistoryDTO.  # noqa: E501

        The NodeStatusSnapshotsDTO objects that provide the actual metric values for the component, for each node. If the NiFi instance is not clustered, this value will be null.  # noqa: E501

        :return: The node_snapshots of this StatusHistoryDTO.  # noqa: E501
        :rtype: list[NodeStatusSnapshotsDTO]
        """
        return self._node_snapshots

    @node_snapshots.setter
    def node_snapshots(self, node_snapshots):
        """Sets the node_snapshots of this StatusHistoryDTO.

        The NodeStatusSnapshotsDTO objects that provide the actual metric values for the component, for each node. If the NiFi instance is not clustered, this value will be null.  # noqa: E501

        :param node_snapshots: The node_snapshots of this StatusHistoryDTO.  # noqa: E501
        :type: list[NodeStatusSnapshotsDTO]
        """

        self._node_snapshots = node_snapshots

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
        if not isinstance(other, StatusHistoryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

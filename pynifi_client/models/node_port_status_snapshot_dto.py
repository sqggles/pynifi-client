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

from pynifi_client.models.port_status_snapshot_dto import PortStatusSnapshotDTO  # noqa: F401,E501


class NodePortStatusSnapshotDTO(object):
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
        'node_id': 'str',
        'address': 'str',
        'api_port': 'int',
        'status_snapshot': 'PortStatusSnapshotDTO'
    }

    attribute_map = {
        'node_id': 'nodeId',
        'address': 'address',
        'api_port': 'apiPort',
        'status_snapshot': 'statusSnapshot'
    }

    def __init__(self, node_id=None, address=None, api_port=None, status_snapshot=None):  # noqa: E501
        """NodePortStatusSnapshotDTO - a model defined in Swagger"""  # noqa: E501

        self._node_id = None
        self._address = None
        self._api_port = None
        self._status_snapshot = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if address is not None:
            self.address = address
        if api_port is not None:
            self.api_port = api_port
        if status_snapshot is not None:
            self.status_snapshot = status_snapshot

    @property
    def node_id(self):
        """Gets the node_id of this NodePortStatusSnapshotDTO.  # noqa: E501

        The unique ID that identifies the node  # noqa: E501

        :return: The node_id of this NodePortStatusSnapshotDTO.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this NodePortStatusSnapshotDTO.

        The unique ID that identifies the node  # noqa: E501

        :param node_id: The node_id of this NodePortStatusSnapshotDTO.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def address(self):
        """Gets the address of this NodePortStatusSnapshotDTO.  # noqa: E501

        The API address of the node  # noqa: E501

        :return: The address of this NodePortStatusSnapshotDTO.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this NodePortStatusSnapshotDTO.

        The API address of the node  # noqa: E501

        :param address: The address of this NodePortStatusSnapshotDTO.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def api_port(self):
        """Gets the api_port of this NodePortStatusSnapshotDTO.  # noqa: E501

        The API port used to communicate with the node  # noqa: E501

        :return: The api_port of this NodePortStatusSnapshotDTO.  # noqa: E501
        :rtype: int
        """
        return self._api_port

    @api_port.setter
    def api_port(self, api_port):
        """Sets the api_port of this NodePortStatusSnapshotDTO.

        The API port used to communicate with the node  # noqa: E501

        :param api_port: The api_port of this NodePortStatusSnapshotDTO.  # noqa: E501
        :type: int
        """

        self._api_port = api_port

    @property
    def status_snapshot(self):
        """Gets the status_snapshot of this NodePortStatusSnapshotDTO.  # noqa: E501

        The port status snapshot from the node.  # noqa: E501

        :return: The status_snapshot of this NodePortStatusSnapshotDTO.  # noqa: E501
        :rtype: PortStatusSnapshotDTO
        """
        return self._status_snapshot

    @status_snapshot.setter
    def status_snapshot(self, status_snapshot):
        """Sets the status_snapshot of this NodePortStatusSnapshotDTO.

        The port status snapshot from the node.  # noqa: E501

        :param status_snapshot: The status_snapshot of this NodePortStatusSnapshotDTO.  # noqa: E501
        :type: PortStatusSnapshotDTO
        """

        self._status_snapshot = status_snapshot

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
        if not isinstance(other, NodePortStatusSnapshotDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

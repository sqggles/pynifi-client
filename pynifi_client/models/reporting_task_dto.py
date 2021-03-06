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

from pynifi_client.models.bundle_dto import BundleDTO  # noqa: F401,E501
from pynifi_client.models.position_dto import PositionDTO  # noqa: F401,E501
from pynifi_client.models.property_descriptor_dto import PropertyDescriptorDTO  # noqa: F401,E501


class ReportingTaskDTO(object):
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
        'name': 'str',
        'type': 'str',
        'bundle': 'BundleDTO',
        'state': 'str',
        'comments': 'str',
        'persists_state': 'bool',
        'restricted': 'bool',
        'deprecated': 'bool',
        'multiple_versions_available': 'bool',
        'scheduling_period': 'str',
        'scheduling_strategy': 'str',
        'default_scheduling_period': 'dict(str, str)',
        'properties': 'dict(str, str)',
        'descriptors': 'dict(str, PropertyDescriptorDTO)',
        'custom_ui_url': 'str',
        'annotation_data': 'str',
        'validation_errors': 'list[str]',
        'active_thread_count': 'int',
        'extension_missing': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'parent_group_id': 'parentGroupId',
        'position': 'position',
        'name': 'name',
        'type': 'type',
        'bundle': 'bundle',
        'state': 'state',
        'comments': 'comments',
        'persists_state': 'persistsState',
        'restricted': 'restricted',
        'deprecated': 'deprecated',
        'multiple_versions_available': 'multipleVersionsAvailable',
        'scheduling_period': 'schedulingPeriod',
        'scheduling_strategy': 'schedulingStrategy',
        'default_scheduling_period': 'defaultSchedulingPeriod',
        'properties': 'properties',
        'descriptors': 'descriptors',
        'custom_ui_url': 'customUiUrl',
        'annotation_data': 'annotationData',
        'validation_errors': 'validationErrors',
        'active_thread_count': 'activeThreadCount',
        'extension_missing': 'extensionMissing'
    }

    def __init__(self, id=None, parent_group_id=None, position=None, name=None, type=None, bundle=None, state=None, comments=None, persists_state=False, restricted=False, deprecated=False, multiple_versions_available=False, scheduling_period=None, scheduling_strategy=None, default_scheduling_period=None, properties=None, descriptors=None, custom_ui_url=None, annotation_data=None, validation_errors=None, active_thread_count=None, extension_missing=False):  # noqa: E501
        """ReportingTaskDTO - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._parent_group_id = None
        self._position = None
        self._name = None
        self._type = None
        self._bundle = None
        self._state = None
        self._comments = None
        self._persists_state = None
        self._restricted = None
        self._deprecated = None
        self._multiple_versions_available = None
        self._scheduling_period = None
        self._scheduling_strategy = None
        self._default_scheduling_period = None
        self._properties = None
        self._descriptors = None
        self._custom_ui_url = None
        self._annotation_data = None
        self._validation_errors = None
        self._active_thread_count = None
        self._extension_missing = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if parent_group_id is not None:
            self.parent_group_id = parent_group_id
        if position is not None:
            self.position = position
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if bundle is not None:
            self.bundle = bundle
        if state is not None:
            self.state = state
        if comments is not None:
            self.comments = comments
        if persists_state is not None:
            self.persists_state = persists_state
        if restricted is not None:
            self.restricted = restricted
        if deprecated is not None:
            self.deprecated = deprecated
        if multiple_versions_available is not None:
            self.multiple_versions_available = multiple_versions_available
        if scheduling_period is not None:
            self.scheduling_period = scheduling_period
        if scheduling_strategy is not None:
            self.scheduling_strategy = scheduling_strategy
        if default_scheduling_period is not None:
            self.default_scheduling_period = default_scheduling_period
        if properties is not None:
            self.properties = properties
        if descriptors is not None:
            self.descriptors = descriptors
        if custom_ui_url is not None:
            self.custom_ui_url = custom_ui_url
        if annotation_data is not None:
            self.annotation_data = annotation_data
        if validation_errors is not None:
            self.validation_errors = validation_errors
        if active_thread_count is not None:
            self.active_thread_count = active_thread_count
        if extension_missing is not None:
            self.extension_missing = extension_missing

    @property
    def id(self):
        """Gets the id of this ReportingTaskDTO.  # noqa: E501

        The id of the component.  # noqa: E501

        :return: The id of this ReportingTaskDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReportingTaskDTO.

        The id of the component.  # noqa: E501

        :param id: The id of this ReportingTaskDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def parent_group_id(self):
        """Gets the parent_group_id of this ReportingTaskDTO.  # noqa: E501

        The id of parent process group of this component if applicable.  # noqa: E501

        :return: The parent_group_id of this ReportingTaskDTO.  # noqa: E501
        :rtype: str
        """
        return self._parent_group_id

    @parent_group_id.setter
    def parent_group_id(self, parent_group_id):
        """Sets the parent_group_id of this ReportingTaskDTO.

        The id of parent process group of this component if applicable.  # noqa: E501

        :param parent_group_id: The parent_group_id of this ReportingTaskDTO.  # noqa: E501
        :type: str
        """

        self._parent_group_id = parent_group_id

    @property
    def position(self):
        """Gets the position of this ReportingTaskDTO.  # noqa: E501

        The position of this component in the UI if applicable.  # noqa: E501

        :return: The position of this ReportingTaskDTO.  # noqa: E501
        :rtype: PositionDTO
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this ReportingTaskDTO.

        The position of this component in the UI if applicable.  # noqa: E501

        :param position: The position of this ReportingTaskDTO.  # noqa: E501
        :type: PositionDTO
        """

        self._position = position

    @property
    def name(self):
        """Gets the name of this ReportingTaskDTO.  # noqa: E501

        The name of the reporting task.  # noqa: E501

        :return: The name of this ReportingTaskDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReportingTaskDTO.

        The name of the reporting task.  # noqa: E501

        :param name: The name of this ReportingTaskDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this ReportingTaskDTO.  # noqa: E501

        The fully qualified type of the reporting task.  # noqa: E501

        :return: The type of this ReportingTaskDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ReportingTaskDTO.

        The fully qualified type of the reporting task.  # noqa: E501

        :param type: The type of this ReportingTaskDTO.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def bundle(self):
        """Gets the bundle of this ReportingTaskDTO.  # noqa: E501

        The details of the artifact that bundled this processor type.  # noqa: E501

        :return: The bundle of this ReportingTaskDTO.  # noqa: E501
        :rtype: BundleDTO
        """
        return self._bundle

    @bundle.setter
    def bundle(self, bundle):
        """Sets the bundle of this ReportingTaskDTO.

        The details of the artifact that bundled this processor type.  # noqa: E501

        :param bundle: The bundle of this ReportingTaskDTO.  # noqa: E501
        :type: BundleDTO
        """

        self._bundle = bundle

    @property
    def state(self):
        """Gets the state of this ReportingTaskDTO.  # noqa: E501

        The state of the reporting task.  # noqa: E501

        :return: The state of this ReportingTaskDTO.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ReportingTaskDTO.

        The state of the reporting task.  # noqa: E501

        :param state: The state of this ReportingTaskDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["RUNNING", "STOPPED", "DISABLED"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def comments(self):
        """Gets the comments of this ReportingTaskDTO.  # noqa: E501

        The comments of the reporting task.  # noqa: E501

        :return: The comments of this ReportingTaskDTO.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this ReportingTaskDTO.

        The comments of the reporting task.  # noqa: E501

        :param comments: The comments of this ReportingTaskDTO.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def persists_state(self):
        """Gets the persists_state of this ReportingTaskDTO.  # noqa: E501

        Whether the reporting task persists state.  # noqa: E501

        :return: The persists_state of this ReportingTaskDTO.  # noqa: E501
        :rtype: bool
        """
        return self._persists_state

    @persists_state.setter
    def persists_state(self, persists_state):
        """Sets the persists_state of this ReportingTaskDTO.

        Whether the reporting task persists state.  # noqa: E501

        :param persists_state: The persists_state of this ReportingTaskDTO.  # noqa: E501
        :type: bool
        """

        self._persists_state = persists_state

    @property
    def restricted(self):
        """Gets the restricted of this ReportingTaskDTO.  # noqa: E501

        Whether the reporting task requires elevated privileges.  # noqa: E501

        :return: The restricted of this ReportingTaskDTO.  # noqa: E501
        :rtype: bool
        """
        return self._restricted

    @restricted.setter
    def restricted(self, restricted):
        """Sets the restricted of this ReportingTaskDTO.

        Whether the reporting task requires elevated privileges.  # noqa: E501

        :param restricted: The restricted of this ReportingTaskDTO.  # noqa: E501
        :type: bool
        """

        self._restricted = restricted

    @property
    def deprecated(self):
        """Gets the deprecated of this ReportingTaskDTO.  # noqa: E501

        Whether the reporting task has been deprecated.  # noqa: E501

        :return: The deprecated of this ReportingTaskDTO.  # noqa: E501
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """Sets the deprecated of this ReportingTaskDTO.

        Whether the reporting task has been deprecated.  # noqa: E501

        :param deprecated: The deprecated of this ReportingTaskDTO.  # noqa: E501
        :type: bool
        """

        self._deprecated = deprecated

    @property
    def multiple_versions_available(self):
        """Gets the multiple_versions_available of this ReportingTaskDTO.  # noqa: E501

        Whether the reporting task has multiple versions available.  # noqa: E501

        :return: The multiple_versions_available of this ReportingTaskDTO.  # noqa: E501
        :rtype: bool
        """
        return self._multiple_versions_available

    @multiple_versions_available.setter
    def multiple_versions_available(self, multiple_versions_available):
        """Sets the multiple_versions_available of this ReportingTaskDTO.

        Whether the reporting task has multiple versions available.  # noqa: E501

        :param multiple_versions_available: The multiple_versions_available of this ReportingTaskDTO.  # noqa: E501
        :type: bool
        """

        self._multiple_versions_available = multiple_versions_available

    @property
    def scheduling_period(self):
        """Gets the scheduling_period of this ReportingTaskDTO.  # noqa: E501

        The frequency with which to schedule the reporting task. The format of the value willd epend on the valud of the schedulingStrategy.  # noqa: E501

        :return: The scheduling_period of this ReportingTaskDTO.  # noqa: E501
        :rtype: str
        """
        return self._scheduling_period

    @scheduling_period.setter
    def scheduling_period(self, scheduling_period):
        """Sets the scheduling_period of this ReportingTaskDTO.

        The frequency with which to schedule the reporting task. The format of the value willd epend on the valud of the schedulingStrategy.  # noqa: E501

        :param scheduling_period: The scheduling_period of this ReportingTaskDTO.  # noqa: E501
        :type: str
        """

        self._scheduling_period = scheduling_period

    @property
    def scheduling_strategy(self):
        """Gets the scheduling_strategy of this ReportingTaskDTO.  # noqa: E501

        The scheduling strategy that determines how the schedulingPeriod value should be interpreted.  # noqa: E501

        :return: The scheduling_strategy of this ReportingTaskDTO.  # noqa: E501
        :rtype: str
        """
        return self._scheduling_strategy

    @scheduling_strategy.setter
    def scheduling_strategy(self, scheduling_strategy):
        """Sets the scheduling_strategy of this ReportingTaskDTO.

        The scheduling strategy that determines how the schedulingPeriod value should be interpreted.  # noqa: E501

        :param scheduling_strategy: The scheduling_strategy of this ReportingTaskDTO.  # noqa: E501
        :type: str
        """

        self._scheduling_strategy = scheduling_strategy

    @property
    def default_scheduling_period(self):
        """Gets the default_scheduling_period of this ReportingTaskDTO.  # noqa: E501

        The default scheduling period for the different scheduling strategies.  # noqa: E501

        :return: The default_scheduling_period of this ReportingTaskDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._default_scheduling_period

    @default_scheduling_period.setter
    def default_scheduling_period(self, default_scheduling_period):
        """Sets the default_scheduling_period of this ReportingTaskDTO.

        The default scheduling period for the different scheduling strategies.  # noqa: E501

        :param default_scheduling_period: The default_scheduling_period of this ReportingTaskDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._default_scheduling_period = default_scheduling_period

    @property
    def properties(self):
        """Gets the properties of this ReportingTaskDTO.  # noqa: E501

        The properties of the reporting task.  # noqa: E501

        :return: The properties of this ReportingTaskDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ReportingTaskDTO.

        The properties of the reporting task.  # noqa: E501

        :param properties: The properties of this ReportingTaskDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._properties = properties

    @property
    def descriptors(self):
        """Gets the descriptors of this ReportingTaskDTO.  # noqa: E501

        The descriptors for the reporting tasks properties.  # noqa: E501

        :return: The descriptors of this ReportingTaskDTO.  # noqa: E501
        :rtype: dict(str, PropertyDescriptorDTO)
        """
        return self._descriptors

    @descriptors.setter
    def descriptors(self, descriptors):
        """Sets the descriptors of this ReportingTaskDTO.

        The descriptors for the reporting tasks properties.  # noqa: E501

        :param descriptors: The descriptors of this ReportingTaskDTO.  # noqa: E501
        :type: dict(str, PropertyDescriptorDTO)
        """

        self._descriptors = descriptors

    @property
    def custom_ui_url(self):
        """Gets the custom_ui_url of this ReportingTaskDTO.  # noqa: E501

        The URL for the custom configuration UI for the reporting task.  # noqa: E501

        :return: The custom_ui_url of this ReportingTaskDTO.  # noqa: E501
        :rtype: str
        """
        return self._custom_ui_url

    @custom_ui_url.setter
    def custom_ui_url(self, custom_ui_url):
        """Sets the custom_ui_url of this ReportingTaskDTO.

        The URL for the custom configuration UI for the reporting task.  # noqa: E501

        :param custom_ui_url: The custom_ui_url of this ReportingTaskDTO.  # noqa: E501
        :type: str
        """

        self._custom_ui_url = custom_ui_url

    @property
    def annotation_data(self):
        """Gets the annotation_data of this ReportingTaskDTO.  # noqa: E501

        The annotation data for the repoting task. This is how the custom UI relays configuration to the reporting task.  # noqa: E501

        :return: The annotation_data of this ReportingTaskDTO.  # noqa: E501
        :rtype: str
        """
        return self._annotation_data

    @annotation_data.setter
    def annotation_data(self, annotation_data):
        """Sets the annotation_data of this ReportingTaskDTO.

        The annotation data for the repoting task. This is how the custom UI relays configuration to the reporting task.  # noqa: E501

        :param annotation_data: The annotation_data of this ReportingTaskDTO.  # noqa: E501
        :type: str
        """

        self._annotation_data = annotation_data

    @property
    def validation_errors(self):
        """Gets the validation_errors of this ReportingTaskDTO.  # noqa: E501

        Gets the validation errors from the reporting task. These validation errors represent the problems with the reporting task that must be resolved before it can be scheduled to run.  # noqa: E501

        :return: The validation_errors of this ReportingTaskDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this ReportingTaskDTO.

        Gets the validation errors from the reporting task. These validation errors represent the problems with the reporting task that must be resolved before it can be scheduled to run.  # noqa: E501

        :param validation_errors: The validation_errors of this ReportingTaskDTO.  # noqa: E501
        :type: list[str]
        """

        self._validation_errors = validation_errors

    @property
    def active_thread_count(self):
        """Gets the active_thread_count of this ReportingTaskDTO.  # noqa: E501

        The number of active threads for the reporting task.  # noqa: E501

        :return: The active_thread_count of this ReportingTaskDTO.  # noqa: E501
        :rtype: int
        """
        return self._active_thread_count

    @active_thread_count.setter
    def active_thread_count(self, active_thread_count):
        """Sets the active_thread_count of this ReportingTaskDTO.

        The number of active threads for the reporting task.  # noqa: E501

        :param active_thread_count: The active_thread_count of this ReportingTaskDTO.  # noqa: E501
        :type: int
        """

        self._active_thread_count = active_thread_count

    @property
    def extension_missing(self):
        """Gets the extension_missing of this ReportingTaskDTO.  # noqa: E501

        Whether the underlying extension is missing.  # noqa: E501

        :return: The extension_missing of this ReportingTaskDTO.  # noqa: E501
        :rtype: bool
        """
        return self._extension_missing

    @extension_missing.setter
    def extension_missing(self, extension_missing):
        """Sets the extension_missing of this ReportingTaskDTO.

        Whether the underlying extension is missing.  # noqa: E501

        :param extension_missing: The extension_missing of this ReportingTaskDTO.  # noqa: E501
        :type: bool
        """

        self._extension_missing = extension_missing

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
        if not isinstance(other, ReportingTaskDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

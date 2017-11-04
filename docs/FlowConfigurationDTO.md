# FlowConfigurationDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supports_managed_authorizer** | **bool** | Whether this NiFi supports a managed authorizer. Managed authorizers can visualize users, groups, and policies in the UI. | [optional] [default to False]
**supports_configurable_authorizer** | **bool** | Whether this NiFi supports a configurable authorizer. | [optional] [default to False]
**supports_configurable_users_and_groups** | **bool** | Whether this NiFi supports configurable users and groups. | [optional] [default to False]
**auto_refresh_interval_seconds** | **int** | The interval in seconds between the automatic NiFi refresh requests. | [optional] 
**current_time** | **str** | The current time on the system. | [optional] 
**time_offset** | **int** | The time offset of the system. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



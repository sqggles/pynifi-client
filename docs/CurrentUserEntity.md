# CurrentUserEntity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity** | **str** | The user identity being serialized. | [optional] 
**anonymous** | **bool** | Whether the current user is anonymous. | [optional] [default to False]
**provenance_permissions** | [**PermissionsDTO**](PermissionsDTO.md) | Permissions for querying provenance. | [optional] 
**counters_permissions** | [**PermissionsDTO**](PermissionsDTO.md) | Permissions for accessing counters. | [optional] 
**tenants_permissions** | [**PermissionsDTO**](PermissionsDTO.md) | Permissions for accessing tenants. | [optional] 
**controller_permissions** | [**PermissionsDTO**](PermissionsDTO.md) | Permissions for accessing the controller. | [optional] 
**policies_permissions** | [**PermissionsDTO**](PermissionsDTO.md) | Permissions for accessing the policies. | [optional] 
**system_permissions** | [**PermissionsDTO**](PermissionsDTO.md) | Permissions for accessing system. | [optional] 
**restricted_components_permissions** | [**PermissionsDTO**](PermissionsDTO.md) | Permissions for accessing restricted components. Note: the read permission are not used and will always be false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



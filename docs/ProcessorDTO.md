# ProcessorDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the component. | [optional] 
**parent_group_id** | **str** | The id of parent process group of this component if applicable. | [optional] 
**position** | [**PositionDTO**](PositionDTO.md) | The position of this component in the UI if applicable. | [optional] 
**name** | **str** | The name of the processor. | [optional] 
**type** | **str** | The type of the processor. | [optional] 
**bundle** | [**BundleDTO**](BundleDTO.md) | The details of the artifact that bundled this processor type. | [optional] 
**state** | **str** | The state of the processor | [optional] 
**style** | **dict(str, str)** | Styles for the processor (background-color : #eee). | [optional] 
**relationships** | [**list[RelationshipDTO]**](RelationshipDTO.md) | The available relationships that the processor currently supports. | [optional] 
**description** | **str** | The description of the processor. | [optional] 
**supports_parallel_processing** | **bool** | Whether the processor supports parallel processing. | [optional] [default to False]
**supports_event_driven** | **bool** | Whether the processor supports event driven scheduling. | [optional] [default to False]
**supports_batching** | **bool** | Whether the processor supports batching. This makes the run duration settings available. | [optional] [default to False]
**persists_state** | **bool** | Whether the processor persists state. | [optional] [default to False]
**restricted** | **bool** | Whether the processor requires elevated privileges. | [optional] [default to False]
**deprecated** | **bool** | Whether the processor has been deprecated. | [optional] [default to False]
**multiple_versions_available** | **bool** | Whether the processor has multiple versions available. | [optional] [default to False]
**input_requirement** | **str** | The input requirement for this processor. | [optional] 
**config** | [**ProcessorConfigDTO**](ProcessorConfigDTO.md) | The configuration details for the processor. These details will be included in a response if the verbose flag is included in a request. | [optional] 
**validation_errors** | **list[str]** | The validation errors for the processor. These validation errors represent the problems with the processor that must be resolved before it can be started. | [optional] 
**extension_missing** | **bool** | Whether the underlying extension is missing. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



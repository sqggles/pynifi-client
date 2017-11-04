# swagger_client.RemoteProcessGroupsApi

All URIs are relative to *http://localhost/nifi-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_remote_process_group**](RemoteProcessGroupsApi.md#get_remote_process_group) | **GET** /remote-process-groups/{id} | Gets a remote process group
[**remove_remote_process_group**](RemoteProcessGroupsApi.md#remove_remote_process_group) | **DELETE** /remote-process-groups/{id} | Deletes a remote process group
[**update_remote_process_group**](RemoteProcessGroupsApi.md#update_remote_process_group) | **PUT** /remote-process-groups/{id} | Updates a remote process group
[**update_remote_process_group_input_port**](RemoteProcessGroupsApi.md#update_remote_process_group_input_port) | **PUT** /remote-process-groups/{id}/input-ports/{port-id} | Updates a remote port
[**update_remote_process_group_output_port**](RemoteProcessGroupsApi.md#update_remote_process_group_output_port) | **PUT** /remote-process-groups/{id}/output-ports/{port-id} | Updates a remote port


# **get_remote_process_group**
> RemoteProcessGroupEntity get_remote_process_group(id)

Gets a remote process group



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RemoteProcessGroupsApi()
id = 'id_example' # str | The remote process group id.

try:
    # Gets a remote process group
    api_response = api_instance.get_remote_process_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteProcessGroupsApi->get_remote_process_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The remote process group id. | 

### Return type

[**RemoteProcessGroupEntity**](RemoteProcessGroupEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_remote_process_group**
> RemoteProcessGroupEntity remove_remote_process_group(id, version=version, client_id=client_id)

Deletes a remote process group



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RemoteProcessGroupsApi()
id = 'id_example' # str | The remote process group id.
version = 'version_example' # str | The revision is used to verify the client is working with the latest version of the flow. (optional)
client_id = 'client_id_example' # str | If the client id is not specified, new one will be generated. This value (whether specified or generated) is included in the response. (optional)

try:
    # Deletes a remote process group
    api_response = api_instance.remove_remote_process_group(id, version=version, client_id=client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteProcessGroupsApi->remove_remote_process_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The remote process group id. | 
 **version** | **str**| The revision is used to verify the client is working with the latest version of the flow. | [optional] 
 **client_id** | **str**| If the client id is not specified, new one will be generated. This value (whether specified or generated) is included in the response. | [optional] 

### Return type

[**RemoteProcessGroupEntity**](RemoteProcessGroupEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_remote_process_group**
> RemoteProcessGroupEntity update_remote_process_group(id, body)

Updates a remote process group



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RemoteProcessGroupsApi()
id = 'id_example' # str | The remote process group id.
body = swagger_client.RemoteProcessGroupEntity() # RemoteProcessGroupEntity | The remote process group.

try:
    # Updates a remote process group
    api_response = api_instance.update_remote_process_group(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteProcessGroupsApi->update_remote_process_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The remote process group id. | 
 **body** | [**RemoteProcessGroupEntity**](RemoteProcessGroupEntity.md)| The remote process group. | 

### Return type

[**RemoteProcessGroupEntity**](RemoteProcessGroupEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_remote_process_group_input_port**
> RemoteProcessGroupPortEntity update_remote_process_group_input_port(id, port_id, body)

Updates a remote port

Note: This endpoint is subject to change as NiFi and it's REST API evolve.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RemoteProcessGroupsApi()
id = 'id_example' # str | The remote process group id.
port_id = 'port_id_example' # str | The remote process group port id.
body = swagger_client.RemoteProcessGroupPortEntity() # RemoteProcessGroupPortEntity | The remote process group port.

try:
    # Updates a remote port
    api_response = api_instance.update_remote_process_group_input_port(id, port_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteProcessGroupsApi->update_remote_process_group_input_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The remote process group id. | 
 **port_id** | **str**| The remote process group port id. | 
 **body** | [**RemoteProcessGroupPortEntity**](RemoteProcessGroupPortEntity.md)| The remote process group port. | 

### Return type

[**RemoteProcessGroupPortEntity**](RemoteProcessGroupPortEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_remote_process_group_output_port**
> RemoteProcessGroupPortEntity update_remote_process_group_output_port(id, port_id, body)

Updates a remote port

Note: This endpoint is subject to change as NiFi and it's REST API evolve.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RemoteProcessGroupsApi()
id = 'id_example' # str | The remote process group id.
port_id = 'port_id_example' # str | The remote process group port id.
body = swagger_client.RemoteProcessGroupPortEntity() # RemoteProcessGroupPortEntity | The remote process group port.

try:
    # Updates a remote port
    api_response = api_instance.update_remote_process_group_output_port(id, port_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteProcessGroupsApi->update_remote_process_group_output_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The remote process group id. | 
 **port_id** | **str**| The remote process group port id. | 
 **body** | [**RemoteProcessGroupPortEntity**](RemoteProcessGroupPortEntity.md)| The remote process group port. | 

### Return type

[**RemoteProcessGroupPortEntity**](RemoteProcessGroupPortEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


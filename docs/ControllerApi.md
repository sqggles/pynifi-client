# swagger_client.ControllerApi

All URIs are relative to *http://localhost/nifi-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bulletin**](ControllerApi.md#create_bulletin) | **POST** /controller/bulletin | Creates a new bulletin
[**create_controller_service**](ControllerApi.md#create_controller_service) | **POST** /controller/controller-services | Creates a new controller service
[**create_reporting_task**](ControllerApi.md#create_reporting_task) | **POST** /controller/reporting-tasks | Creates a new reporting task
[**delete_history**](ControllerApi.md#delete_history) | **DELETE** /controller/history | Purges history
[**delete_node**](ControllerApi.md#delete_node) | **DELETE** /controller/cluster/nodes/{id} | Removes a node from the cluster
[**get_cluster**](ControllerApi.md#get_cluster) | **GET** /controller/cluster | Gets the contents of the cluster
[**get_controller_config**](ControllerApi.md#get_controller_config) | **GET** /controller/config | Retrieves the configuration for this NiFi Controller
[**get_node**](ControllerApi.md#get_node) | **GET** /controller/cluster/nodes/{id} | Gets a node in the cluster
[**update_controller_config**](ControllerApi.md#update_controller_config) | **PUT** /controller/config | Retrieves the configuration for this NiFi
[**update_node**](ControllerApi.md#update_node) | **PUT** /controller/cluster/nodes/{id} | Updates a node in the cluster


# **create_bulletin**
> BulletinEntity create_bulletin(body)

Creates a new bulletin



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ControllerApi()
body = swagger_client.BulletinEntity() # BulletinEntity | The reporting task configuration details.

try:
    # Creates a new bulletin
    api_response = api_instance.create_bulletin(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ControllerApi->create_bulletin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulletinEntity**](BulletinEntity.md)| The reporting task configuration details. | 

### Return type

[**BulletinEntity**](BulletinEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_controller_service**
> ControllerServiceEntity create_controller_service(body)

Creates a new controller service



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ControllerApi()
body = swagger_client.ControllerServiceEntity() # ControllerServiceEntity | The controller service configuration details.

try:
    # Creates a new controller service
    api_response = api_instance.create_controller_service(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ControllerApi->create_controller_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ControllerServiceEntity**](ControllerServiceEntity.md)| The controller service configuration details. | 

### Return type

[**ControllerServiceEntity**](ControllerServiceEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_reporting_task**
> ReportingTaskEntity create_reporting_task(body)

Creates a new reporting task



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ControllerApi()
body = swagger_client.ReportingTaskEntity() # ReportingTaskEntity | The reporting task configuration details.

try:
    # Creates a new reporting task
    api_response = api_instance.create_reporting_task(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ControllerApi->create_reporting_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportingTaskEntity**](ReportingTaskEntity.md)| The reporting task configuration details. | 

### Return type

[**ReportingTaskEntity**](ReportingTaskEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_history**
> HistoryEntity delete_history(end_date)

Purges history



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ControllerApi()
end_date = 'end_date_example' # str | Purge actions before this date/time.

try:
    # Purges history
    api_response = api_instance.delete_history(end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ControllerApi->delete_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **str**| Purge actions before this date/time. | 

### Return type

[**HistoryEntity**](HistoryEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node**
> NodeEntity delete_node(id)

Removes a node from the cluster



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ControllerApi()
id = 'id_example' # str | The node id.

try:
    # Removes a node from the cluster
    api_response = api_instance.delete_node(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ControllerApi->delete_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The node id. | 

### Return type

[**NodeEntity**](NodeEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster**
> ClusterEntity get_cluster()

Gets the contents of the cluster

Returns the contents of the cluster including all nodes and their status.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ControllerApi()

try:
    # Gets the contents of the cluster
    api_response = api_instance.get_cluster()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ControllerApi->get_cluster: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterEntity**](ClusterEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_controller_config**
> ControllerConfigurationEntity get_controller_config()

Retrieves the configuration for this NiFi Controller



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ControllerApi()

try:
    # Retrieves the configuration for this NiFi Controller
    api_response = api_instance.get_controller_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ControllerApi->get_controller_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ControllerConfigurationEntity**](ControllerConfigurationEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node**
> NodeEntity get_node(id)

Gets a node in the cluster



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ControllerApi()
id = 'id_example' # str | The node id.

try:
    # Gets a node in the cluster
    api_response = api_instance.get_node(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ControllerApi->get_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The node id. | 

### Return type

[**NodeEntity**](NodeEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_controller_config**
> ControllerConfigurationEntity update_controller_config(body)

Retrieves the configuration for this NiFi



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ControllerApi()
body = swagger_client.ControllerConfigurationEntity() # ControllerConfigurationEntity | The controller configuration.

try:
    # Retrieves the configuration for this NiFi
    api_response = api_instance.update_controller_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ControllerApi->update_controller_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ControllerConfigurationEntity**](ControllerConfigurationEntity.md)| The controller configuration. | 

### Return type

[**ControllerConfigurationEntity**](ControllerConfigurationEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node**
> NodeEntity update_node(id, body)

Updates a node in the cluster



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ControllerApi()
id = 'id_example' # str | The node id.
body = swagger_client.NodeEntity() # NodeEntity | The node configuration. The only configuration that will be honored at this endpoint is the status.

try:
    # Updates a node in the cluster
    api_response = api_instance.update_node(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ControllerApi->update_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The node id. | 
 **body** | [**NodeEntity**](NodeEntity.md)| The node configuration. The only configuration that will be honored at this endpoint is the status. | 

### Return type

[**NodeEntity**](NodeEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


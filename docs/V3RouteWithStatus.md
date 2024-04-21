# V3RouteWithStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**route_service_status** | [**V3RouteServiceStatus**](V3RouteServiceStatus.md) |  | [optional] 
**route_type** | **int** | Transport mode identifier | [optional] 
**route_id** | **int** | Route identifier | [optional] 
**route_name** | **str** | Name of route | [optional] 
**route_number** | **str** | Route number presented to public (nb. not route_id) | [optional] 
**route_gtfs_id** | **str** | GTFS Identifer of the route | [optional] 
**geopath** | **List[object]** | GeoPath of the route | [optional] 

## Example

```python
from openapi_client.models.v3_route_with_status import V3RouteWithStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V3RouteWithStatus from a JSON string
v3_route_with_status_instance = V3RouteWithStatus.from_json(json)
# print the JSON string representation of the object
print(V3RouteWithStatus.to_json())

# convert the object into a dict
v3_route_with_status_dict = v3_route_with_status_instance.to_dict()
# create an instance of V3RouteWithStatus from a dict
v3_route_with_status_from_dict = V3RouteWithStatus.from_dict(v3_route_with_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



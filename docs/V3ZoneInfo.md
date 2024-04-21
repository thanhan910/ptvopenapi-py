# V3ZoneInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_zone** | **int** |  | [optional] 
**max_zone** | **int** |  | [optional] 
**unique_zones** | **List[int]** |  | [optional] 

## Example

```python
from openapi_client.models.v3_zone_info import V3ZoneInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V3ZoneInfo from a JSON string
v3_zone_info_instance = V3ZoneInfo.from_json(json)
# print the JSON string representation of the object
print(V3ZoneInfo.to_json())

# convert the object into a dict
v3_zone_info_dict = v3_zone_info_instance.to_dict()
# create an instance of V3ZoneInfo from a dict
v3_zone_info_from_dict = V3ZoneInfo.from_dict(v3_zone_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



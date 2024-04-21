# V3FareEstimateResultStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.v3_fare_estimate_result_status import V3FareEstimateResultStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V3FareEstimateResultStatus from a JSON string
v3_fare_estimate_result_status_instance = V3FareEstimateResultStatus.from_json(json)
# print the JSON string representation of the object
print(V3FareEstimateResultStatus.to_json())

# convert the object into a dict
v3_fare_estimate_result_status_dict = v3_fare_estimate_result_status_instance.to_dict()
# create an instance of V3FareEstimateResultStatus from a dict
v3_fare_estimate_result_status_from_dict = V3FareEstimateResultStatus.from_dict(v3_fare_estimate_result_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



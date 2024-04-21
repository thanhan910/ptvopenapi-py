# V3FareEstimateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fare_estimate_result_status** | [**V3FareEstimateResultStatus**](V3FareEstimateResultStatus.md) |  | [optional] 
**fare_estimate_result** | [**V3FareEstimateResult**](V3FareEstimateResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.v3_fare_estimate_response import V3FareEstimateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V3FareEstimateResponse from a JSON string
v3_fare_estimate_response_instance = V3FareEstimateResponse.from_json(json)
# print the JSON string representation of the object
print(V3FareEstimateResponse.to_json())

# convert the object into a dict
v3_fare_estimate_response_dict = v3_fare_estimate_response_instance.to_dict()
# create an instance of V3FareEstimateResponse from a dict
v3_fare_estimate_response_from_dict = V3FareEstimateResponse.from_dict(v3_fare_estimate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



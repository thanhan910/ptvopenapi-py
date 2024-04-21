# V3FareEstimateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_early_bird** | **bool** |  | [optional] 
**is_journey_in_free_tram_zone** | **bool** |  | [optional] 
**is_this_weekend_journey** | **bool** |  | [optional] 
**zone_info** | [**V3ZoneInfo**](V3ZoneInfo.md) |  | [optional] 
**passenger_fares** | [**List[V3PassengerFare]**](V3PassengerFare.md) |  | [optional] 

## Example

```python
from openapi_client.models.v3_fare_estimate_result import V3FareEstimateResult

# TODO update the JSON string below
json = "{}"
# create an instance of V3FareEstimateResult from a JSON string
v3_fare_estimate_result_instance = V3FareEstimateResult.from_json(json)
# print the JSON string representation of the object
print(V3FareEstimateResult.to_json())

# convert the object into a dict
v3_fare_estimate_result_dict = v3_fare_estimate_result_instance.to_dict()
# create an instance of V3FareEstimateResult from a dict
v3_fare_estimate_result_from_dict = V3FareEstimateResult.from_dict(v3_fare_estimate_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



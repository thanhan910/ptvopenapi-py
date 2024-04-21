# V3PassengerFare


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passenger_type** | **str** |  | [optional] 
**fare2_hour_peak** | **float** |  | [optional] 
**fare2_hour_off_peak** | **float** |  | [optional] 
**fare_daily_peak** | **float** |  | [optional] 
**fare_daily_off_peak** | **float** |  | [optional] 
**pass7_days** | **float** |  | [optional] 
**pass28_to69_day_per_day** | **float** |  | [optional] 
**pass70_plus_day_per_day** | **float** |  | [optional] 
**weekend_cap** | **float** |  | [optional] 
**holiday_cap** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.v3_passenger_fare import V3PassengerFare

# TODO update the JSON string below
json = "{}"
# create an instance of V3PassengerFare from a JSON string
v3_passenger_fare_instance = V3PassengerFare.from_json(json)
# print the JSON string representation of the object
print(V3PassengerFare.to_json())

# convert the object into a dict
v3_passenger_fare_dict = v3_passenger_fare_instance.to_dict()
# create an instance of V3PassengerFare from a dict
v3_passenger_fare_from_dict = V3PassengerFare.from_dict(v3_passenger_fare_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



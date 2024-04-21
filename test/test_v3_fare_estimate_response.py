# coding: utf-8

"""
    PTV Timetable API - Version 3

    The PTV Timetable API provides direct access to Public Transport Victoria's public transport timetable data.    The API returns scheduled timetable, route and stop data for all metropolitan and regional train, tram and bus services in Victoria, including Night Network(Night Train and Night Tram data are included in metropolitan train and tram services data, respectively, whereas Night Bus is a separate route type).    The API also returns real-time data for metropolitan train, tram and bus services (where this data is made available to PTV), as well as disruption information, stop facility information, and access to myki ticket outlet data.    This Swagger is for Version 3 of the PTV Timetable API. By using this documentation you agree to comply with the licence and terms of service.    Train timetable data is updated daily, while the remaining data is updated weekly, taking into account any planned timetable changes (for example, due to holidays or planned disruptions). The PTV timetable API is the same API used by PTV for its apps. To access the most up to date data PTV has (including real-time data) you must use the API dynamically.    You can access the PTV Timetable API through a HTTP or HTTPS interface, as follows:        base URL / version number / API name / query string  The base URL is either:    *  http://timetableapi.ptv.vic.gov.au  or    *  https://timetableapi.ptv.vic.gov.au    The Swagger JSON file is available at http://timetableapi.ptv.vic.gov.au/swagger/docs/v3    Frequently asked questions are available on the PTV website at http://ptv.vic.gov.au/apifaq    Links to the following information are also provided on the PTV website at http://ptv.vic.gov.au/ptv-timetable-api/  * How to register for an API key and calculate a signature  * PTV Timetable API V2 to V3 Migration Guide  * PTV Timetable API Data Quality Statement    All information about how to use the API is in this documentation. PTV cannot provide technical support for the API.  

    The version of the OpenAPI document: v3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.v3_fare_estimate_response import V3FareEstimateResponse

class TestV3FareEstimateResponse(unittest.TestCase):
    """V3FareEstimateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V3FareEstimateResponse:
        """Test V3FareEstimateResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V3FareEstimateResponse`
        """
        model = V3FareEstimateResponse()
        if include_optional:
            return V3FareEstimateResponse(
                fare_estimate_result_status = openapi_client.models.v3/fare_estimate_result_status.V3.FareEstimateResultStatus(
                    status_code = 56, 
                    message = '', ),
                fare_estimate_result = openapi_client.models.v3/fare_estimate_result.V3.FareEstimateResult(
                    is_early_bird = True, 
                    is_journey_in_free_tram_zone = True, 
                    is_this_weekend_journey = True, 
                    zone_info = openapi_client.models.v3/zone_info.V3.ZoneInfo(
                        min_zone = 56, 
                        max_zone = 56, 
                        unique_zones = [
                            56
                            ], ), 
                    passenger_fares = [
                        openapi_client.models.v3/passenger_fare.V3.PassengerFare(
                            passenger_type = '', 
                            fare2_hour_peak = 1.337, 
                            fare2_hour_off_peak = 1.337, 
                            fare_daily_peak = 1.337, 
                            fare_daily_off_peak = 1.337, 
                            pass7_days = 1.337, 
                            pass28_to69_day_per_day = 1.337, 
                            pass70_plus_day_per_day = 1.337, 
                            weekend_cap = 1.337, 
                            holiday_cap = 1.337, )
                        ], )
            )
        else:
            return V3FareEstimateResponse(
        )
        """

    def testV3FareEstimateResponse(self):
        """Test V3FareEstimateResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

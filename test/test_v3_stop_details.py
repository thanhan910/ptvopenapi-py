# coding: utf-8

"""
    PTV Timetable API - Version 3

    The PTV Timetable API provides direct access to Public Transport Victoria's public transport timetable data.    The API returns scheduled timetable, route and stop data for all metropolitan and regional train, tram and bus services in Victoria, including Night Network(Night Train and Night Tram data are included in metropolitan train and tram services data, respectively, whereas Night Bus is a separate route type).    The API also returns real-time data for metropolitan train, tram and bus services (where this data is made available to PTV), as well as disruption information, stop facility information, and access to myki ticket outlet data.    This Swagger is for Version 3 of the PTV Timetable API. By using this documentation you agree to comply with the licence and terms of service.    Train timetable data is updated daily, while the remaining data is updated weekly, taking into account any planned timetable changes (for example, due to holidays or planned disruptions). The PTV timetable API is the same API used by PTV for its apps. To access the most up to date data PTV has (including real-time data) you must use the API dynamically.    You can access the PTV Timetable API through a HTTP or HTTPS interface, as follows:        base URL / version number / API name / query string  The base URL is either:    *  http://timetableapi.ptv.vic.gov.au  or    *  https://timetableapi.ptv.vic.gov.au    The Swagger JSON file is available at http://timetableapi.ptv.vic.gov.au/swagger/docs/v3    Frequently asked questions are available on the PTV website at http://ptv.vic.gov.au/apifaq    Links to the following information are also provided on the PTV website at http://ptv.vic.gov.au/ptv-timetable-api/  * How to register for an API key and calculate a signature  * PTV Timetable API V2 to V3 Migration Guide  * PTV Timetable API Data Quality Statement    All information about how to use the API is in this documentation. PTV cannot provide technical support for the API.  

    The version of the OpenAPI document: v3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.v3_stop_details import V3StopDetails

class TestV3StopDetails(unittest.TestCase):
    """V3StopDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V3StopDetails:
        """Test V3StopDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V3StopDetails`
        """
        model = V3StopDetails()
        if include_optional:
            return V3StopDetails(
                disruption_ids = [
                    56
                    ],
                station_type = '',
                station_description = '',
                route_type = 56,
                stop_location = openapi_client.models.v3/stop_location.V3.StopLocation(
                    gps = openapi_client.models.v3/stop_gps.V3.StopGps(
                        latitude = 1.337, 
                        longitude = 1.337, ), ),
                stop_amenities = openapi_client.models.v3/stop_amenity_details.V3.StopAmenityDetails(
                    toilet = True, 
                    taxi_rank = True, 
                    car_parking = '', 
                    cctv = True, ),
                stop_accessibility = openapi_client.models.v3/stop_accessibility.V3.StopAccessibility(
                    lighting = True, 
                    platform_number = 56, 
                    audio_customer_information = True, 
                    escalator = True, 
                    hearing_loop = True, 
                    lift = True, 
                    stairs = True, 
                    stop_accessible = True, 
                    tactile_ground_surface_indicator = True, 
                    waiting_room = True, 
                    wheelchair = openapi_client.models.v3/stop_accessibility_wheelchair.V3.StopAccessibilityWheelchair(
                        accessible_ramp = True, 
                        parking = True, 
                        telephone = True, 
                        toilet = True, 
                        low_ticket_counter = True, 
                        manouvering = True, 
                        raised_platform = True, 
                        ramp = True, 
                        secondary_path = True, 
                        raised_platform_shelther = True, 
                        steep_ramp = True, ), ),
                stop_staffing = openapi_client.models.v3/stop_staffing.V3.StopStaffing(
                    fri_am_from = '', 
                    fri_am_to = '', 
                    fri_pm_from = '', 
                    fri_pm_to = '', 
                    mon_am_from = '', 
                    mon_am_to = '', 
                    mon_pm_from = '', 
                    mon_pm_to = '', 
                    ph_additional_text = '', 
                    ph_from = '', 
                    ph_to = '', 
                    sat_am_from = '', 
                    sat_am_to = '', 
                    sat_pm_from = '', 
                    sat_pm_to = '', 
                    sun_am_from = '', 
                    sun_am_to = '', 
                    sun_pm_from = '', 
                    sun_pm_to = '', 
                    thu_am_from = '', 
                    thu_am_to = '', 
                    thu_pm_from = '', 
                    thu_pm_to = '', 
                    tue_am_from = '', 
                    tue_am_to = '', 
                    tue_pm_from = '', 
                    tue_pm_to = '', 
                    wed_am_from = '', 
                    wed_am_to = '', 
                    wed_pm_from = '', 
                    wed_pm_to = '', ),
                routes = [
                    None
                    ],
                stop_id = 56,
                stop_name = '',
                stop_landmark = ''
            )
        else:
            return V3StopDetails(
        )
        """

    def testV3StopDetails(self):
        """Test V3StopDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
# coding: utf-8

"""
    PTV Timetable API - Version 3

    The PTV Timetable API provides direct access to Public Transport Victoria's public transport timetable data.    The API returns scheduled timetable, route and stop data for all metropolitan and regional train, tram and bus services in Victoria, including Night Network(Night Train and Night Tram data are included in metropolitan train and tram services data, respectively, whereas Night Bus is a separate route type).    The API also returns real-time data for metropolitan train, tram and bus services (where this data is made available to PTV), as well as disruption information, stop facility information, and access to myki ticket outlet data.    This Swagger is for Version 3 of the PTV Timetable API. By using this documentation you agree to comply with the licence and terms of service.    Train timetable data is updated daily, while the remaining data is updated weekly, taking into account any planned timetable changes (for example, due to holidays or planned disruptions). The PTV timetable API is the same API used by PTV for its apps. To access the most up to date data PTV has (including real-time data) you must use the API dynamically.    You can access the PTV Timetable API through a HTTP or HTTPS interface, as follows:        base URL / version number / API name / query string  The base URL is either:    *  http://timetableapi.ptv.vic.gov.au  or    *  https://timetableapi.ptv.vic.gov.au    The Swagger JSON file is available at http://timetableapi.ptv.vic.gov.au/swagger/docs/v3    Frequently asked questions are available on the PTV website at http://ptv.vic.gov.au/apifaq    Links to the following information are also provided on the PTV website at http://ptv.vic.gov.au/ptv-timetable-api/  * How to register for an API key and calculate a signature  * PTV Timetable API V2 to V3 Migration Guide  * PTV Timetable API Data Quality Statement    All information about how to use the API is in this documentation. PTV cannot provide technical support for the API.  

    The version of the OpenAPI document: v3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from datetime import datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from openapi_client.models.v3_stopping_pattern import V3StoppingPattern

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class PatternsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def patterns_get_pattern_by_run(
        self,
        run_ref: Annotated[StrictStr, Field(description="The run_ref is the identifier of a run as returned by the departures/* and runs/* endpoints. WARNING, run_id is deprecated. Use run_ref instead.")],
        route_type: Annotated[StrictInt, Field(description="Number identifying transport mode; values returned via RouteTypes API")],
        expand: Annotated[List[StrictStr], Field(description="List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor and None. Default is Disruption. Run must be expanded to receive VehiclePosition and VehicleDescriptor information.")],
        stop_id: Annotated[Optional[StrictInt], Field(description="Filter by stop_id; values returned by Stops API")] = None,
        date_utc: Annotated[Optional[datetime], Field(description="Filter by the date and time of the request (ISO 8601 UTC format)")] = None,
        include_skipped_stops: Annotated[Optional[StrictBool], Field(description="Include any skipped stops in a stopping pattern. Defaults to false.")] = None,
        include_geopath: Annotated[Optional[StrictBool], Field(description="Indicates if geopath data will be returned (default = false)")] = None,
        token: Annotated[Optional[StrictStr], Field(description="Please ignore")] = None,
        devid: Annotated[Optional[StrictStr], Field(description="Your developer id")] = None,
        signature: Annotated[Optional[StrictStr], Field(description="Authentication signature for request")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> V3StoppingPattern:
        """View the stopping pattern for a specific trip/service run


        :param run_ref: The run_ref is the identifier of a run as returned by the departures/* and runs/* endpoints. WARNING, run_id is deprecated. Use run_ref instead. (required)
        :type run_ref: str
        :param route_type: Number identifying transport mode; values returned via RouteTypes API (required)
        :type route_type: int
        :param expand: List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor and None. Default is Disruption. Run must be expanded to receive VehiclePosition and VehicleDescriptor information. (required)
        :type expand: List[str]
        :param stop_id: Filter by stop_id; values returned by Stops API
        :type stop_id: int
        :param date_utc: Filter by the date and time of the request (ISO 8601 UTC format)
        :type date_utc: datetime
        :param include_skipped_stops: Include any skipped stops in a stopping pattern. Defaults to false.
        :type include_skipped_stops: bool
        :param include_geopath: Indicates if geopath data will be returned (default = false)
        :type include_geopath: bool
        :param token: Please ignore
        :type token: str
        :param devid: Your developer id
        :type devid: str
        :param signature: Authentication signature for request
        :type signature: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._patterns_get_pattern_by_run_serialize(
            run_ref=run_ref,
            route_type=route_type,
            expand=expand,
            stop_id=stop_id,
            date_utc=date_utc,
            include_skipped_stops=include_skipped_stops,
            include_geopath=include_geopath,
            token=token,
            devid=devid,
            signature=signature,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "V3StoppingPattern",
            '400': "V3ErrorResponse",
            '403': "V3ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def patterns_get_pattern_by_run_with_http_info(
        self,
        run_ref: Annotated[StrictStr, Field(description="The run_ref is the identifier of a run as returned by the departures/* and runs/* endpoints. WARNING, run_id is deprecated. Use run_ref instead.")],
        route_type: Annotated[StrictInt, Field(description="Number identifying transport mode; values returned via RouteTypes API")],
        expand: Annotated[List[StrictStr], Field(description="List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor and None. Default is Disruption. Run must be expanded to receive VehiclePosition and VehicleDescriptor information.")],
        stop_id: Annotated[Optional[StrictInt], Field(description="Filter by stop_id; values returned by Stops API")] = None,
        date_utc: Annotated[Optional[datetime], Field(description="Filter by the date and time of the request (ISO 8601 UTC format)")] = None,
        include_skipped_stops: Annotated[Optional[StrictBool], Field(description="Include any skipped stops in a stopping pattern. Defaults to false.")] = None,
        include_geopath: Annotated[Optional[StrictBool], Field(description="Indicates if geopath data will be returned (default = false)")] = None,
        token: Annotated[Optional[StrictStr], Field(description="Please ignore")] = None,
        devid: Annotated[Optional[StrictStr], Field(description="Your developer id")] = None,
        signature: Annotated[Optional[StrictStr], Field(description="Authentication signature for request")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[V3StoppingPattern]:
        """View the stopping pattern for a specific trip/service run


        :param run_ref: The run_ref is the identifier of a run as returned by the departures/* and runs/* endpoints. WARNING, run_id is deprecated. Use run_ref instead. (required)
        :type run_ref: str
        :param route_type: Number identifying transport mode; values returned via RouteTypes API (required)
        :type route_type: int
        :param expand: List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor and None. Default is Disruption. Run must be expanded to receive VehiclePosition and VehicleDescriptor information. (required)
        :type expand: List[str]
        :param stop_id: Filter by stop_id; values returned by Stops API
        :type stop_id: int
        :param date_utc: Filter by the date and time of the request (ISO 8601 UTC format)
        :type date_utc: datetime
        :param include_skipped_stops: Include any skipped stops in a stopping pattern. Defaults to false.
        :type include_skipped_stops: bool
        :param include_geopath: Indicates if geopath data will be returned (default = false)
        :type include_geopath: bool
        :param token: Please ignore
        :type token: str
        :param devid: Your developer id
        :type devid: str
        :param signature: Authentication signature for request
        :type signature: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._patterns_get_pattern_by_run_serialize(
            run_ref=run_ref,
            route_type=route_type,
            expand=expand,
            stop_id=stop_id,
            date_utc=date_utc,
            include_skipped_stops=include_skipped_stops,
            include_geopath=include_geopath,
            token=token,
            devid=devid,
            signature=signature,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "V3StoppingPattern",
            '400': "V3ErrorResponse",
            '403': "V3ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def patterns_get_pattern_by_run_without_preload_content(
        self,
        run_ref: Annotated[StrictStr, Field(description="The run_ref is the identifier of a run as returned by the departures/* and runs/* endpoints. WARNING, run_id is deprecated. Use run_ref instead.")],
        route_type: Annotated[StrictInt, Field(description="Number identifying transport mode; values returned via RouteTypes API")],
        expand: Annotated[List[StrictStr], Field(description="List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor and None. Default is Disruption. Run must be expanded to receive VehiclePosition and VehicleDescriptor information.")],
        stop_id: Annotated[Optional[StrictInt], Field(description="Filter by stop_id; values returned by Stops API")] = None,
        date_utc: Annotated[Optional[datetime], Field(description="Filter by the date and time of the request (ISO 8601 UTC format)")] = None,
        include_skipped_stops: Annotated[Optional[StrictBool], Field(description="Include any skipped stops in a stopping pattern. Defaults to false.")] = None,
        include_geopath: Annotated[Optional[StrictBool], Field(description="Indicates if geopath data will be returned (default = false)")] = None,
        token: Annotated[Optional[StrictStr], Field(description="Please ignore")] = None,
        devid: Annotated[Optional[StrictStr], Field(description="Your developer id")] = None,
        signature: Annotated[Optional[StrictStr], Field(description="Authentication signature for request")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """View the stopping pattern for a specific trip/service run


        :param run_ref: The run_ref is the identifier of a run as returned by the departures/* and runs/* endpoints. WARNING, run_id is deprecated. Use run_ref instead. (required)
        :type run_ref: str
        :param route_type: Number identifying transport mode; values returned via RouteTypes API (required)
        :type route_type: int
        :param expand: List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor and None. Default is Disruption. Run must be expanded to receive VehiclePosition and VehicleDescriptor information. (required)
        :type expand: List[str]
        :param stop_id: Filter by stop_id; values returned by Stops API
        :type stop_id: int
        :param date_utc: Filter by the date and time of the request (ISO 8601 UTC format)
        :type date_utc: datetime
        :param include_skipped_stops: Include any skipped stops in a stopping pattern. Defaults to false.
        :type include_skipped_stops: bool
        :param include_geopath: Indicates if geopath data will be returned (default = false)
        :type include_geopath: bool
        :param token: Please ignore
        :type token: str
        :param devid: Your developer id
        :type devid: str
        :param signature: Authentication signature for request
        :type signature: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._patterns_get_pattern_by_run_serialize(
            run_ref=run_ref,
            route_type=route_type,
            expand=expand,
            stop_id=stop_id,
            date_utc=date_utc,
            include_skipped_stops=include_skipped_stops,
            include_geopath=include_geopath,
            token=token,
            devid=devid,
            signature=signature,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "V3StoppingPattern",
            '400': "V3ErrorResponse",
            '403': "V3ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _patterns_get_pattern_by_run_serialize(
        self,
        run_ref,
        route_type,
        expand,
        stop_id,
        date_utc,
        include_skipped_stops,
        include_geopath,
        token,
        devid,
        signature,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'expand': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if run_ref is not None:
            _path_params['run_ref'] = run_ref
        if route_type is not None:
            _path_params['route_type'] = route_type
        # process the query parameters
        if expand is not None:
            
            _query_params.append(('expand', expand))
            
        if stop_id is not None:
            
            _query_params.append(('stop_id', stop_id))
            
        if date_utc is not None:
            if isinstance(date_utc, datetime):
                _query_params.append(
                    (
                        'date_utc',
                        date_utc.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('date_utc', date_utc))
            
        if include_skipped_stops is not None:
            
            _query_params.append(('include_skipped_stops', include_skipped_stops))
            
        if include_geopath is not None:
            
            _query_params.append(('include_geopath', include_geopath))
            
        if token is not None:
            
            _query_params.append(('token', token))
            
        if devid is not None:
            
            _query_params.append(('devid', devid))
            
        if signature is not None:
            
            _query_params.append(('signature', signature))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json', 
                'text/json', 
                'text/html'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v3/pattern/run/{run_ref}/route_type/{route_type}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


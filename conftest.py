# we will be adding fixtures of create token and booking id.

from SRC.Constants.api_constants import *
from SRC.Helper.common_verification import *
from SRC.Helper.payload_manager import *
from SRC.Helper.api_request_wrappers import *
from SRC.Utils.utils import *

import allure
import pytest



@pytest.fixture(scope="session")
def create_token():
    response = post_request(
        url=API_constants().url_create_token(),
        auth=None,
        headers=utils().common_headers_json(),
        payload=payload_create_token(),
        in_json=False
    )
    verify_http_status_code(response_data=response, expected_data=200)
    verify_jason_key_is_not_null_token(response.json()["token"])
    return response.json()["token"]


@pytest.fixture(scope="session")
def get_booking_id():
    response = post_request(
        url=API_constants().url_create_booking(),
        auth=None,
        headers=utils().common_headers_json(),
        payload=payload_create_booking(),
        in_json=False)
    booking_id = response.json()["bookingid"]
    verify_http_status_code(response_data=response, expected_data=200)
    verify_json_key_is_not_null(booking_id)
    return booking_id

# @pytest.fixture(scope="session")
# def get_booking_id():
#     response = post_request(url=API_constants().url_create_booking(),
#                             auth=None,
#                             headers=utils().common_headers_json(),
#                             payload=payload_create_booking(),
#                             in_json=False)
#
#     booking_id = response.json()["bookingid"]
#
#     verify_http_status_code(response_data=response, expected_data=200)
#     verify_json_key_is_not_null(booking_id)
#     return booking_id

# performing integration testing by following modules
# create token
# create booking
# update the booking(Put) -booking_id, token
# delete booking

import allure
import pytest


from SRC.Constants.api_constants import API_constants
from SRC.Helper.common_verification import *
from SRC.Helper.api_request_wrappers import *
from SRC.Helper.payload_manager import *
from SRC.Utils.utils import utils


class TestCRUDINTEGRATION(object):
    @pytest.mark.put
    @allure.title("updating teh booking id")
    @allure.description("updating the booking_id using fixtures in conftest.")
    def test_update_booking_id_token(self, create_token, get_booking_id):
        put_url = API_constants.url_put_patch_delete(booking_id=get_booking_id)
        print(put_url)
        response = put_request(
            url=put_url,
            headers=utils().common_headers_patch_put_delete_cookie(token=create_token),
            auth=None,
            payload=payload_update_booking(),
            in_json=False
        )
        # verify the status code and response in the below
        verify_http_status_code(response_data=response, expected_data=200)
        verify_response_key(response.json()["firstname"], expected_data="Mohammed")
        verify_response_key(response.json()["lastname"], expected_data="Khalid")

    def test_delete_booking(self, create_token, get_booking_id):
        delete_url = API_constants.url_put_patch_delete(booking_id=get_booking_id)
        print(delete_url)
        response = delete_request(
            url=delete_url,
            headers=utils().common_headers_patch_put_delete_cookie(token=create_token),
            auth=None,
            in_json=False
        )
        verify_response_delete(response=response.text)
        verify_http_status_code(response_data=response, expected_data=201)

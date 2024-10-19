# we will make function which we can use for put,post,get,patch,and delete.
# we store all http methods in this module.
import json
import requests


def get_request(url, auth):
    response = requests.get(url=url, auth=auth)
    return response.json()


def post_request(url, auth, headers, payload, in_json):
    post_response_data = requests.post(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return post_response_data.json()
    return post_response_data


def patch_request(url, auth, headers, payload, in_json):
    patch_response_data = requests.patch(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return patch_response_data.json()
    return patch_response_data


def put_request(url, auth, headers, payload, in_json):
    put_response_data = requests.put(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return put_response_data.json()
    return put_response_data


def delete_request(url, auth, headers, in_json):
    delete_response_data = requests.delete(url=url, auth=auth, headers=headers)
    if in_json is True:
        return delete_response_data.json()
    return delete_response_data

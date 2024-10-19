# we add all our payload in this file sucha s follows
# create booking payload
# create token payload

def payload_create_booking():
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"

    }
    return payload

def payload_update_booking():
    payload = {
        "firstname": "Mohammed",
        "lastname": "khalid",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"

    }
    return payload

def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload

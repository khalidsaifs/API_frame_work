Hybrid custom Api Framework


Python 3.12
Requests - HTTP Requests
PyTest - Testing Framework
Reporting - Allure Report, PyTest HTML
Test Data - CSV, Excel, JSON, Faker
Advance API Testcase - jsonschema
Parallel Execution - x distribute (xdist)

How to Install Packages

pip install requests pytest pytest-html faker allure-pytest jsonschema
How to run your Testcase Parallel pip install pytest-xdist 

How to run the Basic Test with Allure report

 pytest tests/tests/crud/test_create_booking.py  --alluredir=allure_result -s
 allure serve allure_result 
 
API test case

we did all the code into smaller chunks, so we can reuse the chunks.

what we need for API test cases as follows

URLs = constants.py
Headers = utils.py
payload = payload_manager.py
verification = common_verification.py(helper)
http request = api_request_wrappers.py(helper)



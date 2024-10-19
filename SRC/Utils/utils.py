# common utilities
# headers
# read data from excel,csv,jason files.
# set the headers  - application/json or application/xml

class utils(object):

    def common_headers_json(self):
        headers = {
            "Content-Type" : "application/json"
        }
        return headers

    def common_headers_xml(self):
        headers = {
            "Content-Type" : "application/xml"
        }
        return headers

    def common_headers_patch_put_delete_auth(self,basic_auth_value):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic" + str(basic_auth_value)
        }
        return headers

    def common_headers_patch_put_delete_cookie(self,token):
        headers = {
            "Content-Type": "application/json",
            "Cookie": "token=" + str(token)
        }
        return headers
# if we need we can also add teh following function in the future, if they are in use

    def read_csv_file(self):
        pass

    def read_excel_file(self):
        pass

    def read_database(self):
        pass

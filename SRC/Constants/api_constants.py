# constants are used to store all the end points and usefull URL
# all the URLs

class API_constants(object):

    def url_base(self):
        return "https://restful-booker.herokuapp.com"

    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    def url_put_patch_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking/:id" + str(booking_id)

# In the 17th line booking id is converted into str to avoid concatination, because booking id is int.


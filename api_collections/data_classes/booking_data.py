import json


class Booking:
    def __init__(self, booking_id=None, **kwargs):
        self.firstname = 'Mary' if 'firstname' not in kwargs.keys() else kwargs['firstname']
        self.lastname = 'Ericsson' if 'lastname' not in kwargs.keys() else kwargs['lastname']
        self.totalprice = 793 if 'totalprice' not in kwargs.keys() else kwargs['totalprice']
        self.depositpaid = True if 'depositpaid' not in kwargs.keys() else kwargs['depositpaid']
        self.bookingdates = {"checkin": "2020-12-22",
                             "checkout": "2023-04-10"} if 'bookingdates' not in kwargs.keys() else \
            kwargs['bookingdates']
        self.__booking_id = booking_id

    def get_body_dict(self):
        booking_dict = self.__dict__
        booking_id_key = '_Booking__booking_id'
        if booking_id_key in booking_dict:
            del booking_dict[booking_id_key]
        return booking_dict

    def get_booking_id(self):
        return self.__booking_id

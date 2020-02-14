class Address:
    def __init__(self, address_one, address_two, city, state, zipcode, country):
        self.address_one = address_one
        self.address_two = address_two
        self.city = city
        self.county = state
        self.zipcode = zipcode
        self.country = country

    def __repr__(self):
        return "Address('{}','{}','{}','{}','{}','{}')".format(self.address_one, self.address_two, self.city, self.state, self.zipcode, self.country)

    def __str__(self):
        return "{}".format(self.address_one)


class Contact:
    def __init__(self, phone=None, alt_phone=None, fax=None, alt_fax=None, email=None, alt_email=None, website=None):
        self.phone = phone
        self.alt_phone = alt_phone
        self.fax = fax
        self.alt_fax = alt_fax
        self.email = email
        self.alt_email = alt_email
        self.website = website

    def __repr__(self):
        return "Contact('{}','{}','{}','{}','{}','{}','{}')".format(self.phone, self.alt_phone, self.fax, self.alt_fax, self.email, self.alt_email, self.website)


class Openings:
    def __init__(self, monday_open, monday_close, tuesday_open, tuesday_close, wednesday_open, wednesday_close, thursday_open, thursday_close, friday_open, friday_close, saturday_open, saturday_close, sunday_open, sunday_close):
        self.monday_open = monday_open
        self.monday_close = monday_close
        self.tuesday_open = tuesday_open
        self.tuesday_close = tuesday_close
        self.wednesday_open = wednesday_open
        self.wednesday_close = wednesday_close
        self.thursday_open = thursday_open
        self.thursday_close = thursday_close
        self.friday_open = friday_open
        self.friday_close = friday_close
        self.saturday_open = saturday_open
        self.saturday_close = saturday_close
        self.sunday_open = sunday_open
        self.sunday_close = sunday_close

    def __repr__(self):
        return "Openings('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
            self.monday_open, self.monday_close, self.tuesday_open, self.tuesday_close, self.wednesday_open,
            self.wednesday_close, self.thursday_open, self.thursday_close, self.friday_open, self.friday_close,
            self.saturday_open, self.saturday_close, self.sunday_open, self.sunday_close,
        )


class Property:
    def __init__(self, address, contact, owner):
        self.address = address
        self.contact = contact
        self.owner = owner

    def __repr__(self):
        return "Property('{}','{}','{}')".format(self.address, self.contact, self.owner)

    def __str__(self):
        return "{}".format(self.address)


class Premise(Property):
    def __init__(self, openings, address, contact, owner):
        super().__init__(address, contact, owner)
        self.openings = openings

    def __repr__(self):
        return "Premise('{}','{}')".format(self.openings, super().__repr__())


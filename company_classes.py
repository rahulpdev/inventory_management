class Company:
    def __init__(self, name, address, contact, owners=[]):
        self.name = name
        self.address = address
        self.contact = contact
        self.owners = owners

    def __repr__(self):
        return "Company('{}','{}','{}','{}')".format(self.name, self.address, self.contact, self.owners)

    def __str__(self):
        return "{}".format(self.name)

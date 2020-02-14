from product_inventory import company_classes as corp, inventory_classes as inventory, location_classes as loc


class Supplier(corp.Company):
    def __init__(self, name, address=None, contact=None, owners=None, product_list=[]):
        super().__init__(name, address, contact, owners)
        self.product_list = product_list

    def __repr__(self):
        return "Supplier('{}','{}')".format(super().__repr__(), self.product_list)

    def add_good(self, good):
        if good not in self.product_list:
            self.product_list.append(good)


class Store(loc.Premise):
    def __init__(self, store_type, openings, address, contact, owner=None):
        super().__init__(openings, address, contact, owner)
        self.store_type = store_type
        self.stock = inventory.Stock()

    def __repr__(self):
        return "Store('{}','{}')".format(self.store_type, super().__repr__())


class Business(corp.Company):
    def __init__(self, name, address=None, contact=None, owners=None, stores=[]):
        super().__init__(name, address, contact, owners)
        self.stores = stores

    def __repr__(self):
        return "Business('{}','{}')".format(super().__repr__(), self.stores)

    def add_store(self, store):
        if store not in self.stores:
            self.stores.append(store)

    def stock_units(self):
        total = 0
        for store in self.stores:
            total += store.stock.units()
        return total

    def stock_value(self):
        total = 0
        for store in self.stores:
            total += store.stock.value()
        return total

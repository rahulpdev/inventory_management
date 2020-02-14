class Item:
    def __init__(self, producer, category, sub_category, name=None, image=None, description=None, dimension=None, variation=None):
        self.producer = producer
        self.category = category
        self.sub_category = sub_category
        self.name = name
        self.image = image
        self.dimension = dimension
        self.variation = variation
        self.description = description

    def __repr__(self):
        return "Item('{}','{}','{}','{}','{}','{}','{}','{}')".format(
            self.producer, self.category, self.sub_category, self.name, self.image, self.description, self.dimension, self.variation
        )

    def __str__(self):
        return "{}".format(self.name)


class Good(Item):
    def __init__(self, supplier, sku, producer, category, sub_category, name=None, image=None, description=None, dimension=None, variation=None):
        super().__init__(producer, category, sub_category, name, image, description, dimension, variation)
        self.supplier = supplier
        self.sku = sku

    def __repr__(self):
        return "Good('{}','{}','{}')".format(
            self.supplier, self.sku, self.producer
        )

    def __str__(self):
        return "{} from {}".format(super().__str__(), self.supplier)


class Stock:
    def __init__(self, purchases=[], sales=[]):
        self.purchases = purchases
        self.sales = sales

    def __repr__(self):
        return "Stock('{}','{}')".format(self.purchases, self.sales)

    def __str__(self):
        return "Stock"

    def buy_stock(self, stock_purchase):
        self.purchases.append(stock_purchase)

    def sell_stock(self, stock_sale):
        self.sales.append(stock_sale)

# what happens if the purchases list is empty?
    def units(self):
        total = 0
        for transaction in self.purchases:
            total += transaction.units
        for transaction in self.sales:
            total -= transaction.units
        return total

    def value(self):
        total = 0
        try:
            for transaction in self.purchases:
                total += transaction.cost * transaction.units
            for transaction in self.sales:
                total -= transaction.cost * transaction.units
        except TypeError:
            # total += 0
        return total

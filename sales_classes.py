class Transaction:
    def __init__(self, good, units, date, cost):
        self.good = good
        self.units = units
        self.date = date
        self.cost = cost

    def __repr__(self):
        return "Transaction('{}',{},{},{})".format(
            self.good, self.units, self.date, self.cost
        )

    def __str__(self):
        return "{} transaction".format(self.good)

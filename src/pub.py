class Pub:
    def __init__( self, name, till ):
        self.name = name
        self.till = till
        self.drinks = [] 

    def add_drink_to_stock(self, drink):
        self.drinks.append(drink)
        # print("drinks", drink.name, drink.price)

    def stock_check(self):
        return len(self.drinks)
import unittest

class ShopModel(object):
    def __init__(self, drink, food, table):
        self.drink = drink
        self.food = food
        self.table = table

    def get_drink(self):
        return self.drink

    def set_drink(self, drink):
        self.drink = drink

    def get_food(self):
        return self.food

    def set_food(self, food):
        self.food = food

    def get_table(self):
        return self.table

    def set_table(self, table):
        self.table = table

    def get_all(self):
        data = {
            'drink' : 'Es teh',
            'food' : 'Nasi goreng',
            'table' : '4'
        }

        return data

unittest.main()
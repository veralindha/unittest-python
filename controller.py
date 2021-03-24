import unittest
from model import ShopModel
from view import MenuView

# Create a class shop controller
class ShopController(object):
    def create_order(self):
        view = MenuView()
        data = view.form_menu()

        return data

    def show(self, data):
        view = MenuView()
        option = view.pilih_pengaturan()

        if option=='1':
            self.view_menu(data)
        elif option=='2':
            print('stop')
        else:
            print('404 error')
            self.show(data)

    def view_menu(self, data):
        view = MenuView()
        view.show_menu(data)

        self.show(data)

    def run(self):
        register = self.create_order()
        drink = register['drink']
        food = register['food']
        table = register['table']

        data = ShopModel(drink, food, table)

        data_menu = data.get_all()
        self.show(data_menu)
unittest.main()
import unittest
class MenuView(object):
    def form_menu(self):
        drink = input('input drink :')
        food = input('input food :')
        table = int(input('input alamat :'))

        data = {
            'drink' : drink,
            'food' : food,
            'table' : table
        }

        return data

    def pilih_pengaturan(self):
        print("[1]. view : \n [2]. exit")
        option = (input('Pilih :'))

        return option

    def show_menu(self, data):
        print('drink' + ":" + str(data['drink']))
        print('food' + ":" + data['food'])
        print('table' + ":" + data['table'])

unittest.main()
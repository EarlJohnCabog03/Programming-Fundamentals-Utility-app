# -*- coding: utf-8 -*-
"""
Created on Tue Jan 1 12:16:05 2024

@author: 97154
"""
"""
Vending Machine
"""
class VendingMachine:
    def __init__(self):
        self.menu = {
            '0': {'item': 'Takis', 'price': 3.97},
            '1': {'item': 'Triscuit', 'price': 4.98},
            '2': {'item': 'Pocky', 'price': 1.24},
            '3': {'item': 'Whoppers', 'price': 1.30},
            '4': {'item': 'Coca-Cola Soda', 'price': 4.98},
            '5': {'item': 'Cactus Cooler Orange Soda', 'price': 6.78},
            '6': {'item': 'Schweppes', 'price': 1.48},
            '7': {'item': 'Mountain Dew Citrus Soda', 'price': 2.99},
            '8': {'item': 'Sprite', 'price': 2.01},
            '9': {'item': 'Pepsi', 'price': 5.96},
            '10': {'item': 'Hersheys', 'price': 4.38},
            '11': {'item': 'Reeses', 'price': 2.70},
            '12': {'item': 'Snickers', 'price': 1.32},
            '13': {'item': 'Hersheys Kisses', 'price': 3.96},
            '14': {'item': 'Ferrero Rocher', 'price': 2.48},
            '15': {'item': 'Pure Life Purified Water', 'price': 1.34},
            '16': {'item': 'Crescents', 'price': 5.73},
            '17': {'item': 'Monster Ultra Strawberry', 'price': 2.28},
            '18': {'item': 'Bucked Up Energy Drink', 'price': 2.60},
            '19': {'item': 'Monster Energy, Original, Energy Drink', 'price': 10.4},
            '20': {'item': 'Red Bull Sea Blue Edition Energy Drink', 'price': 3.49},
            '21': {'item': 'Bimbo Soft White Bread', 'price': 2.54},
            '22': {'item': 'Great Value Dry Roasted Peanuts', 'price': 2.44},
            '23': {'item': 'Blue Diamond Almonds, BOLD Elote Mexican Street Corn Flavored Snack Nuts', 'price': 3.64},
        }
        self.stock = {code: 5 for code in self.menu}

    def display_menu(self):
        print("=== VENDING MACHINE MENU ===")
        for code, item_info in self.menu.items():
            print(f"{code}. {item_info['item']} - ${item_info['price']:.2f}")

    def get_user_selection(self):
        while True:
            code = input("Enter the code of the item you want to buy: ")
            if code in self.menu and self.stock[code] > 0:
                return code
            elif code in self.menu and self.stock[code] == 0:
                print("Sorry, this item is out of stock. Please make another selection.")
            else:
                print("Invalid code. Please enter a valid code.")

    def process_payment(self, item_code):
        item_price = self.menu[item_code]['price']

        while True:
            try:
                amount_inserted = float(input(f"Insert money (${item_price:.2f}): "))
                if amount_inserted >= item_price:
                    change = amount_inserted - item_price
                    print(f"Dispensing {self.menu[item_code]['item']}...")
                    print(f"Change: ${change:.2f}")
                    self.stock[item_code] -= 1
                    break
                else:
                    print("Insufficient funds. Please insert more money.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

    def operate_vending_machine(self):
        while True:
            self.display_menu()
            selected_code = self.get_user_selection()
            self.process_payment(selected_code)

            another_purchase = input("Do you want to make another purchase? (yes/no): ")
            if another_purchase.lower() != 'yes':
                print("Thank you for using the vending machine. Have a great day!")
                break

if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.operate_vending_machine()

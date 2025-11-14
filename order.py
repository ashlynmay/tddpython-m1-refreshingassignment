# Ashlyn May
# Ms. Young
# Test-Driven Development Python
# Thursday, November 13th

# This file is used for declaring a class called order with various functions.
# This class holds objects such as drinks in a list.
# Functions include:
#   get_items() -> returns a multiline string with descriptions of the 
#                  items in the order
#   get_total() -> returns a string that includes the total of the prices 
#                  of all items in the order, it is formatted as a decimal
#   get_num_items() -> returns an int equal to the number of items
#   get_receipt() -> returns a formatted multiline string with a header for the
#                   business information as well as each individual drink including
#                   listing its base and toppings with prices, and a total price. it
#                   calls the two private format functions to do this (__format_line(),
#                   __format_header()). it sets a string equal to the the result of
#                   __format_header(), and then it loops through each drink object and 
#                   its flavors, and calls __format_line on them with the drink price, flavor price,
#                   or base price and adds that to the string. it then calls get_total()
#                   and prints that to the end. 
#   add_item(drink: Drink, silent: Bool) -> takes a drink object as a paremeter and
#                   adds it to the order. By default, this will print a message to
#                   the console saying it added the drink with its description,
#                   but it can also be thrown an additional parameter "silent: True"
#                   to remove this functionality when adding items
#   remove_item(index: int) -> requires an int paremeter of the index of the drink
#                   that you want removed. it then checks if it is a valid index
#                   and removes the drink. if it isnt valid, it throws a custom error
#   __format_line(string, price) -> takes a string and a price and formats them on
#                   far ends of the width of the receipt (set in config.py), then
#                   returns this formatted string. this function is private so it
#                   can only be accessed inside the order object, like by get_receipt()
#   __format_header(header) -> takes the header list from config.py and formats the
#                   information in it to be centered and gapped on the top & bottom.
#                   this function is also private and cannot be accessed outside of
#                   the order object

from config import header, base_prices, flavor_price, receipt_width
from drink import Drink

class Order:
    def __init__(self):
        self.__items = []
        
    def get_items(self):
        item_defs = ""
        item_num = 1
        for item in self.__items:
            item_defs += f"\n {item_num}. {item.get_drink_description()}"
            item_num+=1
        return item_defs
    
    def get_total(self):
        total = 0.00
        for item in self.__items:
            total += item.get_price()
        total = f"{total:.2f}"
        return total
    
    def get_num_items(self):
        return len(self.__items)

    def get_receipt(self):
        receipt = ""
        receipt += self.__format_header(header) + "\n"
        for item in self.__items:
            receipt += self.__format_line("Drink", item.get_price()) + "\n"
            receipt += self.__format_line("- " + item.get_base().capitalize(), base_prices[item.get_base()]) + "\n"
            for flavor in item.get_flavors():
                receipt += self.__format_line("- " + flavor.capitalize(), flavor_price) + "\n"
            receipt += "\n"
        receipt += self.__format_line("Total:", self.get_total())
        return receipt
    
    def add_item(self, drink: Drink, silent=False):
        self.__items.append(drink)
        if not silent:
            print(f"{drink.get_drink_description()} was added to the order.")
        return f"{drink.get_drink_description()} was added to the order."
    
    def remove_item(self, index: int):
        if index < 0 or index >= len(self.__items):
            raise IndexError("Index out of range")
        self.__items.pop(index)
        return
    
    def __format_line(self, string, price):
        price = str(price)
        space = receipt_width - len(string)
        for i in range(space-4):
            string+=" "
        if len(price) != 4:
            diff = len(price) - 4
            string = string[:-diff]
        string+=price
        return string
        
    def __format_header(self, header):
        fheader = "\n"
        for text in header:
            string = text.center(receipt_width)
            fheader+=string+"\n"
        fheader+="\nOrder:"
        return fheader
    
    
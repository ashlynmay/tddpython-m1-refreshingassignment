# Ashlyn May
# Ms. Young
# Test-Driven Development Python
# Thursday, November 13th

# This file is used for declaring a class called drink with various functions.
# This class is used to create a Drink object that has a base, flavors, and a price.
# Functions include:
#   __init__(base, *flavors) -> this initializer function sets up the drink object with
#                   variables flavors, price, and base. it checks that the base is allowed, 
#                   then adds the bases price to the drink price. it then checks if there are
#                   any flavors, and if so, calls set_flavors(*flavors) to initialize them,
#                   and adds the price to the drink price for each flavor. then its rounds
#                   the price to the nearest cent
#   get_flavors() -> returns the flavors list from the drink from __init__
#   get_base() -> returns the base as a string from __init__
#   get_num_flavors() -> returns the number of flavors in the drink from __init__
#   get_price() -> returns the price of the drink from __init__
#   get_drink_description() -> formats a string explaining the drink in english
#   set_flavors(*flavors) -> resets the flavors of the object and calls add_flavor(*flavors)
#                            with the flavors given to it
#   add_flavor(*flavors) -> takes a parameter flavors that can hold as many flavors as you want,
#                           it then checks if any of the flavors repeats and returns an error if
#                           they do. if they dont, it moves on and iterates through the flavors
#                           and checks if they are allowed and not a base to ensure there is only
#                           one base, and appends them to the current list of flavors.


from config import allowed_bases, base_prices, allowed_flavors, flavor_price

class Drink():
    def __init__(self, base, *flavors):
        self.__flavors = []
        self.__price = 0.00
        if base in allowed_bases:
            self.__base = base
            self.__price += base_prices[base]
        else:
            raise ValueError(f"Invalid base: '{base}'. Base options are: {allowed_bases}")
        if flavors:
            self.set_flavors(*flavors)
            self.__price += len(flavors) * flavor_price
        self.__price = round(self.__price, 2)
    
    def get_flavors(self):
        return self.__flavors
    
    def get_base(self):
        return self.__base
    
    def get_num_flavors(self):
        return len(self.__flavors)
    
    def get_price(self):
        return self.__price
    
    def get_drink_description(self):
        item_msg = ""
        if self.__flavors:
            item_msg = f"A {self.__base} based drink with"
            for prop in self.__flavors[:-1]:
                item_msg += f" {prop}"
                if len(self.__flavors) != 2:
                    item_msg += ','
            item_msg += f" and {self.__flavors[-1]}"
        else:
            item_msg += self.__base.capitalize()
        return(item_msg)
    
    def set_flavors(self, *flavors):
        self.__flavors = []
        self.add_flavor(*flavors)
            
    def add_flavor(self, *flavors):
        if len(flavors) != len(set(flavors)):
            raise ValueError(f"Invalid flavors: {flavors} Flavors can't repeat.")
        for flavor in flavors:
            if flavor in allowed_flavors:
                self.__flavors.append(flavor)
            elif flavor in allowed_bases:
                raise ValueError(f"Invalid option: '{flavor}'. You may only have one base.")
            else:
                raise ValueError(f"Invalid flavor: '{flavor}'. Flavor options are: {allowed_flavors}")
        return
# Ashlyn May
# Ms. Young
# Test-Driven Development Python
# Thursday, November 13th

# This file is used for:
# running code where you are utilizing the two classes drink and order.

from drink import Drink
from order import Order               
        
order = Order()
testdrink1 = Drink('water', 'lemon', 'lime', 'cherry')
testdrink2 = Drink('sbrite', 'strawberry', 'lime')
testdrink3 = Drink('leaf wine', 'mint', 'blueberry', 'cherry', 'lime')
testdrink4 = Drink('Mr. Salt', 'blueberry', 'cherry', 'lime')
testdrink5 = Drink('hill fog', 'mint')
testdrink6 = Drink('pokeacola', 'strawberry')
testdrink7 = Drink('pokeacola')
order.add_item(testdrink1, silent=True)
order.add_item(testdrink2, silent=True)
order.add_item(testdrink3, silent=True)
order.add_item(testdrink4, silent=True)
order.add_item(testdrink5, silent=True)
order.add_item(testdrink6, silent=True)
order.add_item(testdrink6, silent=True)

order.add_item(testdrink7)
print(order.get_receipt())

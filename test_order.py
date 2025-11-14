# Ashlyn May
# Ms. Young
# Test-Driven Development Python
# Thursday, November 13th

# This file is used for testing each function and error case of the order object.
# Error cases include:
#   remove_item(index):
#       index being out of range of the list of items


from order import Order
from drink import Drink
from config import base_prices, flavor_price, header
import pytest

default_base = 'water'
default_flavor1 = 'lemon'
default_flavor2 = 'lime'
default_order = Order()
default_drink = Drink(default_base, default_flavor1, default_flavor2)
default_order.add_item(default_drink)

class TestSetters:
    def test_add_item(self):
        order = Order()
        testdrink = Drink('water', 'lemon', 'lime')
        result = order.add_item(testdrink)
        assert result == f"A water based drink with lemon and lime was added to the order."
        assert order.get_num_items() == 1
    
    def test_remove_item(self):
        order = Order()
        testdrink = Drink('water', 'lemon', 'lime')
        order.add_item(testdrink)
        test_length = order.get_num_items()
        order.remove_item(0)
        assert order.get_num_items() < test_length
        assert order.get_num_items() == 0
    
    def test_remove_item_oob_error(self):
        order = Order()
        with pytest.raises(IndexError, match='Index out of range'):
            test = order.remove_item(0)
        testdrink = Drink('water', 'lemon', 'lime')
        order.add_item(testdrink)
        with pytest.raises(IndexError, match='Index out of range'):
            test = order.remove_item(1)
        with pytest.raises(IndexError, match='Index out of range'):
            test = order.remove_item(-1)
        
class TestGetters:
    def test_get_items(self):
        assert default_order.get_items() == f"\n 1. A water based drink with lemon and lime"
    
    def test_get_total(self):
        test_total = base_prices['water']+(flavor_price*2)
        assert default_order.get_total() == str(round(test_total, 2))
    
    def test_num_items(self):
        assert default_order.get_num_items() == 1
        
    def test_get_receipt(self):
        test_receipt = default_order.get_receipt()
        assert header[0] in test_receipt 
        assert header[1] in test_receipt 
        assert header[2] in test_receipt 
        assert header[3] in test_receipt 
        assert default_base.capitalize() in test_receipt
        assert default_flavor1.capitalize() in test_receipt
        assert default_flavor2.capitalize() in test_receipt
        assert str(default_drink.get_price()) in test_receipt
# Ashlyn May
# Ms. Young
# Test-Driven Development Python
# Thursday, November 13th

# This file is used for testing each function and error case of the drink object.
# Error cases include:
#   __init__(base, *flavors):
#       invalid base, base is not included in allowed base list
#       invalid flavor, flavor is included in flavor list
#       only one base, ensure that there are no repeating bases or more than one
#       flavors cant repeat, ensure that no flavors repeat


import pytest
from drink import Drink
from config import base_prices, flavor_price

default_base = 'water'
default_flavor1 = 'lemon'
default_flavor2 = 'cherry'

default_drink = Drink(default_base, default_flavor1, default_flavor2)

class TestInit:
    def test_drink(self):
        assert default_drink != ValueError
        assert type(default_drink) == Drink
    
    def test_only_base(self):
        correct = Drink('water')
        assert correct != ValueError
        
    def test_invalid_base_error(self):
        with pytest.raises(ValueError, match='Invalid base'):
            Drink('vodka', 'lemon', 'cherry')
            
    def test_invalid_flavor_error(self):
        with pytest.raises(ValueError, match='Invalid flavor'):
            Drink('water', 'orange', 'cherry')
            
    def test_no_repeating_bases_error(self):
        with pytest.raises(ValueError, match='one base'):
            Drink('water', 'sbrite', 'lemon')
            
    def test_no_repeating_flavors_error(self):
        with pytest.raises(ValueError, match="Flavors can't repeat"):
            Drink('water', 'lemon', 'lemon')

            
class TestGetters:
    def test_get_flavors_returns_flavors(self):
        test_flavors = ['lemon', 'cherry']
        drink = Drink('water', test_flavors[0], test_flavors[1])
        assert drink.get_flavors() == test_flavors
        
    def test_get_base_returns_base(self):
        test_base = 'water'
        drink = Drink(test_base, 'lime')
        assert drink.get_base() == test_base
    
    def test_get_num_flavors(self):
        test_flavors = ['lemon', 'lime']
        drink = Drink('water', test_flavors[0], test_flavors[1])
        assert drink.get_num_flavors() == len(test_flavors)
        
    def test_get_price(self):
        test_price = round(base_prices['water'] + (flavor_price*2), 2)
        assert default_drink.get_price() == test_price
        
    def test_get_drink_desc(self):
        test_desc = f"A {default_base} based drink with {default_flavor1} and {default_flavor2}"
        assert default_drink.get_drink_description() == test_desc
    
    

class TestSetters:
    def test_set_flavors(self):
        drink = Drink('water', 'lemon', 'lime')
        assert drink.get_flavors() == ['lemon', 'lime']
        drink.set_flavors('cherry', 'mint')
        assert drink.get_flavors() == ['cherry', 'mint']
        
    def test_add_flavor(self):
        drink = Drink('water', 'lemon', 'lime')
        assert drink.get_flavors() == ['lemon', 'lime']
        drink.add_flavor('cherry')
        assert drink.get_flavors() == ['lemon', 'lime', 'cherry']

class TestPrivateVars:
    def test_flavors(self):
        flavors = ['lemon', 'lime']
        drink = Drink('water', flavors[0], flavors[1])
        with pytest.raises(AttributeError, match='no attribute'):
            test = drink.__flavors
            
    def test_base(self):
        flavors = ['lemon', 'lime']
        drink = Drink('water', flavors[0], flavors[1])
        with pytest.raises(AttributeError, match='no attribute'):
            test = drink.__base
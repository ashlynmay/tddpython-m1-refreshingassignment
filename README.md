
# Sprint 1 - A Refreshing Assignment

An API backend for a drink ordering system. It includes two main classes, `Order` and `Drink`, as well as various methods for both classes that can be used to manipulate the objects in various ways. The project also includes unit tests for both classes to align with the test-driven development philosophy.



## Demo

Insert gif or link to demo


## Configuration

All configuration for this project can be done in the `config.py` file. This file includes multiple variables for different settings such as:

### Drink Customization
These variables are used to customize the `Drink` class.
#### allowed_bases
A list containing the bases that are allowed in the drinks. Default: `['water', 'sbrite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine']`
#### base_prices
A dictionary where the key is the name of the base and the key is the price. Bases can have individual prices. Default `{'water': 1.99, 'sbrite': 2.99, 'pokeacola': 3.49, 'Mr. Salt': 3.49, 'hill fog': 3.99, 'leaf wine': 4.99}`
#### allowed_flavors
A list containing the allowed flavors for the drinks. Default: `['lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime']`
#### flavor_price
A variable containing the price of all flavors. Flavors do not have individual pricing. Default: `0.49`

### Receipt Customization
These variables are used to customize the result of the `Order.get_receipt()` method.
#### restaurant_name
A string that contains the name of the restaurant. Default: `"Giovanni's Drink Shoppe"`
#### restaurant_address
A string that contains the address of the restaurant. Default: `"1234 N Boldergeist Rd."` 
#### restaurant_phone
A string that contains the phone number of the restaurant. Default: `"(316)123-4567"`
#### restaurant_website
A string that contains the website of the restaurant. Default: `"www.giovannisdrinks.com"`
#### header
A list that combines all restaurant variables to be used in to format the header in the receipt. Default: `[restaurant_name, restaurant_address, restaurant_phone, restaurant_website]`
#### receipt_width
A int that defines the width of the printed string. Default: `30`


## Documentation
Aside from the `config.py` file, there are five other files.
### `drink.py`
This file is used for declaring a class called drink with various functions. This class is used to create a Drink object that has a base, flavors, and a price. The functions included in this file are:
#### `__init__(base, *flavors)`
This initializer function sets up the drink object with variables flavors, price, and base. It checks that the base is allowed, then adds the bases price to the drink price. It then checks if there are any flavors, and if so, calls set_flavors(*flavors) to initialize them, and adds the price to the drink price for each flavor. Then its rounds the price to the nearest cent.
#### `get_flavors()`
Returns the flavors list from the drink from `__init__`.
#### `get_base()`
Returns the base as a string from `__init__`.
#### `get_num_flavors()`
Returns the number of flavors in the drink from `__init__`.
#### `get_price()`
Returns the price of the drink from `__init__`.
#### `get_drink_description()`
Formats a string explaining the drink in English.
#### `set_flavors(*flavors)`
Resets the flavors of the object and calls `add_flavor(*flavors)` with the flavors given to it.
#### `add_flavor(*flavors)`
Takes a parameter `flavors` that can hold as many flavors as you want. It then checks if any of the flavors repeat and returns an error if they do. If they dont, it moves on and iterates through the flavors and checks if they are allowed and not a base to ensure there is only one base, and appends them to the current list of flavors.


### `order.py`
#### `get_items()`
Returns a multiline string with descriptions of the items in the order.
#### `get_total()`
Returns a string that includes the total of the prices of all items in the order, it is formatted as a decimal.
#### `get_num_items()`
Returns an int equal to the number of items.
#### `get_receipt()`
Returns a formatted multiline string with a header for the business information as well as each individual drink, including listing its base and toppings with prices and a total price. It calls the two private format functions to do this (`__format_line()`, `__format_header()`). It sets a string equal to the the result of `__format_header()`, and then it loops through each drink object and it's flavors, and calls `__format_line()` on them with the drink price, flavor price or base price, and adds that to the string. It then calls `get_total()` and prints that to the end. 
#### `add_item(drink: Drink, silent: Bool)`
Takes a `Drink` object as a paremeter and adds it to the order. By default, this will print a message to the console saying it added the drink with its description,
but it can also be thrown an additional parameter `silent: True`
to remove this functionality when adding items.
#### `remove_item(index: int)`
Requires an int paremeter of the index of the drink that you want removed. It then checks if it is a valid index and removes the drink. If it isnt valid, it throws a custom error.
#### `__format_line(string, price)`
Takes a string and a price and formats them on far ends of the width of the receipt (set in `config.py`). It then returns this formatted string. This function is private so it can only be accessed inside the `Order` object, like by `get_receipt()`.
#### `__format_header(header)`
Takes the header list from `config.py` and formats the information in it to be centered and gapped on the top and bottom. This function is also private and cannot be accessed outside of the `Order` object.

### `main.py`
This file can be edited however the user seems fit to utilize the objects. Currently it sets up a drink, adds it to an order, and prints a receipt.

### `test_order.py`
This is a file that can be utilized by `pytest` to perform unit tests on the `Order` class. It includes tests for each function and error case. Error cases include:
#### `remove_item(index)`
#### Invalid index
Index being out of range of the list of items.

### `test_drink.py`
This is a file that can be utilized by `pytest` to perform unit tests on the `Drink` class. It includes tests for each function and error case. Error cases include:
#### `__init__(base, *flavors)`
#### Invalid base
Base is not included in allowed base list.
#### Invalid flavor
Flavor is included in allowed flavors list.
#### Only one base
Ensure that there is not more than one base.
#### Flavors cant repeat
Ensure that no flavors repeat.

## Screenshots

### `config.py`
![config.py screenshot](/screenshots/configpy.png)


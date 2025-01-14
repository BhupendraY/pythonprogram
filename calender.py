import calendar

year = 2025
month =2
print(calendar.month(year, month))


product_info = [
    'Wireless Mouse',
    'Electonics',
    'Black',
    'Battery Included',
    15.99,
    'In Stock'
]

product_name, *_, price, availability = product_info

# *_: The * (asterisk) is used to collect all intermediate elements into a list called _. 
# The _ is often used to indicate that the collected items won't be used. 
# This means elements 'Electonics', 'Black', and 'Battery Included' are stored in _.

print(f'{product_name} costs ${price} and is {availability}.')
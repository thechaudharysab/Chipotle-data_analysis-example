'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the file with csv.reader() and store it in an object called 'file_nested_list'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''

import csv

# specify that the delimiter is a tab character
# make sure that the path in Spyder (top right hand corner) is set to to dataset folder
with open('chipotle.tsv', 'rU') as f:
    file_nested_list = [row for row in csv.reader(f, delimiter='\t')]

'''
BASIC LEVEL
PART 2: Separate 'file_nested_list' into the 'header' and the 'data'.
'''

header = file_nested_list[0]
data = file_nested_list[1:]
print()
print('Headers: ',header)

'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!
'''

all_prices = []

for price in data:
     all_prices.append(float(price[4].replace('$','')))

average_price = sum(all_prices)/len(all_prices)
print()
print('Average price of an order: $',round(average_price, 2))
print()

'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''

unique_sodas = []
for item in data:
    if item[2] == 'Canned Soda' or item[2] == 'Canned Soft Drink':
        unique_sodas.append(item[3])

print()
print(set(unique_sodas))
print()


'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''
avg_num_topping = []
for item in data:
    if item[2] == 'Burrito':
        avg_num_topping.append(item[3].count(',') + 1)

avg_num_per_burrito = sum(avg_num_topping)/len(avg_num_topping)
print('Average number of toppings per burrito: ', int(round(avg_num_per_burrito)))
print()


'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''
chips_dict = {}
for item in data:
    if "Chips" in item[2]:
        if item[2] in chips_dict.keys():
            chips_dict[item[2]] = int(chips_dict[item[2]])+int(item[1])
        else:
            chips_dict[item[2]] = item[1]
print()
print(chips_dict)

'''
BONUS: Think of a question about this data that interests you, and then answer it!

I'm Answering the average number of items each order
I'll be using order_id
'''

avg_items_per_order = {}
for item in data:
    if item[0] in avg_items_per_order.keys():
        avg_items_per_order[item[0]] = int(avg_items_per_order[item[0]]+1)
    else:
        avg_items_per_order[item[0]] = 1

avg_value = sum(avg_items_per_order.values())/len(avg_items_per_order)
print()
print('Average number of items with an order: ',round(avg_value))
print()
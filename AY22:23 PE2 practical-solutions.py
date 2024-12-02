##############
# Question 1 #
##############

# Question 1 grading scheme
# Recursive solution
# [+0.5] Recursive call on dictionary present (must be reached)
# [+0.5] CORRECTLY checked type(v) != dict, then CORRECTLY added key:value pair to flattened dictionary
# [+1] CORRECTLY checked type(v) == dict correctly, then attempted ALL of the following:
# 1. recurse the nested dictionary
# 2. concatenate the new key
# 3. add new key:value pair to flattened dictionary
# 
# [+3] Fully correct solution
# >>> [+2] Flatten correctly, but failed to account for duplicate keys correctly
# >>> [+1] Flatten correctly, but failed to account for duplicate keys correctly, and other minor mistakes  
#
# Iterative solution
# [+0.5] Used while loop to traverse the entire dictionary
# [+0.5] CORRECTLY checked type(v) != dict correctly, then CORRECTLY added key:value pair to flattened dictionary
# [+1] CORRECTLY checked type(v) == dict correctly, then attempted ALL of the following:
# 1. iteratively flatten the nested dictionary
# 2. concatenate the new key
# 3. add new key:value pair to flattened dictionary
# 
# [+3] Fully correct solution
# >>> [+2] Flatten correctly, but failed to account for duplicate keys correctly
# >>> [+1] Flatten correctly, but failed to account for duplicate keys correctly, and other minor mistakes 

# Recursive solution
def flatten_dictionary(nested_dict, sep):
    result = {}
    for key, value in nested_dict.items():
        if type(value) == dict:
            flatten_value = flatten_dictionary(value, sep)
            for inner_key, inner_value in flatten_value.items():
                new_key = f'{key}{sep}{inner_key}'
                if new_key not in result:
                    result[new_key] = inner_value
        elif str(key) not in result:
            result[str(key)] = value
    return result

# Non-recursive solution
# The idea is to process everything in reverse order using stack
# This ensures the lastly updated value is the first one appearing in the dictionary
def flatten_dictionary(nested_dict, sep):
    result = {}
    stack = list(nested_dict.items())
    while stack:
        key, value = stack.pop()
        if type(value) != dict:
            result[str(key)] = value
        else:
            stack.extend([(f'{key}{sep}{inner_key}', inner_value) for inner_key, inner_value in value.items()])
    return result

def test_q1():
    _ = flatten_dictionary({'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}, '_'); 
    print(_=={'a': 1, 'b_c': 2, 'b_d_e': 3}, "flatten_dictionary({'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}, '_')", _, sep='\t')
    
    _ = flatten_dictionary({'C': {'S': {'1': {'0': {'1': {'0':'S'}}}}}}, ''); 
    print(_=={'CS1010': 'S'}, "flatten_dictionary({'C': {'S': {'1': {'0': {'1': {'0':'S'}}}}}}, '')", _, sep='\t')
    
    _ = flatten_dictionary({2: 1, 4: {6: 2, 8: {10: 3}, 12:4}, 14:5}, '-'); 
    print(_=={'2': 1, '4-6': 2, '4-8-10': 3, '4-12': 4, '14': 5}, " flatten_dictionary({2: 1, 4: {6: 2, 8: {10: 3}, 12:4}, 14:5}, '-')", _, sep='\t')
    
    _ = flatten_dictionary({(1,2): { 3: ['a','b', 'c'], (4,5): {(6,7): ['d','e,','f','g'] }}}, '*');
    print(_=={'(1, 2)*3': ['a', 'b', 'c'], '(1, 2)*(4, 5)*(6, 7)': ['d', 'e,', 'f', 'g']}, "flatten_dictionary({(1,2): { 3: ['a','b', 'c'], (4,5): {(6,7): ['d','e,','f','g'] }}}, '*')", _, sep='\t')
    
    _ = flatten_dictionary({'b_c': 5, 'b': {'c': 3}}, '_');
    print(_=={'b_c': 5}, "flatten_dictionary({'b_c': 5, 'b': {'c': 3}}, '_')", _, sep='\t')


# Uncomment to test question 1
# test_q1()


###############
# Helper for Q2
###############

import csv

def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of lists
    containing rows in the csv file and its entries.
    """
    with open(csvfilename, encoding='utf-8') as csvfile:
        return list(csv.reader(csvfile))

###############
# Question 2a #
###############

# Question 2a grading scheme
def year_of_max_graduates(course, filename):
    data = read_csv(filename)[1:]
    # [+1] filter course
    data = list(filter(lambda x: x[2] == course, data))
    # [+1] iterate and store data
    store = {}
    for year, sex, course, intake, graduates in data:
        year = int(year)
        if year not in store:
            store[year] = 0
        # [+1] sum graduate
        store[year] += int(graduates)
    # [+1] return max graduate
    # [+1] return most recent year
    return max(store.items(), key = lambda x: (x[1],x[0]))

def test_q2a():
    filename = 'enrollment.csv'
    _ = year_of_max_graduates('Accountancy', filename); print(_==(2019, 2248), "year_of_max_graduates('Accountancy', 'enrollment.csv')", _, sep='\t')
    _ = year_of_max_graduates('Education', filename); print(_==(2012, 1117), "year_of_max_graduates('Education', 'enrollment.csv')", _, sep='\t')
    _ = year_of_max_graduates('Law', filename); print(_==(2021, 631), "year_of_max_graduates('Law', 'enrollment.csv')", _, sep='\t')


# Uncomment to test question 2a
# test_q2a()

###############
# Question 2b #
###############

# Question 2b grading scheme
# [+1] Filter by year
# [+1] Group by courses with both genders
# [+1] Calculated ratio and round off to 2 dp
# The marks below will be awarded only if there is a significant attempt
# to calculate the disproportionate ratio
# - [+1] Sorting and return top-k disproportionate courses
# - [+0.5] Handle ties
# - [+0.5] Handle edge cases where k > len(data)

def top_K_disproportionate_courses(k, year, filename):
    data = read_csv(filename)[1:]
    grouped_data = {}

    for yr, sex, crs, intake, grad in data:
        if int(yr) == year:
            if crs not in grouped_data: grouped_data[crs] = {'M': 0, 'F': 0}
            grouped_data[crs][sex] += int(intake)

    for course in grouped_data:
        males, females = grouped_data[course]['M'], grouped_data[course]['F']
        grouped_data[course] = round(abs(males - females)/(males + females), 2)

    sorted_data = sorted(grouped_data.items(), key=lambda x: x[1], reverse=True)
    if k >= len(sorted_data):
        return sorted_data

    threshold_ratio = sorted_data[k-1][1]
    return list(filter(lambda x: x[1] >= threshold_ratio, sorted_data))

def test_q2b():
    filename = 'enrollment.csv'
    _ = top_K_disproportionate_courses(3, 2011, filename); print(_==[('Engineering Sciences', 0.55), ('Information Technology', 0.49), ('Law', 0.36)], "top_K_dispropotionate_courses(3, 2011, 'enrollment.csv')", _, sep='\t')
    _ = top_K_disproportionate_courses(3, 2019, filename); print(_==[('Engineering Sciences', 0.55), ('Information Technology', 0.48), ('Medicine', 0.38)], "top_K_dispropotionate_courses(3, 2019, 'enrollment.csv')", _, sep='\t')
    _ = top_K_disproportionate_courses(4, 2021, filename); print(_==[('Information Technology', 0.61), ('Engineering Sciences', 0.57),  ('Law', 0.36), ('Medicine', 0.35)], "top_K_dispropotionate_courses(4, 2021, 'enrollment.csv')", _, sep='\t')

# Uncomment to test question 2a
# test_q2b()

##############
# Question 3 #
##############

# Question 3 grading scheme
# Product Class
# [+0.5] Initialise Product with name and price
# [+0.5] Correctly implement get_price
#
# DiscountedProduct Class
# [+0.5] Declare Product as a superclass of DiscountedProduct
# # Declare `class DiscountedProduct(Product):`
# [+0.5] Use superclass init for DiscountedProduct
#
# [+0.5] Good OOP practice
# Input CORRECTLY computed discounted price into superclass init
# # super().__init__(name, discounted_price)
# OR
# Initialise discount as an attribute and override get_price to CORRECTLY compute the price
# NOT awarded if:
# #  `self.price` is modified directly (Breaking Abstraction)
# # the computed price is not rounded off to 2 decimal places
#
# Cart Class
# [+0.5] Correctly initialise Cart
# [+0.5] Correctly implement add_item
# # Awarded based on functionality
# [+0.5] Check if product is a valid Product with isInstance in add_item
# # Using type check is not accepted
# [+0.5] Correctly implement checkout
# [+0.5] Use get_price to get product price
# # Not awarded if you directly access price attribute
# # Not awarded if you make a different getter for DiscountedProduct

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def get_price(self):
        modifier = (100 - self.discount) / 100
        return round(super().get_price() * modifier, 2)

class Cart:
    def __init__(self):
        self.cart = {}

    def add_item(self, thing):
        if isinstance(thing, Product):
            if thing.name not in self.cart:
                self.cart[thing.name] = 0
            self.cart[thing.name] += thing.get_price()
            return f'Adding {thing.name} to the cart.'
        else:
            return 'Invalid item.'

    def checkout(self):
        return self.cart

# Alternative (No Polymorphism)
class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        discounted_price = round(price * (100 - discount) / 100, 2)
        super().__init__(name, discounted_price)

# Tests
def test_q3():
    milk = Product("milk", 5.65)
    bread = Product("bread", 3.25)
    eggs = Product("eggs", 2.85)
    cereal = DiscountedProduct("post", 6.6, 10)
    c = Cart()
    shopping_list = [milk, milk, bread]
   
    _=milk.get_price(); print(_ == 5.65, "\tmilk.get_price()  \t", repr(_))
    _=c.add_item(milk); print(_ == 'Adding milk to the cart.', "\tc.add_item(milk)  \t", repr(_))
    _=c.add_item(bread); print(_ == 'Adding bread to the cart.', "\tc.add_item(bread)  \t", repr(_))
    _=c.add_item(bread); print(_ == 'Adding bread to the cart.', "\tc.add_item(bread)  \t", repr(_))
    _=c.add_item(shopping_list); print(_ == 'Invalid item.', "\tc.add_item(shopping_list)  \t", repr(_))
    _=c.add_item(eggs); print(_ == 'Adding eggs to the cart.', "\tc.add_item(eggs)  \t", repr(_))
    _=c.add_item(cereal); print(_ == 'Adding post to the cart.', "\tc.add_item(cereal)  \t", repr(_))
    _=c.add_item(c); print(_ == 'Invalid item.', "\tc.add_item(c)  \t", repr(_))
    _=c.checkout(); print(_ == {'milk': 5.65, 'bread': 6.5, 'eggs': 2.85, 'post': 5.94}, "\tc.checkout() \t", repr(_))

# Uncomment to test question 3
# test_q3()

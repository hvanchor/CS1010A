##############
# Question 1 #
##############
def flatten_dictionary(nested_dict, sep):
    result = {}
    for k, v in nested_dict.items():
        if isinstance(v, dict):
            flatten_value = flatten_dictionary(v, sep)
            for key, value in flatten_value.items():
                new_key = f"{k}{sep}{key}"
                if new_key not in result:
                    result[new_key] = value
                result[new_key] == value
        elif str(k) not in result:
            result[str(k)] = v
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
#test_q1()


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

def year_of_max_graduates(course, filename):
    data = filter(lambda x: x[2] == course, read_csv(filename)[1:])
    d = {}
    for row in data:
        year = int(row[0])
        graduates = int(row[4])
        if year not in d:
            d[year] = 0
        d[year] += graduates
    return max(d.items(), key = lambda x: (x[1],x[0]))


def test_q2a():
    filename = 'enrollment.csv'
    _ = year_of_max_graduates('Accountancy', filename); print(_==(2019, 2248), "year_of_max_graduates('Accountancy', 'enrollment.csv')", _, sep='\t')
    _ = year_of_max_graduates('Education', filename); print(_==(2012, 1117), "year_of_max_graduates('Education', 'enrollment.csv')", _, sep='\t')
    _ = year_of_max_graduates('Law', filename); print(_==(2021, 631), "year_of_max_graduates('Law', 'enrollment.csv')", _, sep='\t')


# Uncomment to test question 2a
#test_q2a()

###############
# Question 2b #
###############


def top_K_disproportionate_courses(k, year, filename):
    data = filter(lambda x: x[0] == str(year), read_csv(filename))
    d = {}
    for row in data:
        intake = int(row[3])
        gender = row[1]
        course = row[2]
        if course not in d:
            d[course] = {'M': 0, 'F': 0}
        d[course][gender] += intake
    for course in d:
        m, f = d[course]['M'], d[course]['F']
        d[course] = round(abs(m-f)/(m+f), 2)
    sorted_d = sorted(d.items(), key = lambda x:x[1], reverse = True)
    if k == 0:
        return []
    if k >= len(sorted_d):
        return sorted_d
    kth = sorted_d[k-1][1]
    return list(filter(lambda x: x[1] >= kth, sorted_d))       

def test_q2b():
    filename = 'enrollment.csv'
    _ = top_K_disproportionate_courses(3, 2011, filename); print(_==[('Engineering Sciences', 0.55), ('Information Technology', 0.49), ('Law', 0.36)], "top_K_disproportionate_courses(3, 2011 'enrollment.csv')", _, sep='\t')
    _ = top_K_disproportionate_courses(3, 2019, filename); print(_==[('Engineering Sciences', 0.55), ('Information Technology', 0.48), ('Medicine', 0.38)], "top_K_disproportionate_courses(3, 2019 'enrollment.csv')", _, sep='\t')
    _ = top_K_disproportionate_courses(4, 2021, filename); print(_==[('Information Technology', 0.61), ('Engineering Sciences', 0.57),  ('Law', 0.36), ('Medicine', 0.35)], "top_K_disproportionate_courses(4, 2021, 'enrollment.csv')", _, sep='\t')

# Uncomment to test question 2a
test_q2b()

##############
# Question 3 #
##############

# Your answer here.
# Q3

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

class DiscountedProduct(Product):
    def __init__(self, name, price, percentage):
        super().__init__(name, price)
        self.percentage = percentage

    def get_price(self):
        discount = (1-self.percentage/100)
        return round(super().get_price() * discount, 2)

class Cart:
    def __init__(self):
        self.cart = {}

    def add_item(self, product):
        if isinstance(product, Product):
            if product.name not in self.cart:
                self.cart[product.name] = 0
            self.cart[product.name] += product.get_price()
            return f"Adding {product.name} to the cart."
        else:
            return "Invalid item."
        
    def checkout(self):
        return self.cart

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
test_q3()

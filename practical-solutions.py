##############
# Question 1 #
##############

# Question 1 grading scheme
# [+1] Recursion or iteration present
# [+1] Base case for n == 1 correct (NEED recursion/iteration to qualify)
# [+1] Multiply recursive call by 4, or exponentiate 4 by n
# [+2] Fully correct

# Recursive
def snowflake(n):
    if n == 1:
        return 3
    if n % 2 == 0:
        return 4 * snowflake(n-1)
    else:
        return 4 * snowflake(n-1) + 3

# Iterative
def snowflake(n):
    res = 0
    for i in range(n - 1, -1, -2):
        res += 4**i
    return 3 * res

def test_q1():
    print(snowflake(1) == 3)
    print(snowflake(2) == 12)
    print(snowflake(3) == 51)
    print(snowflake(4) == 204)
    print(snowflake(5) == 819)

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

def find_increase(town, start_year, end_year, filename):
    data = read_csv(filename)[1:]

    # [+1] filter according to start_year and end_year correctly
    data = filter(lambda x: int(x[0]) >= start_year and int(x[0]) <= end_year, data)
    
    # [+1] filter according to town correctly
    data = filter(lambda x: x[2] == town, data)

    dic = {}

    # [+1] iterate and store prices in dictionary efficiently
    for _, _, _, flat_type, price in data:
        if flat_type not in dic:
            dic[flat_type] = []
        dic[flat_type].append(int(price))

    # [+1] get maximum and minimum of prices efficiently
    for k, v in dic.items():
        dic[k] = max(v) - min(v)

    # [+1] return dictionary that shows difference of max and min
    return dic



def test_q2a():
    result = find_increase('Ang Mo Kio', 2020, 2023, 'hdb.csv')
    print(result == {'3-room': 115500, '4-room': 208400, '5-room': 313000})

    result = find_increase('Queenstown', 2011, 2022, 'hdb.csv')
    print(result == {'3-room': 110000, '4-room': 297000, '5-room': 152000})

    result = find_increase('Tampines', 2010, 2020, 'hdb.csv')
    print(result == {'3-room': 83500, '4-room': 110700, '5-room': 135000, 'Executive': 185000})


# Uncomment to test question 2a
# test_q2a()

###############
# Question 2b #
###############

# Question 2b grading scheme
# [+1] Filter by flat type
# [+0.5] Group by towns using a dictionary
# [+1] Calculate average price per town and round off to nearest thousand
# The marks below will be awarded only if a significant attempt is made
# to calculate the average
# [+1] Sort and return top-k cheapest towns
# [+1] Handle ties
# [+0.5] Handle edge cases where k > len(data)

def cheapest_towns(flat_type, k, filename):
    data = read_csv(filename)[1:]
    data = filter(lambda x: x[3] == flat_type, data)
    price_table = {}
    
    for year, quarter, town, flat, price in data:
        price = int(price)
        if town not in price_table:
            price_table[town] = []
        price_table[town].append(price)
    
    for town, prices in price_table.items():
        price_table[town] = int(round(sum(prices)/len(prices), -3))
    
    result = sorted(price_table.items(), key=lambda pair: pair[1])
    
    if k == 0:
        return []
    elif k > len(result):
        return result
    
    kth_val = result[k-1][1]
    return list(filter(lambda pair: pair[1] <= kth_val, result))


def test_q2b():
    print(cheapest_towns('3-room', 9, 'hdb.csv') == [
        ('Pasir Ris', 177000),
        ('Woodlands', 273000),
        ('Jurong West', 276000),
        ('Geylang', 278000),
        ('Bukit Batok', 285000),
        ('Yishun', 287000),
        ('Jurong East', 296000),
        ('Bedok', 297000),
        ('Bukit Panjang', 298000),
        ('Hougang', 298000),
        ('Toa Payoh', 298000)])
    print(cheapest_towns('Executive', 5, 'hdb.csv') == [
        ('Toa Payoh', 445000),
        ('Sembawang', 493000),
        ('Punggol', 529000),
        ('Choa Chu Kang', 538000),
        ('Jurong West', 542000)])


# Uncomment to test question 2a
# test_q2b()

##############
# Question 3 #
##############

# Question 3 grading scheme
#
# Overall
# [-0.5] Incorrectly return strings as per PDF
# [-0.5] Very inefficient solution (i.e. worse than O(n) time,
# # where n is the number of points on a Satellite object)
#
# Part Class
# [+0.5] Correctly initialise Part with name and num_of_points
#
# Satellite Class
# [+0.5] Correctly initialise Satellite with name and *points
# # Need to be able to store *points
# [+0.5] Appropriately use a dictionary to store attachment points
# [+0.5] Correctly and efficiently implement Satellite’s methods
# # O(k) time, where k is the number of points for the given Part
# # Not awarded if methods are incorrect
#
# mount Method
# [+0.5] Correctly check the conditions
# # Not awarded if checked in the wrong order
# [+0.5] Correctly update Satellite and Part instances
#
# unmount Method
# [+0.5] Correctly check if nothing is mounted at point
# [+0.5] Correctly update Satellite and Part instances
# 
# test Method
# [+0.5] Correctly check if nothing is mounted at point
# [+0.5] Correctly keep track of and update the test count

class Part:
    def __init__(self, name, num_points):
        self.name = name
        self.num_points = num_points
        self.sat = None
        self.points = ()
        self.tests = 0

class Satellite:
    def __init__(self, name, *points):
        self.name = name
        self.parts = {}
        for point in points:
            self.parts[point] = None

    def mount(self, part, *points):
        if part.sat:
            return f'{part.name} already mounted on {part.sat.name}'
        elif len(points) != part.num_points:
            return 'Wrong number of points'
        
        for point in points:
            if self.parts[point] != None:
                return f'Point {point} is not available'

        part.sat = self
        part.points = points
        for point in points:
            self.parts[point] = part
        return f'{part.name} successfully mounted on {self.name}'

    def unmount(self, point):
        part = self.parts[point]
        if part == None:
            return f'Nothing mounted at {point}'

        part.sat = None
        for pt in part.points:
            self.parts[pt] = None
        return f'{part.name} unmounted from {self.name}'

    def test(self, point):
        part = self.parts[point]
        if part == None:
            return f'Nothing mounted at {point}'

        part.tests += 1
        return f'{part.name} test count is {part.tests}'


# Tests
def test_q3():
    chandrayan3 = Satellite('Chandrayan-III', 'Base', 'Payload Bay',
                            'Solar Mount 1', 'Solar Mount 2')
    inmarsat = Satellite('Inmarsat F4', 'Solar Mount 1', 'Solar Mount 2')
    imager = Part('Imaging', 1)
    rover = Part('Rover', 1)
    panel = Part('Solar Panel', 2)

    _=chandrayan3.mount(imager, 'Payload Bay'); print(_ == 'Imaging successfully mounted on Chandrayan-III', "\tchandrayan3.mount(imager, 'Payload Bay')\t", repr(_))
    _=inmarsat.mount(imager, 'Payload Bay'); print(_ == 'Imaging already mounted on Chandrayan-III', "\tinmarsat.mount(imager, 'Payload Bay')\t", repr(_))
    _=chandrayan3.mount(rover, 'Payload Bay'); print(_ == 'Point Payload Bay is not available', "\tchandrayan3.mount(rover, 'Payload Bay')\t", repr(_))
    _=chandrayan3.mount(panel, 'Solar Mount 1'); print(_ == 'Wrong number of points', "\tchandrayan3.mount(panel, 'Solar Mount 1')\t", repr(_))
    _=chandrayan3.mount(panel, 'Solar Mount 1', 'Solar Mount 2'); print(_ == 'Solar Panel successfully mounted on Chandrayan-III', "\tchandrayan3.mount(panel, 'Solar Mount 1', 'Solar Mount 2')\t", repr(_))
    _=chandrayan3.test('Base'); print(_ == 'Nothing mounted at Base', "\tchandrayan3.test('Base')\t", repr(_))
    _=chandrayan3.test('Payload Bay'); print(_ == 'Imaging test count is 1', "\tchandrayan3.test('Payload Bay')\t", repr(_))
    _=chandrayan3.test('Solar Mount 1'); print(_ == 'Solar Panel test count is 1', "\tchandrayan3.test('Solar Mount 1')\t", repr(_))
    _=chandrayan3.test('Payload Bay'); print(_ == 'Imaging test count is 2', "\tchandrayan3.test('Payload Bay')\t", repr(_))
    _=chandrayan3.test('Solar Mount 2'); print(_ == 'Solar Panel test count is 2', "\tchandrayan3.test('Solar Mount 2')\t", repr(_))
    _=chandrayan3.unmount('Solar Mount 1'); print(_ == 'Solar Panel unmounted from Chandrayan-III', "\tchandrayan3.unmount('Solar Mount 1')\t", repr(_))
    _=inmarsat.mount(panel, 'Solar Mount 1', 'Solar Mount 2'); print(_ == 'Solar Panel successfully mounted on Inmarsat F4', "\tinmarsat.mount(panel, 'Solar Mount 1', 'Solar Mount 2')\t", repr(_))
    _=inmarsat.test('Solar Mount 2'); print(_ == 'Solar Panel test count is 3', "\tinmarsat.test('Solar Mount 2')\t", repr(_))


# Uncomment to test question 3
# test_q3()

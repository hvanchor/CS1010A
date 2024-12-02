##############
# Question 1 #
##############

def snowflake(n):
    if n == 1:
        return 3
    if n % 2 == 0:
        return 4 * snowflake(n-1)
    else:
        return 4 * snowflake(n-1) + 3



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

def find_increase(town, start, end, filename):
    data = read_csv(filename)[1:]
    data = filter(lambda x: int(x[0]) >= start and int(x[0]) <= end, data)
    data = filter(lambda x: x[2] == town, data)
    dic = {}
    for _, _, _, flat_type, price in data:
        if flat_type not in dic:
            dic[flat_type] = []
        dic[flat_type].append(int(price))
    for k, v in dic.items():
        dic[k] = max(v) - min(v)
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

def cheapest_towns(flat_type, k, filename):
    data = read_csv(filename)[1:]
    data = filter(lambda x: x[3] == flat_type, data)
    dic = {}
    for year, quarter, town, flat, price in data:
        price = int(price)
        if town not in dic:
            dic[town] = []
        dic[town].append(price)
    for town, prices in dic.items():
        dic[town] = int(round(sum(prices) / len(prices), -3))

    result = sorted(dic.items(), key=lambda pair: pair[1])

    if k == 0:
        return []
    elif k > len(result):
        return result

    kth_val = result[k - 1][1]
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
test_q3()
##############
# Question 1 #
##############

### Your answer here.
# Q1A
def valid_move(game, start, end):
    removed = False
    for left, right in game:
        if start <= right and left <= end:
            if removed:
                return False
            else:
            	removed = True
    return removed

### Your answer here.
# Q1B
def make_move(game, start, end):
    if not valid_move(game, start, end):
        raise Exception('Invalid Move')
    
    for i in range(len(game)):
        if i >= len(game):
            break
        left, right = game[i]
        # 4 cases
        # remove whole cluster
        if start <= left and right <= end:
            game.pop(i)
        # remove left part of cluster
        elif start <= left and left <= end < right:
            game[i][0] = end + 1
        # remove right part of cluster
        elif left < start <= right and right <= end:
            game[i][1] = start - 1
        # split cluster into two
        elif left < start and end < right:
            game.insert(i+1, [end + 1, game[i][1]])
            game[i][1] = start - 1
            
    return game


# Tests
def test_q1a():
    game = [[1, 3], [8, 9], [14,20]]
    print(valid_move(game, 2, 8))
    print(valid_move(game, 4, 7))
    print(valid_move(game, 2, 6))

def test_q1b():
    game = [[1, 20]]
    print(make_move(game, 10, 13))
    print(make_move(game, 4, 7))
    print(make_move(game, 15, 17))


# Uncomment to test question 1
##test_q1a()
test_q1b()



##############
# Question 2 #
##############

import csv
def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    rows = []
    with open(csvfilename, encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows

import math
def get_distance(lat1, long1, lat2, long2):
    """
    Takes in two pairs of lat-long float coordinates,
    returns the distance between the two coordinates
    """
    return round(math.sqrt( (lat1-lat2)**2 + (long1-long2)**2 ), 5)



### Your answer here.
# Q2A
def k_nearest_listings(fname, latitude, longitude, k):
    # drop header
    data = read_csv(fname)[1:]
    # sort via distance latitude [6] and longitude [7]
    data = sorted(data, key=lambda row: get_distance(float(row[4]), float(row[5]), latitude, longitude))
    k_th = data[:k][-1]
    data = list(filter(lambda row: get_distance(float(row[4]), float(row[5]), latitude, longitude) <= \
        get_distance(float(k_th[4]), float(k_th[5]), latitude, longitude), data))
    # get top k entries and extract listing id [0] as integer
    return list(map(lambda row: int(row[0]), data))

### Your answer here.
# Q2B      
def neighbourhood_price_per_region(fname, region):
    # drop header
    data = read_csv(fname)[1:]
    # filter by at least 1 review [7] and region [2]
    data = list(filter(lambda row: int(row[7])>0 and row[2] == region, data))

    # store neighbourhood [3] as key, and prices [6] as value in a list
    neighbouhood_prices = {}
    for row in data:
        if row[3] not in neighbouhood_prices:
            neighbouhood_prices[row[3]] = []
        neighbouhood_prices[row[3]].append(int(row[6]))

    # convert to average price
    for neighbourhood, prices in neighbouhood_prices.items():
        neighbouhood_prices[neighbourhood] = round(sum(prices)/len(prices),2)
    return neighbouhood_prices


# Tests
def test_q2a():
    print(k_nearest_listings("listings.csv", 1.38837, 103.67087, 1) == \
        [13756029])
    print(k_nearest_listings("listings.csv", 1.42724, 103.84648, 3) == \
        [9980935, 9105592, 15189554])
    print(k_nearest_listings("listings.csv", 1.29114, 103.87363, 5) == \
        [35199403, 1178486, 17540932, 35219943, 8623041])

def test_q2b():
    print(neighbourhood_price_per_region("listings.csv", "East Region") == \
        {'Tampines': 97.02, 'Bedok': 124.14, 'Pasir Ris': 86.35})
    print(neighbourhood_price_per_region("listings.csv", "North-East Region") == \
        {'Serangoon': 88.4, 'Hougang': 89.16, 'Punggol': 75.0, 'Ang Mo Kio': 80.96, 'Sengkang': 57.02})
    print(neighbourhood_price_per_region("listings.csv", "North Region") == \
        {'Woodlands': 90.02, 'Sembawang': 89.58, 'Central Water Catchment': 110.36, 'Yishun': 96.68, 'Mandai': 56.67, 'Sungei Kadut': 49.0})


# Uncomment to test question 2
##test_q2a()
##test_q2b()    

##############
# Question 3 #
##############

class Doll:
    def __init__(self, name):
        self.name = name
        self.dolls = [self]
        self.mother = None
        self.daughter = None

    def encase(self, other):
        if self.daughter:
            return f"{self.name} already contains {self.daughter.name}"
        if self.mother:
            return f"{self.name} is currently encased in {self.mother.name}"
        elif other.mother:
            return f"{other.name} is currently encased in {other.mother.name}"
        else:
            self.daughter = other
            other.mother = self
            # Update the series of dolls
            if self.dolls != other.dolls:
                self.dolls.remove(self)
                self.dolls = other.dolls
                self.dolls.append(self)
            return f'{self.name} encases {other.name}'        

    def release(self):
        if self.mother:
            return f'{self.name} is currently encased in {self.mother.name}'
        elif not self.daughter:
            return f'{self.name} does not contain any dolls'
        else:
            msg = f'{self.name} releases {self.daughter.name}'   
            self.daughter.mother = None
            self.daughter = None
            return msg

    def get_name(self):
        return self.name

    def get_mother(self):
        return self.mother

    def get_daughter(self):
        return self.daughter

    def num_encased(self):
        return len(tuple(filter(lambda doll: doll.mother, self.dolls)))
   
    def deeply_contains(self, other):        
        if self.daughter == other:
            return True
        elif self.daughter:
            return self.daughter.deeply_contains(other)
        else:
            return False

    def series(self):
         return tuple(map(lambda doll: doll.name, self.dolls))



# Test cases

def test_q3():
    alice = Doll("Alice")
    betty = Doll("Betty")
    clara = Doll("Clara")
    doris = Doll("Doris")
    
    _=alice.get_name(); print(_ == "Alice", "\talice.get_name():\t", _)
    _=alice.get_mother(); print(_ == None, "\talice.get_mother():\t", _)
    _=alice.get_daughter(); print(_ == None, "\talice.get_daughter():\t", _)
    _=alice.series(); print(tuple(sorted(_)) == ('Alice',), "\talice.series():\t", _)
    _=betty.encase(alice); print(_ == "Betty encases Alice", "\tbetty.encase(alice):\t", _)
    _=betty.get_daughter() is alice; print(_ == True, "\tbetty.get_daughter() is alice:\t", _)
    _=alice.get_mother() is betty; print(_ == True, "\talice.get_mother() is betty:\t", _)
    _=betty.encase(clara); print(_ == "Betty already contains Alice", "\tbetty.encase(clara):\t", _)
    _=alice.encase(clara); print(_ == "Alice is currently encased in Betty", "\talice.encase(clara):\t", _)
    _=clara.encase(alice); print(_ == "Alice is currently encased in Betty", "\tclara.encase(alice):\t", _)
    _=clara.encase(betty); print(_ == "Clara encases Betty", "\tclara.encase(betty):\t", _)
    _=alice.series(); print(tuple(sorted(_)) == ('Alice', 'Betty', 'Clara'), "\talice.series():\t", _)
    _=betty.series(); print(tuple(sorted(_)) == ('Alice', 'Betty', 'Clara'), "\tbetty.series():\t", _)
    _=clara.series(); print(tuple(sorted(_)) == ('Alice', 'Betty', 'Clara'), "\tclara.series():\t", _)
    _=alice.num_encased(); print(_ == 2, "\talice.num_encased():\t", _)
    _=betty.num_encased(); print(_ == 2, "\tbetty.num_encased():\t", _)
    _=clara.num_encased(); print(_ == 2, "\tclara.num_encased():\t", _)
    _=clara.deeply_contains(alice); print(_ == True, "\tclara.deeply_contains(alice):\t", _)
    _=alice.deeply_contains(clara); print(_ == False, "\talice.deeply_contains(clara):\t", _)
    _=alice.release(); print(_ == "Alice is currently encased in Betty", "\talice.release():\t", _)
    _=betty.release(); print(_ == "Betty is currently encased in Clara", "\tbetty.release():\t", _)
    _=clara.release(); print(_ == "Clara releases Betty", "\tclara.release():\t", _)
    _=betty.release(); print(_ == "Betty releases Alice", "\tbetty.release():\t", _)
    _=alice.release(); print(_ == "Alice does not contain any dolls", "\talice.release():\t", _)
    _=alice.series() == betty.series() == clara.series(); print(_ == True, "\talice.series() == betty.series() == clara.series():\t", _)
    _=alice.encase(clara); print(_ == "Alice encases Clara", "\talice.encase(clara):\t", _)
    _=alice.num_encased(); print(_ == 1, "\talice.num_encased():\t", _)
    _=betty.num_encased(); print(_ == 1, "\tbetty.num_encased():\t", _)
    _=clara.num_encased(); print(_ == 1, "\tclara.num_encased():\t", _)
    _=betty.encase(doris); print(_ == "Betty encases Doris", "\tbetty.encase(doris):\t", _)
    _=alice.series(); print(tuple(sorted(_)) == ('Alice', 'Clara'), "\talice.series():\t", _)
    _=betty.series(); print(tuple(sorted(_)) == ('Betty', 'Doris'), "\tbetty.series():\t", _)
    _=clara.series(); print(tuple(sorted(_)) == ('Alice', 'Clara'), "\tclara.series():\t", _)
    _=doris.series(); print(tuple(sorted(_)) == ('Betty', 'Doris'), "\tdoris.series():\t", _)
    
# Uncomment to test question 3
##test_q3()    

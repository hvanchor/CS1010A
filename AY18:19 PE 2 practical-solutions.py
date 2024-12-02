##############
# Question 1 #
##############

def count_ways(n):
    if n < 0:
        return 0
    if n <= 1:
        return 1
    else:
        return count_ways(n-1) + count_ways(n-2)

# Iterative
def count_ways(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return b


def count_k_ways(n, k):
    if n < 0:
        return 0
    if n <= 1:
        return 1
    else:
        return sum(count_k_ways(n-x, k) for x in range(1,k+1))

# Iterative
def count_k_ways(n, k):
    a = [0]*(k-1) + [1]
    for i in range(n):
        a.append(sum(a))
        a.pop(0)
    return a[-1]


# Tests
def test_q1a():
    print(count_ways(1))
    print(count_ways(4))
    print(count_ways(6))


def test_q1b():
    print(count_k_ways(3, 4))
    print(count_k_ways(4, 3))
    print(count_k_ways(10, 4))
    print(count_k_ways(20, 6))


# Uncomment to test
##test_q1a()
##test_q1b()



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


### Your answer here.
# Q2A
def gender(fname, month):
    data = read_csv(fname)[1:]
    dow = {}
    for row in data:
        if int(row[3]) != month:
            continue
        if row[1] not in dow:
            dow[row[1]] = {}
        d = dow[row[1]]

        if row[7] not in d:
            d[row[7]] = 0
        d[row[7]] += 1

    for k, v in dow.items():
        total = sum(v.values())
        d = {}
        if "Male" in v:
            d["Male"] = round(v["Male"]/total, 2)
        else:
            d["Male"] = round(0/total, 2)
        if "Female" in v:
            d["Female"] = round(v["Female"]/total, 2)
        else:
            d["Female"] = round(0/total, 2)
        dow[k] = d
        
    return dow


# Q2B      
def count_light(fname, month):
    data = read_csv(fname)[1:]
    dow = {}
    for row in data:
        if int(row[3]) != month:
            continue
        if row[5] not in dow:
            dow[row[5]] = []

        if row[0] not in dow[row[5]]:
            dow[row[5]].append(row[0])
        

    for k, v in dow.items():
        dow[k] = len(v)
    return dow



# Tests
def test_q2a():
    print(gender("accidents.csv", 1) == \
        {'Serious': {'Male': 0.69, 'Female': 0.25}, 'Slight': {'Male': 0.63, 'Female': 0.3}, 'Fatal': {'Male': 0.78, 'Female': 0.21}})

    print(gender("accidents.csv", 6) == \
        {'Slight': {'Male': 0.64, 'Female': 0.29}, 'Serious': {'Male': 0.7, 'Female': 0.24}, 'Fatal': {'Male': 0.78, 'Female': 0.22}})

    print(gender("accidents.csv", 12) == \
        {'Slight': {'Male': 0.63, 'Female': 0.28}, 'Serious': {'Male': 0.7, 'Female': 0.23}, 'Fatal': {'Male': 0.74, 'Female': 0.23}})  


def test_q2b():
    print(count_light("accidents.csv", 1) == \
        {'Daylight': 6084, 'Darkness - lights lit': 4150, 'Darkness - no lighting': 1027, 'Darkness - lighting unknown': 305, 'Darkness - lights unlit': 116, 'Data missing or out of range': 6})

    print(count_light("accidents.csv", 6) == \
        {'Daylight': 9778, 'Darkness - lights lit': 900, 'Darkness - lighting unknown': 93, 'Darkness - lights unlit': 30, 'Darkness - no lighting': 245})

    print(count_light("accidents.csv", 11) == \
        {'Darkness - lights unlit': 129, 'Darkness - lights lit': 4426, 'Daylight': 6887, 'Darkness - no lighting': 975, 'Darkness - lighting unknown': 324})


##test_q2a()
##test_q2b()

    

##############
# Question 3 #
##############

class Dragon:
    def __init__(self, name):
        self.name = name
        self.alpha = None
        self.followers = []

    def command(self, dragon, order):
        if self.alpha or self.followers == []:
            return f"{self.name} is not an alpha"        
        if dragon == self:
            return f"{self.name} cannot command itself"
        if dragon.alpha != self:
            return f"{self.name} is not the alpha of {dragon.name}"
        if dragon.alpha == self:
            return f"{self.name} commands {dragon.name} to {order}"

    def defeat(self, dragon):
        if self == dragon:
            return f"{self.name} cannot defeat itself"
        if dragon.alpha == self:
            return f"{self.name} is already alpha of {dragon.name}"
        if dragon.alpha:
            return f"{dragon.name} is following {dragon.alpha.name}"
        if self.alpha:
            self.alpha.followers.remove(self)
            self.alpha = None
        dragon.alpha = self
        self.followers.append(dragon)
        for d in dragon.followers:
            d.alpha = self
            self.followers.append(d)
        dragon.followers = []
        return f"{self.name} becomes alpha of {dragon.name}"

    def who_is_alpha(self):
        if self.alpha:
            return f"{self.name} alpha is {self.alpha.name}"
        if self.followers:
            return f"{self.name} is alpha"
        else:
            return f"{self.name} has no alpha"


# Test cases

def test_q3():
    valka_bewilderbeast = Dragon("Bewilderbeast")
    drago_bewilderbeast = Dragon("Bewilderbeast")
    cloudjumper = Dragon("Cloudjumper")
    toothless = Dragon("Toothless")
    stormfly = Dragon("StormFly")
    meatlug = Dragon("Meatlug")
    reddragon = Dragon("Red Dragon")

    _=cloudjumper.who_is_alpha(); print(_ == "Cloudjumper has no alpha", "\tcloudjumper.who_is_alpha():\t", _)
    _=valka_bewilderbeast.defeat(cloudjumper); print(_ == "Bewilderbeast becomes alpha of Cloudjumper", "\tvalka_bewilderbeast.defeat(cloudjumper):\t", _)
    _=cloudjumper.who_is_alpha(); print(_ == "Cloudjumper alpha is Bewilderbeast", "\tcloudjumper.who_is_alpha():\t", _)
    _=valka_bewilderbeast.who_is_alpha(); print(_ == "Bewilderbeast is alpha", "\tvalka_bewilderbeast.who_is_alpha():\t", _)
    _=valka_bewilderbeast.command(valka_bewilderbeast, 'go find Hiccup'); print(_ == "Bewilderbeast cannot command itself", "\tvalka_bewilderbeast.command(valka_bewilderbeast, 'go find Hiccup'):\t", _)
    _=valka_bewilderbeast.command(cloudjumper, 'go find Hiccup'); print(_ == "Bewilderbeast commands Cloudjumper to go find Hiccup", "\tvalka_bewilderbeast.command(cloudjumper, 'go find Hiccup'):\t", _)
    _=cloudjumper.command(valka_bewilderbeast, 'get me food'); print(_ == "Cloudjumper is not an alpha", "\tcloudjumper.command(valka_bewilderbeast, 'get me food'):\t", _)
    _=drago_bewilderbeast.command(cloudjumper, 'go find Hiccup'); print(_ == "Bewilderbeast is not an alpha", "\tdrago_bewilderbeast.command(cloudjumper, 'go find Hiccup'):\t", _)
    _=drago_bewilderbeast.defeat(valka_bewilderbeast); print(_ == "Bewilderbeast becomes alpha of Bewilderbeast", "\tdrago_bewilderbeast.defeat(valka_bewilderbeast):\t", _)
    _=drago_bewilderbeast.command(cloudjumper, 'go find Hiccup'); print(_ == "Bewilderbeast commands Cloudjumper to go find Hiccup", "\tdrago_bewilderbeast.command(cloudjumper, 'go find Hiccup'):\t", _)
    _=cloudjumper.who_is_alpha(); print(_ == "Cloudjumper alpha is Bewilderbeast", "\tcloudjumper.who_is_alpha():\t", _)
    _=valka_bewilderbeast.who_is_alpha(); print(_ == "Bewilderbeast alpha is Bewilderbeast", "\tvalka_bewilderbeast.who_is_alpha():\t", _)
    _=toothless.defeat(stormfly); print(_ == "Toothless becomes alpha of StormFly", "\ttoothless.defeat(stormfly):\t", _)
    _=toothless.defeat(meatlug); print(_ == "Toothless becomes alpha of Meatlug", "\ttoothless.defeat(meatlug):\t", _)
    _=drago_bewilderbeast.command(toothless, 'kill Hiccup'); print(_ == "Bewilderbeast is not the alpha of Toothless", "\tdrago_bewilderbeast.command(toothless, 'kill Hiccup'):\t", _)
    _=drago_bewilderbeast.defeat(toothless); print(_ == "Bewilderbeast becomes alpha of Toothless", "\tdrago_bewilderbeast.defeat(toothless):\t", _)
    _=drago_bewilderbeast.command(toothless, 'kill Hiccup'); print(_ == "Bewilderbeast commands Toothless to kill Hiccup", "\tdrago_bewilderbeast.command(toothless, 'kill Hiccup'):\t", _)
    _=toothless.who_is_alpha(); print(_ == "Toothless alpha is Bewilderbeast", "\ttoothless.who_is_alpha():\t", _)
    _=toothless.defeat(reddragon); print(_ == "Toothless becomes alpha of Red Dragon", "\ttoothless.defeat(reddragon):\t", _)
    _=toothless.who_is_alpha(); print(_ == "Toothless is alpha", "\ttoothless.who_is_alpha():\t", _)
    _=stormfly.who_is_alpha(); print(_ == "StormFly alpha is Bewilderbeast", "\tstormfly.who_is_alpha():\t", _)
    _=meatlug.who_is_alpha(); print(_ == "Meatlug alpha is Bewilderbeast", "\tmeatlug.who_is_alpha():\t", _)
    _=drago_bewilderbeast.command(toothless, 'kill Hiccup'); print(_ == "Bewilderbeast is not the alpha of Toothless", "\tdrago_bewilderbeast.command(toothless, 'kill Hiccup'):\t", _)
    _=toothless.defeat(drago_bewilderbeast); print(_ == "Toothless becomes alpha of Bewilderbeast", "\ttoothless.defeat(drago_bewilderbeast):\t", _)
    _=toothless.who_is_alpha(); print(_ == "Toothless is alpha", "\ttoothless.who_is_alpha():\t", _)
    _=toothless.defeat(cloudjumper); print(_ == "Toothless is already alpha of Cloudjumper", "\ttoothless.defeat(cloudjumper):\t", _)
    _=drago_bewilderbeast.who_is_alpha(); print(_ == "Bewilderbeast alpha is Toothless", "\tdrago_bewilderbeast.who_is_alpha():\t", _)
    _=cloudjumper.who_is_alpha(); print(_ == "Cloudjumper alpha is Toothless", "\tcloudjumper.who_is_alpha():\t", _)
    _=valka_bewilderbeast.who_is_alpha(); print(_ == "Bewilderbeast alpha is Toothless", "\tvalka_bewilderbeast.who_is_alpha():\t", _)
    _=stormfly.who_is_alpha(); print(_ == "StormFly alpha is Toothless", "\tstormfly.who_is_alpha():\t", _)
    _=meatlug.who_is_alpha(); print(_ == "Meatlug alpha is Toothless", "\tmeatlug.who_is_alpha():\t", _)
    _=reddragon.who_is_alpha(); print(_ == "Red Dragon alpha is Toothless", "\treddragon.who_is_alpha():\t", _)
    
# Uncomment to test question 3
##test_q3()    

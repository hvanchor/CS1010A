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


def count_k_ways(n, k):
    if n < 0:
        return 0
    if n <= 1:
        return 1
    else:
        return sum(count_k_ways(n-x, k) for x in range(1,k+1))


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
def gender(filename, month):
    data = filter(lambda x: x[3] == str(month), read_csv(filename)[1:])
    d1 = {}

    for row in data:
        severity = row[1]
        gender = row[-1]

        if severity not in d1:
            d1[severity] = {}
        if gender not in d1[severity]:
            d1[severity][gender] = 0
        d1[severity][gender] += 1


    for k, v in d1.items():
        total = sum(v.values())
        d2 = {}
        if "Male" in v:
            d2["Male"] = round(v["Male"] / total, 2)
        else:
            d2["Male"] = round(0 / total, 2)
        if "Female" in v:
            d2["Female"] = round(v["Female"] / total, 2)
        else:
            d2["Female"] = round(0 / total, 2)
        d1[k] = d2
    return d1






# Q2B      
def count_light(filename, month):
    data = filter(lambda x: x[3] == str(month), read_csv(filename)[1:])
    d = {}
    for row in data:
        accident = row[0]
        lighting = row[5]
        if lighting not in d:
            d[lighting] = []
        if accident not in d[lighting]:
            d[lighting].append(accident)

    for k, v in d.items():
        d[k] = len(v)
    return d


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


#test_q2a()
#test_q2b()

    

##############
# Question 3 #
##############

class Dragon:
    def __init__(self, name):
        self.name = name
        self.alpha = None
        self.followers = []

    def who_is_alpha(self):
        if self.followers:
            return f"{self.name} is alpha"
        elif self.alpha:
            return f"{self.name} alpha is {self.alpha.name}"
        else:
            return f"{self.name} has no alpha"

    def command(self, other, order):
        if self.alpha or not self.followers:
            return f"{self.name} is not an alpha"
        elif self == other:
            return f"{self.name} cannot command itself"
        elif self != other.alpha:
            return f"{self.name} is not the alpha of {other.name}"
        else:
            return f"{self.name} commands {other.name} to {order}"

    def defeat(self, other):
        if self == other:
            return f"{self.name} cannot defeat itself"
        if self == other.alpha:
            return f"{self.name} is already alpha of {other.name}"
        if other.alpha:
            return f"{other.name} is following {other.alpha.name}"
        if self.alpha:
            self.alpha.followers.remove(self)
            self.alpha = None
        other.alpha = self
        self.followers.append(other)
        for d in other.followers:
            d.alpha = self
            self.followers.append(d)
        other.followers = []
        return f"{self.name} becomes alpha of {other.name}"





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
test_q3()

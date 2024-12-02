#******************************************************
#*
#*  CS1010S Re-Practical Exam
#*  AY2016/2017, Semester 2
#*  Name: <fill in your name here>
#*
#*  This template is to be used if Coursemology fails.
#*  Otherwise, answers should be uploaded to Coursemology
#*  directly. 
#*
#******************************************************

#------------#
# Question 1 #
#------------#

def check_digit(digits, table):
    # sum the digits
    total = 0
    for d in digits:
        total += int(d)

    # modulo the total
    total %= len(table)
    return table[total]

def check_digit(digits, table):
    return table[sum(int(x) for x in digits) % len(table)]



nus_matric = {
    0: 'Y',
    1: 'X',
    2: 'W',
    3: 'U',
    4: 'R',
    5: 'N',
    6: 'M',
    7: 'L',
    8: 'J',
    9: 'H',
    10: 'E',
    11: 'A',
    12: 'B'
}
# Uncomment to test
##print(check_digit("0113093", nus_matric))
##print(check_digit("0129969", nus_matric))


def weighted_check_digit(digits, table, weights):
    # sum with weights
    total = 0
    for i in range(len(digits)):
        total += int(digits[i]) * int(weights[i])

    # modulo the total
    total %= len(table)
    return table[total]


sg_nric = dict(enumerate("JZIHGFEDCBA"))
sg_weights = "2765432"

# Uncomment to test
##print(weighted_check_digit("9702743", sg_nric, sg_weights))
##print(weighted_check_digit("9875133", sg_nric, sg_weights))


#------------#
# Question 2 #
#------------#

import csv
def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    rows = []

    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows


def oversub_avg(fname, year):
    data = read_csv(fname)
    data = filter(lambda x:x[0] == year, data)

    d = {}
    for row in data:
        category = row[3]
        if category not in d:
            d[category] = []
        rate = float(row[6])/float(row[5])
        d[category].append(rate)

    for cat, rates in d.items():
        d[cat] = round(sum(rates)/len(rates), 3)

    return d


# Uncomment to test
##print(oversub_avg("coe.csv", "2013"))
##print(oversub_avg("coe.csv", "2015"))


def most_oversub(fname, year):
    data = filter(lambda x:x[0] == year, read_csv(fname))
    
    rounds = {}
    most = {}

    for row in data:
        category = row[3]
        if category not in most:
            most[category] = 0

        rnd = (row[1], row[2])
        rate = float(row[6])/float(row[5])
        if rnd not in rounds or rounds[rnd][0] < rate:
            rounds[rnd] = [rate, category]
        elif rounds[rnd][0] == rate:
            rounds[rnd].append(category)
    
    for rate, cat in rounds.values():
        most[cat] += 1

    return most

# Uncomment to test
##print(most_oversub("coe.csv", "2013"))     
##print(most_oversub("coe.csv", "2015")) 



#------------#
# Question 3 #
#------------#

class Monster:
    def __init__(self, name, scariness):
        self.name = name
        self.scariness = scariness
        self.door = None
        self.energy = 0

    def get_name(self):
        return self.name

    def get_energy(self):
        return self.energy

    def get_location(self):
        if self.door:
            return "{} is in {}".format(self.name,
                                        self.door.name)
        else:
            return "{} is on the Scream Floor".format(self.name)

    def enter(self, door):
        if self.door == door:
            return "{} has already entered {}".format(self.name, door.name)
        elif self.door:
            return "{} is currently in {}".format(self.name, self.door.name)
        else:
            # enters the room
            self.door = door
            door.monsters.append(self)
            if self not in door.seen:
                door.seen[self] = 1
            return "{} enters {}".format(self.name, door.name)

    def scare(self):
        door = self.door
        if not door:
            return "{} has not entered any door".format(self.name)
    
        # remove monsters from door
        monsters = door.monsters
        monsters_name = door.get_monsters()
        door.monsters = []

        scariness = 0
        for m in monsters:
            m.door = None            
            scariness += m.scariness/door.seen[m] # determine scariness
            door.seen[m] += 1 # increase monsters seen

        energy = scariness - door.bravery
        door.bravery += len(monsters)

        if energy <= 0:            
            return "{} failed to obtain energy from {}".format(monsters_name, door.name)
        else:
            for m in monsters:                
                 m.energy += energy / len(monsters) # split the energy obtained
            return "{} got {} energy from {}".format(monsters_name, energy, door.name)
            

class Door:
    def __init__(self, name, bravery):
        self.name = name
        self.bravery = bravery
        self.seen = {}
        self.monsters = []
        

    def get_bravery(self):
        return self.bravery

    def get_monsters(self):
        return ", ".join(sorted(m.name for m in self.monsters))



## helper function. Do NOT modify. No need to paste on Coursemology
def leaderboard(*monsters):
    return "\n".join("{}: {}".format(m.get_name(),
                                     round(m.get_energy(), 2)) for m in
                     sorted(monsters, key=lambda x:float(x.get_energy()), reverse=True))

# Sample run test case
def test_q3():
    sully = Monster("Sully", 12)
    mike = Monster("Mike", 1)
    randall = Monster("Randall", 8)

    mary = Door("Mary's Room", 1)
    ted = Door("Ted's Room", 1)
    boo = Door("Boo's Room", 21)
        
    _=leaderboard(sully, mike, randall); print(_ == """Sully: 0
Mike: 0
Randall: 0""", '\tleaderboard(sully, mike, randall):\t', _)
    _=sully.get_energy(); print(_ == 0, '\tsully.get_energy():\t', _)
    _=sully.get_location(); print(_ == "Sully is on the Scream Floor", '\tsully.get_location():\t', _)
    _=sully.enter(mary); print(_ == "Sully enters Mary's Room", '\tsully.enter(mary):\t', _)
    _=sully.get_location(); print(_ == "Sully is in Mary's Room", '\tsully.get_location():\t', _)
    _=mary.get_monsters(); print(_ == "Sully", '\tmary.get_monsters():\t', _)
    _=sully.scare(); print(_ == "Sully got 11.0 energy from Mary's Room", '\tsully.scare():\t', _)
    _=leaderboard(sully, mike, randall); print(_ == """Sully: 11.0
Mike: 0
Randall: 0""", '\tleaderboard(sully, mike, randall):\t', _)
    _=mary.get_bravery(); print(_ == 2, '\tmary.get_bravery():\t', _)
    _=sully.get_location(); print(_ == "Sully is on the Scream Floor", '\tsully.get_location():\t', _)
    _=randall.scare(); print(_ == "Randall has not entered any door", '\trandall.scare():\t', _)
    _=randall.enter(mary); print(_ == "Randall enters Mary's Room", '\trandall.enter(mary):\t', _)
    _=randall.scare(); print(_ == "Randall got 6.0 energy from Mary's Room", '\trandall.scare():\t', _)
    _=sully.enter(mary); print(_ == "Sully enters Mary's Room", '\tsully.enter(mary):\t', _)
    _=sully.enter(ted); print(_ == "Sully is currently in Mary's Room", '\tsully.enter(ted):\t', _)
    _=mary.get_bravery(); print(_ == 3, '\tmary.get_bravery():\t', _)
    _=sully.scare(); print(_ == "Sully got 3.0 energy from Mary's Room", '\tsully.scare():\t', _)
    _=mary.get_bravery(); print(_ == 4, '\tmary.get_bravery():\t', _)
    _=sully.enter(mary); print(_ == "Sully enters Mary's Room", '\tsully.enter(mary):\t', _)
    _=sully.scare(); print(_ == "Sully failed to obtain energy from Mary's Room", '\tsully.scare():\t', _)
    _=randall.enter(mary); print(_ == "Randall enters Mary's Room", '\trandall.enter(mary):\t', _)
    _=randall.scare(); print(_ == "Randall failed to obtain energy from Mary's Room", '\trandall.scare():\t', _)
    _=mary.get_bravery(); print(_ == 6, '\tmary.get_bravery():\t', _)
    _=randall.get_location(); print(_ == "Randall is on the Scream Floor", '\trandall.get_location():\t', _)
    _=sully.enter(ted); print(_ == "Sully enters Ted's Room", '\tsully.enter(ted):\t', _)
    _=mike.enter(ted); print(_ == "Mike enters Ted's Room", '\tmike.enter(ted):\t', _)
    _=leaderboard(sully, mike, randall); print(_ == """Sully: 14.0
Randall: 6.0
Mike: 0""", '\tleaderboard(sully, mike, randall):\t', _)
    _=ted.get_monsters(); print(_ == "Mike, Sully", '\tted.get_monsters():\t', _)
    _=ted.get_bravery(); print(_ == 1, '\tted.get_bravery():\t', _)
    _=mike.scare(); print(_ == "Mike, Sully got 12.0 energy from Ted's Room", '\tmike.scare():\t', _)
    _=leaderboard(sully, mike, randall); print(_ == """Sully: 20.0
Mike: 6.0
Randall: 6.0""", '\tleaderboard(sully, mike, randall):\t', _)
    _=ted.get_bravery(); print(_ == 3, '\tted.get_bravery():\t', _)
    _=sully.enter(ted); print(_ == "Sully enters Ted's Room", '\tsully.enter(ted):\t', _)
    _=mike.enter(ted); print(_ == "Mike enters Ted's Room", '\tmike.enter(ted):\t', _)
    _=randall.enter(ted); print(_ == "Randall enters Ted's Room", '\trandall.enter(ted):\t', _)
    _=randall.scare(); print(_ == "Mike, Randall, Sully got 11.5 energy from Ted's Room", '\trandall.scare():\t', _)
    _=ted.get_bravery(); print(_ == 6, '\tted.get_bravery():\t', _)
    _=sully.enter(boo); print(_ == "Sully enters Boo's Room", '\tsully.enter(boo):\t', _)
    _=mike.enter(boo); print(_ == "Mike enters Boo's Room", '\tmike.enter(boo):\t', _)
    _=randall.enter(boo); print(_ == "Randall enters Boo's Room", '\trandall.enter(boo):\t', _)
    _=sully.scare(); print(_ == "Mike, Randall, Sully failed to obtain energy from Boo's Room", '\tsully.scare():\t', _)
    _=mike.get_energy(); print(_ == 9.833333333333334, '\tmike.get_energy():\t', _)
    _=leaderboard(sully, mike, randall); print(_ == """Sully: 23.83
Mike: 9.83
Randall: 9.83""", '\tleaderboard(sully, mike, randall):\t', _)

# Uncomment to test
test_q3()

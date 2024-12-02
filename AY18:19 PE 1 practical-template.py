##############
# Question 1 #
##############

def floyd_row(n):
    i = 1
    for j in range(1, n):
        i += j
    return tuple(range(i, i+n))



def floyd_sum(n):
    result = 0
    for i in range(1, n+1):
        result += sum(floyd_row(i))
    return result




# Tests
def test_q1a():
    print(floyd_row(1))
    print(floyd_row(2))
    print(floyd_row(5))


def test_q1b():
    print(floyd_sum(1))
    print(floyd_sum(2))
    print(floyd_sum(5))


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

    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows


### Your answer here.
# Q2A
def regional_sales(filename, platform, year):
    data = filter(lambda x: x[2] == str(year) and x[1] == platform, read_csv(filename)[1:])
    results = [0, 0, 0, 0, 0]
    for row in data:
        for i in range(5):
            if row[5+1] != "N/A":
                results[i] += float(row[5+i])
    for j in range(5):
        results[j] = round(results[j], 2)
    return tuple(results)


# Q2B      
def trending_genre(filename, platform):
    data = filter(lambda x: x[1] == platform, read_csv(filename)[1:])
    d = {}
    for row in data:
        if row[2] != "N/A" and row[3] != "N/A":
            year, genre = int(row[2]), row[3]
            total = float(row[9])
            sales = sum(map(float, row[5:9]))

            if year not in d:
                d[year] = {}
            if genre not in d[year]:
                d[year][genre] = 0
            d[year][genre] += sales

    result = {}
    for year, genre in d.items():
        inc = []
        for genre, sales in genre.items():
            if year-1 in d and genre in d[year-1] and d[year-1][genre] != 0:
                inc.append((round((sales - d[year-1][genre])*100/d[year-1][genre], 2), genre))
        if inc == []:
            continue
        inc.sort(key=lambda x: (-x[0], x[1]))
        result[year] = inc[0][1]

    return result





# Tests
def test_q2a():
    print(regional_sales("vgsales.csv", "X360", 2016))
    print(regional_sales("vgsales.csv", "3DS", 2012))

def test_q2b():
    print(trending_genre("vgsales.csv", "PS3") == \
        {2013: 'Misc', 2014: 'Misc', 2015: 'Simulation', 2016: 'Role-Playing'})
    print(trending_genre("vgsales.csv", "PC") == \
        {2013: 'Misc', 2014: 'Simulation', 2015: 'Strategy', 2016: 'Adventure'})


#test_q2a()
#test_q2b()

    

##############
# Question 3 #
##############

class Stone:
    def __init__(self, name, *powers):
        self.name = name
        self.powers = list(powers)
        self.destroyed = False
        self.artifact = None

    def imbue(self, power):
        if self.destroyed:
            return f"{self.name} already destroyed"
        if power in self.powers:
            return f"{self.name} already imbued with the power {power}"
        else:
            self.powers.append(power)
            return f"{self.name} is now imbued with the power {power}"

    def disarm(self, power):
        if self.destroyed:
            return f"{self.name} already destroyed"
        if power not in self.powers:
            return f"{self.name} is not imbued with the power {power}"
        else:
            self.powers.remove(power)
            return f"{self.name} is no longer imbued with the power {power}"

    def destroy(self):
        if self.destroyed:
            return f"{self.name} already destroyed"
        else:
            self.destroyed = True
            if self.artifact:
                self.artifact.remove_stone(self)
            return f"{self.name} is now destroyed"

    def list_powers(self):
        if self.destroyed:
            return ()
        else:
            return self.powers

class Artefact:
    def __init__(self, name, *stones):
        self.name = name
        self.others = []
        self.stones = []
        for stone in stones:
            self.add_stone(stone)

    def add_stone(self, stone):
        if stone.destroyed:
            return f"{stone.name} is already destroyed"
        if stone.artifact == self:
            return f"{self.name} already has {stone.name}"
        if stone.artifact:
            return f"{stone.name} is already part of {stone.artifact.name}"
        else:
            self.stones.append(stone)
            stone.artifact = self
            return f"{stone.name} is added to {self.name}"

    def remove_stone(self, stone):
        if stone not in self.stones:
            return f"{self.name} does not contain {stone.name}"
        else:
            stone.artifact = None
            self.stones.remove(stone)
            return f"{stone.name} is removed from {self.name}"

    def combine(self, other):
        if self == other:
            return f"Cannot combine {self.name} with itself"
        if other in self.others:
            return f"{self.name} is already combined with {other.name}"
        else:
            for artifact1 in other.others + [other]:
                for artifact2 in self.others + [self]:
                    if artifact1 not in artifact2.others:
                        artifact2.others.append(artifact1)
                    if artifact2 not in artifact1.others:
                        artifact1.others.append(artifact2)
            return f"{self.name} combines with {other.name}"

    def invoke(self):
        powers = []
        for artifact in self.others + [self]:
            for stone in artifact.stones:
                for power in stone.powers:
                    if power not in powers:
                        powers.append(power)
        return tuple(powers)







# Test cases

def test_q3():
    power_stone   = Stone("Power Stone", "Attack", "Defense")
    mind_stone    = Stone("Mind Stone", "Brainwash")
    time_stone    = Stone("Time Stone")
    reality_stone = Stone("Reality Stone", "Illusion")

    vision          = Artefact("Vision", mind_stone)
    gauntlet        = Artefact("Gauntlet", power_stone)
    eye_of_agamotto = Artefact("Eye of Agamoto")

    mind_stone_remade = Stone("Mind Stone", "Brainwash", "Illusion")

    _=power_stone.imbue("Attack"); print(_ == "Power Stone already imbued with the power Attack", "\tpower_stone.imbue('Attack'):\t", _)
    _=power_stone.imbue("Strength"); print(_ == "Power Stone is now imbued with the power Strength", "\tpower_stone.imbue('Strength'):\t", _)
    _=power_stone.list_powers(); print(tuple(sorted(_)) == ('Attack', 'Defense', 'Strength'), "\tpower_stone.list_powers():\t", _)
    _=time_stone.imbue("Repeat"); print(_ == "Time Stone is now imbued with the power Repeat", "\ttime_stone.imbue('Repeat'):\t", _)
    _=time_stone.imbue("Undo"); print(_ == "Time Stone is now imbued with the power Undo", "\ttime_stone.imbue('Undo'):\t", _)
    _=vision.add_stone(mind_stone); print(_ == "Vision already has Mind Stone", "\tvision.add_stone(mind_stone):\t", _)
    _=vision.remove_stone(power_stone); print(_ == "Vision does not contain Power Stone", "\tvision.remove_stone(power_stone):\t", _)
    _=vision.remove_stone(mind_stone); print(_ == "Mind Stone is removed from Vision", "\tvision.remove_stone(mind_stone):\t", _)
    _=vision.add_stone(mind_stone); print(_ == "Mind Stone is added to Vision", "\tvision.add_stone(mind_stone):\t", _)
    _=vision.invoke(); print(tuple(sorted(_)) == ('Brainwash',), "\tvision.invoke():\t", _)
    _=vision.add_stone(power_stone); print(_ == "Power Stone is already part of Gauntlet", "\tvision.add_stone(power_stone):\t", _)
    _=mind_stone.disarm("AI"); print(_ == "Mind Stone is not imbued with the power AI", "\tmind_stone.disarm('AI'):\t", _)
    _=mind_stone.destroy(); print(_ == "Mind Stone is now destroyed", "\tmind_stone.destroy():\t", _)
    _=mind_stone.disarm("Brainwash"); print(_ == "Mind Stone already destroyed", "\tmind_stone.disarm('Brainwash'):\t", _)
    _=vision.remove_stone(mind_stone); print(_ == "Vision does not contain Mind Stone", "\tvision.remove_stone(mind_stone):\t", _)
    _=eye_of_agamotto.add_stone(time_stone); print(_ == "Time Stone is added to Eye of Agamoto", "\teye_of_agamotto.add_stone(time_stone):\t", _)
    _=vision.combine(eye_of_agamotto); print(_ == "Vision combines with Eye of Agamoto", "\tvision.combine(eye_of_agamotto):\t", _)
    _=eye_of_agamotto.combine(vision); print(_ == "Eye of Agamoto is already combined with Vision", "\teye_of_agamotto.combine(vision):\t", _)
    _=gauntlet.add_stone(mind_stone); print(_ == "Mind Stone is already destroyed", "\tgauntlet.add_stone(mind_stone):\t", _)
    _=gauntlet.add_stone(mind_stone_remade); print(_ == "Mind Stone is added to Gauntlet", "\tgauntlet.add_stone(mind_stone_remade):\t", _)
    _=gauntlet.invoke(); print(tuple(sorted(_)) == ('Attack', 'Brainwash', 'Defense', 'Illusion', 'Strength'), "\tgauntlet.invoke():\t", _)
    _=gauntlet.add_stone(reality_stone); print(_ == "Reality Stone is added to Gauntlet", "\tgauntlet.add_stone(reality_stone):\t", _)
    _=gauntlet.invoke(); print(tuple(sorted(_)) == ('Attack', 'Brainwash', 'Defense', 'Illusion', 'Strength'), "\tgauntlet.invoke():\t", _)
    _=gauntlet.combine(eye_of_agamotto); print(_ == "Gauntlet combines with Eye of Agamoto", "\tgauntlet.combine(eye_of_agamotto):\t", _)
    _=gauntlet.combine(vision); print(_ == "Gauntlet is already combined with Vision", "\tgauntlet.combine(vision):\t", _)
    _=gauntlet.invoke(); print(tuple(sorted(_)) == ('Attack', 'Brainwash', 'Defense', 'Illusion', 'Repeat', 'Strength', 'Undo'), "\tgauntlet.invoke():\t", _)



# Uncomment to test question 3
test_q3()

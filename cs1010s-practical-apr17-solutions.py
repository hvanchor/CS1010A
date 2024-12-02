##############
# Question 1 #
##############

def l33tify(string, code):
    new = ""
    for s in string:        
        if s in code:
            new += code[s]
        else:
            new += s
    return new


l33t_dict = {
    'a': '4',
    'b': '8',
    'c': '(',
    'e': '3',
    'g': '[',
    'i': '1',
    'o': '0',
    's': '5',
    't': '7',
    'x': '%',
    'z': '2',
    }

# Uncomment to test
##print(l33tify("pheer my leet skills", l33t_dict))
##print(l33tify("python is cool", l33t_dict))


def advance_l33tify(string, code):
    # make a copy of the dict
    d = {}
    for k,v in code.items():
        d[k] = v.copy()
    
    new = ""
    for s in string:        
        if s.lower() in code:
            s = s.lower()
            new += d[s][0]
            # rotate the first entry to the last
            d[s].append(d[s].pop(0))
        else:
            new += s
    return new


adv_l33t_dict = {
    'a': ['4', '/-\\', '/_\\', '@', '/\\'],
    'b': ['8', '|3', '13', '|}', '|:', '|8', '18', '6', '|B'],
    'c': ['<', '{', '[', '('],
    'd': ['|)', '|}', '|]'],
    'e': ['3'],
    'f': ['|=', 'ph', '|#', '|"'],
    'g': ['[', '-', '[+', '6'],
    'h': ['|-|', '[-]', '{-}', '|=|', '[=]', '{=}'],
    'i': ['1', '|'],
    'j': ['_|', '_/', '_7', '_)'],
    'k': ['|<', '1<'],
    'l': ['|_', '|', '1'],
    'm': ['|\\/|', '^^', '/\\/\\'],
    'n': ['|\\|', '/\\/', '/V', '][\\\\]['],
    'o': ['0', '()', '[]', '{}'],
    'p': ['|o', '|O', '|>', '|*', '|°', '|D', '/o'],
    'q': ['O_', '9', '(', ')', ''],
    'r': ['|2', '12', '.-', '|^'],
    's': ['5', '$', '§'],
    't': ['7', '+', '7`', "'|'"],
    'u': ['|_|', '\\_\\', '/_/', '\\_/', '(_)'],
    'v': ['\\/'],
    'w': ['\\/\\/', '(/\\)', '\\^/', '|/\\|'],
    'x': ['%', '*', '><', '}{', ')('],
    'y': ['`/', '¥'],
    'z': ['2', '7_', '>_']
    }

# Uncomment to test
##print(advance_l33tify("Bow b4 me 4 I am root!!!", adv_l33t_dict))
##print(advance_l33tify("Mississippi", adv_l33t_dict))


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

def yearly_average(fname, year):
    data = read_csv(fname)
    data = (x for x in data if x[0] == year)

    d = {}
    for year, month, telco, coverage in data:
        if telco not in d:
            d[telco] = []
        d[telco].append(float(coverage))

    for telco in d:
        d[telco] = round(sum(d[telco])/len(d[telco]), 4)

    return d


# Uncomment to test
##print(yearly_average("3g-coverage.csv", "2015"))
##print(yearly_average("3g-coverage.csv", "2013"))

def best_telco(fname, year):
    data = read_csv(fname)
    data = (x for x in data if x[0] == year)

    d = {}
    t = {}
    for year, month, telco, coverage in data:
        if telco not in t:
            t[telco] = 0            
        if month not in d:
            d[month] = []
        d[month].append((telco, float(coverage)))

    for month in d:
        telco = max(d[month], key=lambda x:x[1])[0]
        t[telco] += 1

    return t

# Uncomment to test
##print(best_telco("3g-coverage.csv", "2015"))
##print(best_telco("3g-coverage.csv", "2013"))



##############
# Question 3 #
##############

class Villain:
    def __init__(self, name):
        self.name = name
        self.evilness = 0
        self.gadgets = []
        self.proficiency = {}

    def get_evilness(self):
        return self.evilness

    def gadgets_owned(self):
        return tuple(map(lambda x: x.name, self.gadgets))

    def do_evil(self, action, gadget):
        if gadget not in self.gadgets:
            return self.name + " does not have " + gadget.name
        else:                        
            if gadget not in self.proficiency:
                self.proficiency[gadget] = 0
                
            self.evilness += gadget.awesomeness + self.proficiency[gadget]
            gadget.awesomeness = max(0, gadget.awesomeness - 1)
            self.proficiency[gadget] += 1
            return self.name + " " + action + " with " + gadget.name

    def get_proficiency(self, gadget):
        if gadget in self.proficiency:
            return self.name + "'s proficiency with " + gadget.name + " is " + str(self.proficiency[gadget])
        else:
            return self.name + " is not proficient with " + gadget.name
    
    def steals(self, gadget):
        if gadget in self.gadgets:
            return self.name + " already has " + gadget.name
        else:
            steal = ""
            if gadget.owner:
                steal = " from " + gadget.owner.name
                gadget.owner.evilness //= 2         # ex-owner's evilness decreases
                gadget.owner.gadgets.remove(gadget) # remove gadget from his possession

                            
            gadget.awesomeness = gadget.original            
            self.gadgets.append(gadget)
            gadget.owner = self
            return self.name + " steals " + gadget.name + steal

    def envy(self, other):
        if isinstance(other, Gadget):
            if not other.owner:
                return self.name + " envies " + other.name
            elif other.owner == self:
                return self.name + " already has " + other.name
            else:
                return self.name + " envies " + other.owner.name + "'s " + other.name
        elif isinstance(other, Villain):
            if other == self:
                return self.name + " cannot envy himself"
            elif other.evilness == self.evilness:
                return "Nobody is envious"
            elif other.evilness > self.evilness:
                return self.name + " envies " + other.name
            else:
                return other.name + " envies " + self.name
                
            
        

class Gadget:
    def __init__(self, name, awesomeness):
        self.name = name
        self.awesomeness = awesomeness
        self.original = awesomeness
        self.owner = None

    def get_description(self):
        return self.name + " has level " + str(self.awesomeness) + " awesomeness"

    def owned_by(self):
        if self.owner:
            return self.name + " belongs to " + self.owner.name
        else:
            return self.name + " is unowned"

# Sample run test case
def test_q3():
    gru = Villain("Gru")
    vector = Villain("Vector")
    freeze_ray = Gadget("Freeze Ray", 5)
    lava_gun = Gadget("Lava Lamp Gun", 3)
    
    _=gru.get_evilness(); print(_ == 0, '\tgru.get_evilness():\t', _)
    _=gru.gadgets_owned(); print(tuple(sorted(_)) == (), '\tgru.gadgets_owned():\t', _)
    _=freeze_ray.get_description(); print(_ == "Freeze Ray has level 5 awesomeness", '\tfreeze_ray.get_description():\t', _)
    _=freeze_ray.owned_by(); print(_ == "Freeze Ray is unowned", '\tfreeze_ray.owned_by():\t', _)
    _=gru.steals(freeze_ray); print(_ == "Gru steals Freeze Ray", '\tgru.steals(freeze_ray):\t', _)
    _=gru.gadgets_owned(); print(tuple(sorted(_)) == ('Freeze Ray',), '\tgru.gadgets_owned():\t', _)
    _=freeze_ray.owned_by(); print(_ == "Freeze Ray belongs to Gru", '\tfreeze_ray.owned_by():\t', _)
    _=gru.get_proficiency(freeze_ray); print(_ == "Gru is not proficient with Freeze Ray", '\tgru.get_proficiency(freeze_ray):\t', _)
    _=gru.do_evil("robs a bank", freeze_ray); print(_ == "Gru robs a bank with Freeze Ray", '\tgru.do_evil("robs a bank", freeze_ray):\t', _)
    _=gru.get_evilness(); print(_ == 5, '\tgru.get_evilness():\t', _)
    _=gru.get_proficiency(freeze_ray); print(_ == "Gru's proficiency with Freeze Ray is 1", '\tgru.get_proficiency(freeze_ray):\t', _)
    _=freeze_ray.get_description(); print(_ == "Freeze Ray has level 4 awesomeness", '\tfreeze_ray.get_description():\t', _)
    _=gru.do_evil("steals candy", freeze_ray); print(_ == "Gru steals candy with Freeze Ray", '\tgru.do_evil("steals candy", freeze_ray):\t', _)
    _=gru.get_proficiency(freeze_ray); print(_ == "Gru's proficiency with Freeze Ray is 2", '\tgru.get_proficiency(freeze_ray):\t', _)
    _=gru.get_evilness(); print(_ == 10, '\tgru.get_evilness():\t', _)
    _=freeze_ray.get_description(); print(_ == "Freeze Ray has level 3 awesomeness", '\tfreeze_ray.get_description():\t', _)
    _=gru.envy(freeze_ray); print(_ == "Gru already has Freeze Ray", '\tgru.envy(freeze_ray):\t', _)
    _=vector.envy(freeze_ray); print(_ == "Vector envies Gru's Freeze Ray", '\tvector.envy(freeze_ray):\t', _)
    _=gru.envy(vector); print(_ == "Vector envies Gru", '\tgru.envy(vector):\t', _)
    _=vector.steals(freeze_ray); print(_ == "Vector steals Freeze Ray from Gru", '\tvector.steals(freeze_ray):\t', _)
    _=gru.get_evilness(); print(_ == 5, '\tgru.get_evilness():\t', _)
    _=freeze_ray.get_description(); print(_ == "Freeze Ray has level 5 awesomeness", '\tfreeze_ray.get_description():\t', _)
    _=freeze_ray.owned_by(); print(_ == "Freeze Ray belongs to Vector", '\tfreeze_ray.owned_by():\t', _)
    _=gru.gadgets_owned(); print(tuple(sorted(_)) == (), '\tgru.gadgets_owned():\t', _)
    _=vector.do_evil("freezes Miami", freeze_ray); print(_ == "Vector freezes Miami with Freeze Ray", '\tvector.do_evil("freezes Miami", freeze_ray):\t', _)
    _=vector.get_evilness(); print(_ == 5, '\tvector.get_evilness():\t', _)
    _=gru.envy(vector); print(_ == "Nobody is envious", '\tgru.envy(vector):\t', _)
    _=gru.envy(lava_gun); print(_ == "Gru envies Lava Lamp Gun", '\tgru.envy(lava_gun):\t', _)
    _=gru.do_evil("steals Freeze Ray", lava_gun); print(_ == "Gru does not have Lava Lamp Gun", '\tgru.do_evil("steals Freeze Ray", lava_gun):\t', _)
    _=gru.envy(lava_gun); print(_ == "Gru envies Lava Lamp Gun", '\tgru.envy(lava_gun):\t', _)
    _=gru.steals(lava_gun); print(_ == "Gru steals Lava Lamp Gun", '\tgru.steals(lava_gun):\t', _)
    _=gru.do_evil("steals the Queen\'s crown", lava_gun); print(_ == "Gru steals the Queen's crown with Lava Lamp Gun", '\tgru.do_evil("steals the Queen\'s crown", lava_gun):\t', _)
    _=gru.get_evilness(); print(_ == 8, '\tgru.get_evilness():\t', _)
    _=gru.steals(freeze_ray); print(_ == "Gru steals Freeze Ray from Vector", '\tgru.steals(freeze_ray):\t', _)
    _=vector.get_evilness(); print(_ == 2, '\tvector.get_evilness():\t', _)
    _=gru.get_evilness(); print(_ == 8, '\tgru.get_evilness():\t', _)
    _=gru.envy(vector); print(_ == "Vector envies Gru", '\tgru.envy(vector):\t', _)
    _=gru.gadgets_owned(); print(tuple(sorted(_)) == ('Freeze Ray', 'Lava Lamp Gun'), '\tgru.gadgets_owned():\t', _)
    _=gru.do_evil("freezes Vector", freeze_ray); print(_ == "Gru freezes Vector with Freeze Ray", '\tgru.do_evil("freezes Vector", freeze_ray):\t', _)
    _=gru.get_evilness(); print(_ == 15, '\tgru.get_evilness():\t', _)

# Uncomment to test
##test_q3()

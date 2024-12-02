###    
### Question 1 ###
###

### Your answer here.
# Q1A
def num_atoms(molecule):
    num = 0
    for c in molecule:
        if c.isalpha():
            num += 1
        elif c.isdigit():
            num += int(c) - 1
    return num

# Q1B
def molar_mass(molecule, table):
    atom = None  # save the previous atom
    mass = 0
    for c in molecule:
        if c.isalpha():
            atom = c
            mass += table[c]
        elif c.isdigit():
            mass += table[atom] * (int(c) - 1)
    return mass

# Or using index
def molar_mass(molecule, table):
    mass = 0
    for i in range(len(molecule)):
        if molecule[i].isalpha():
            mass += table[molecule[i]]
        if molecule[i].isdigit():
            mass += table[molecule[i-1]] * (int(molecule[i]) - 1)
    return mass


### Tests ###
def test_q1a():
    print(num_atoms("H2SO4"))  # sulphuric acid
    print(num_atoms("CH3CH2OH"))  # ethanol
    print(num_atoms("NH4CO2NH2")) # ammonium carbamate


def test_q1b():
    table = {'H':1.008,  'B':10.81 , 'C':12.011, 'N':14.007, 'O':15.999,
             'F':18.998, 'P':30.974, 'S':32.06,  'K':39.098, 'V':50.942,
             'Y':88.906, 'I':126.9,  'W':183.84, 'U':238.03}

    print(molar_mass("H2SO4", table))
    print(molar_mass("CH3CH2OH" ,table))
    print(molar_mass("NH4CO2NH2", table))


# Uncomment to test
##test_q1a()
##test_q1b()

    

###
### Question 2
###

import csv
def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    rows = []

    with open(csvfilename, encoding="utf-8") as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows


### Your answer here.
# Q2A
def top_10_titles(fname, year, weeks):
    data = read_csv(fname)
    del data[0]
    data = filter(lambda row: int(row[0]) in weeks and int(row[1]) == year, data)

    d = {}
    for row in data:
        if row[2] not in d:
            d[row[2]] = 0
        d[row[2]] += int(row[4])

    return tuple(sorted(d.items(), key=lambda x:x[1], reverse=True))[:10]



# Q2B
def top_10_studios(fname, year):
    data = read_csv(fname)
    del data[0]
    data = filter(lambda row: int(row[1]) == year, data)

    d = {}
    for row in data:
        title, studio, gross = row[2:5]
        if studio not in d:
            d[studio] = {}
        studio = d[studio]
        if title not in studio:
            studio[title] = 0
        studio[title] += int(gross)

    for studio, titles in d.items():
        d[studio] = round(sum(titles.values())/len(titles))

    return tuple(sorted(d.items(), key=lambda x:x[1], reverse=True))[:10]



### Tests ###
def test_q2a():
    # First 5 weeks of 2016
    print(top_10_titles('box-office.csv', 2016, (1, 2, 3, 4, 5)) ==
        (('Star Wars: The Force Awakens', 247104200),
         ('The Revenant', 141730884), 
         ("Daddy's Home", 79075678), 
         ('Ride Along 2', 72686830), 
         ('Kung Fu Panda 3', 48050957),
         ('13 Hours: The Secret Soldiers of Benghazi', 44892592),
         ('The Hateful Eight', 39324631), 
         ('The Big Short', 37955298), 
         ('Sisters', 37170845),
         ('Alvin and the Chipmunks: The Road Chip', 27779504)))

    # top 10 for 2010
    print(top_10_titles('box-office.csv', 2010, range(1,54)) ==
        (('Avatar', 466141929), 
         ('Toy Story 3', 415004880), 
         ('Alice in Wonderland (2010)', 334191110), 
         ('Iron Man 2', 312128345), 
         ('The Twilight Saga: Eclipse', 300531751), 
         ('Inception', 292576195), 
         ('Harry Potter and the Deathly Hallows Part 1', 285308372), 
         ('Despicable Me', 251266265), 
         ('Shrek Forever After', 238395990), 
         ('How to Train Your Dragon', 217581231)))

    # What you missed this semester
    print(top_10_titles('box-office.csv', 2017, range(32, 50)) ==
        (('It', 326748251), 
         ('Thor: Ragnarok', 253213000), 
         ('Annabelle: Creation', 102092201), 
         ('Kingsman: The Golden Circle', 99554816), 
         ('Blade Runner 2049', 88650463), 
         ("The Hitman's Bodyguard", 75468583), 
         ('The LEGO Ninjago Movie', 58683641), 
         ('Murder on the Orient Express (2017)', 55632000), 
         ('Happy Death Day', 55469000), 
         ('American Made', 51111000)))


def test_q2b():
    print(top_10_studios('box-office.csv', 2010) ==
     (('P/DW', 143422577), ('BV', 87448476), ('Par.', 86072709),
     ('Fox', 75084303), ('WB (NL)', 71678164), ('Sony', 65610505), 
     ('WB', 57031440), ('Sum.', 51862791), ('Uni.', 50432098), 
     ('MGM', 50287556)))

    print(top_10_studios('box-office.csv', 2015) ==
    (('BV', 159580610), ('Uni.', 106650216), ('W/Dim.', 76223578), 
     ('WB (NL)', 61690814), ('SGem', 60718966), ('Fox', 55193409), 
     ('Sony', 49808077), ('Par.', 47957831), ('LG/S', 39740147), 
     ('WB', 37740410)))

    print(top_10_studios('box-office.csv', 2016) ==
    (('BV', 191325159), ('Uni.', 72451381), ('Fox', 67792415), 
     ('WB (NL)', 57091987), ('WB', 55875409), ('Par.', 49544556), 
     ('SGem', 43301204), ('LG/S', 38679482), ('TriS', 34818558), 
     ('Sony', 34686427)))


# Uncomment to test
##test_q2a()
##test_q2b()



###
### Question 3 ###
###

class Merchant:
    def __init__(self, name, lari, place, *rumours):
        self.name = name
        self.lari = lari
        self.place = place
        place.merchants.append(self)
        self.rumours = list(rumours)        
        self.owes = {}

    def get_rumours(self):
        return tuple(self.rumours)

    def go_to(self, place):
        if self.place == place:
            return f"{self.name} is already at {place.name}"
        else:
            old = self.place
            old.merchants.remove(self)
            self.place = place
            place.merchants.append(self)
            return f"{self.name} moves from {old.name} to {place.name}"

    def gossip(self, other):
        if self == other:
            return f"{self.name} cannot gossip with himself"
        if self.place != other.place:
            return f"{self.name} and {other.name} are not at the same place"
        else:
            r = [r for r in other.rumours if r not in self.rumours]
            if r:
                self.rumours.append(r[0])
##            # Or using iteration
##            for r in other.rumours:
##                if r not in self.rumours:
##                    self.rumours.append(r)
##                    break
            r = [r for r in self.rumours if r not in other.rumours]
            if r:
                other.rumours.append(r[0])
##            # Or using iteration
##            for r in self.rumours:
##                if r not in other.rumours:
##                    other.rumours.append(r)
##                    break
            return f"{self.name} gossips with {other.name}"

    def shout(self, rumour):
        if rumour not in self.rumours:
            return f"{self.name} does not know that {rumour}"
        else:
            for m in self.place.merchants:
                if rumour not in m.rumours:
                    m.rumours.append(rumour)
            return f'{self.name} shouts "Did you know that {rumour}?!"'

    def lend(self, other, amount, interest):
        if self == other:
            return f"{self.name} cannot lend to himself"        
        elif self.place != other.place:
            return f"{self.name} and {other.name} are not at the same place"
        elif self.lari < amount:
            return f"{self.name} does not have enough Lari to lend"
        else:
            self.lari -= amount
            other.lari += amount
            if self not in other.owes:
                other.owes[self] = 0
            other.owes[self] += amount * (1 + interest/100)
            return "{} lends {} Lari to {} at {}% interest".format(self.name, amount, other.name, interest)

    def settle(self):        
        # claim money first
        ret = ""
        for merchant in self.place.merchants:
            if self in merchant.owes and merchant.lari > merchant.owes[self]:
                if ret:
                    ret += ", and"
                ret += " collects {} Lari from {}".format(merchant.owes[self], merchant.name)
                self.lari += merchant.owes[self]
                merchant.lari -= merchant.owes[self]
                merchant.owes[self] = 0
                
        # settle outstanding debt in order of largest
        merchants = sorted(self.owes.items(), key=lambda x:x[1], reverse=True)
        for merchant, amount in merchants:
            if merchant.place == self.place and self.lari >= amount:
                if ret:
                    ret += ", and"               
                ret += " repays {} Lari to {}".format(amount, merchant.name)
                merchant.lari += amount
                self.lari -= amount        
        if ret:
            return self.name + ret
        else:
            return "{} has nothing to settle".format(self.name)
          
class Place:
    def __init__(self, name):
        self.name = name
        self.merchants = []  
    def get_merchants(self):
        return tuple(m.name for m in self.merchants)
    

def test_q3():
    plaza    = Place('Plaza')
    market   = Place('Market')
    bazaar   = Place('Bazaar')
    fountain = Place('Fountain')

    arslan   = Merchant('Arslan', 100, bazaar,
                        'Istanbul is not Constantinople',
                        'Ottoman conquered the Byzantine')
    burhan   = Merchant('Burhan', 20,  market,
                        'banana is having a discount today',
                        'an apple a day keeps the medicine man away')
    doruk    = Merchant('Doruk',  85,  market)
    mustafa  = Merchant('Mustafa', 5,  fountain,
                        'today is Friday',
                        'the repractical exam is today',
                        'the repractical will lasts for 2 hours')

    _=market.get_merchants(); print(tuple(sorted(_)) == ('Burhan', 'Doruk'), '\tmarket.get_merchants():\t', _)
    _=burhan.go_to(market); print(_ == "Burhan is already at Market", '\tburhan.go_to(market):\t', _)
    _=burhan.go_to(plaza); print(_ == "Burhan moves from Market to Plaza", '\tburhan.go_to(plaza):\t', _)
    _=market.get_merchants(); print(tuple(sorted(_)) == ('Doruk',), '\tmarket.get_merchants():\t', _)
    _=burhan.shout('today is Friday'); print(_ == "Burhan does not know that today is Friday", '\tburhan.shout(\'today is Friday\'):\t', _)
    _=burhan.shout('banana is having a discount today'); print(_ == "Burhan shouts \"Did you know that banana is having a discount today?!\"", '\tburhan.shout(\'banana is having a discount today\'):\t', _)
    _=doruk.get_rumours(); print(tuple(sorted(_)) == (), '\tdoruk.get_rumours():\t', _)
    _=mustafa.go_to(plaza); print(_ == "Mustafa moves from Fountain to Plaza", '\tmustafa.go_to(plaza):\t', _)
    _=mustafa.get_rumours(); print(tuple(sorted(_)) == ('the repractical exam is today', 'the repractical will lasts for 2 hours', 'today is Friday'), '\tmustafa.get_rumours():\t', _)
    _=mustafa.shout('the repractical exam is today'); print(_ == "Mustafa shouts \"Did you know that the repractical exam is today?!\"", '\tmustafa.shout(\'the repractical exam is today\'):\t', _)
    _=burhan.get_rumours(); print(tuple(sorted(_)) == ('an apple a day keeps the medicine man away', 'banana is having a discount today', 'the repractical exam is today'), '\tburhan.get_rumours():\t', _)
    _=arslan.go_to(plaza); print(_ == "Arslan moves from Bazaar to Plaza", '\tarslan.go_to(plaza):\t', _)
    _=burhan.gossip(doruk); print(_ == "Burhan and Doruk are not at the same place", '\tburhan.gossip(doruk):\t', _)
    _=doruk.go_to(plaza); print(_ == "Doruk moves from Market to Plaza", '\tdoruk.go_to(plaza):\t', _)
    _=burhan.gossip(doruk); print(_ == "Burhan gossips with Doruk", '\tburhan.gossip(doruk):\t', _)
    _=burhan.gossip(burhan); print(_ == "Burhan cannot gossip with himself", '\tburhan.gossip(burhan):\t', _)
    _=plaza.get_merchants(); print(tuple(sorted(_)) == ('Arslan', 'Burhan', 'Doruk', 'Mustafa'), '\tplaza.get_merchants():\t', _)
    _=burhan.shout('the repractical exam is today'); print(_ == "Burhan shouts \"Did you know that the repractical exam is today?!\"", '\tburhan.shout(\'the repractical exam is today\'):\t', _)
    _=doruk.get_rumours(); print(tuple(sorted(_)) in [('the repractical exam is today',), ('banana is having a discount today', 'the repractical exam is today'), ('an apple a day keeps the medicine man away', 'banana is having a discount today', 'the repractical exam is today')], '\tdoruk.get_rumours():\t', _)
    _=burhan.get_rumours(); print(tuple(sorted(_)) == ('an apple a day keeps the medicine man away', 'banana is having a discount today', 'the repractical exam is today'), '\tburhan.get_rumours():\t', _)
    _=arslan.get_rumours(); print(tuple(sorted(_)) == ('Istanbul is not Constantinople', 'Ottoman conquered the Byzantine', 'the repractical exam is today'), '\tarslan.get_rumours():\t', _)
    _=burhan.gossip(arslan); print(_ == "Burhan gossips with Arslan", '\tburhan.gossip(arslan):\t', _)
    _=burhan.get_rumours(); print(tuple(sorted(_)) in [('Istanbul is not Constantinople', 'an apple a day keeps the medicine man away', 'banana is having a discount today', 'the repractical exam is today'), ('Ottoman conquered the Byzantine', 'an apple a day keeps the medicine man away', 'banana is having a discount today', 'the repractical exam is today')], '\tburhan.get_rumours():\t', _)
    _=arslan.get_rumours(); print(tuple(sorted(_)) in [('Istanbul is not Constantinople', 'Ottoman conquered the Byzantine', 'banana is having a discount today', 'the repractical exam is today'), ('Istanbul is not Constantinople', 'Ottoman conquered the Byzantine', 'an apple a day keeps the medicine man away', 'the repractical exam is today')], '\tarslan.get_rumours():\t', _)
    _=arslan.gossip(burhan); print(_ == "Arslan gossips with Burhan", '\tarslan.gossip(burhan):\t', _)
    _=burhan.get_rumours(); print(tuple(sorted(_)) == ('Istanbul is not Constantinople', 'Ottoman conquered the Byzantine', 'an apple a day keeps the medicine man away', 'banana is having a discount today', 'the repractical exam is today'), '\tburhan.get_rumours():\t', _)
    _=arslan.get_rumours(); print(tuple(sorted(_)) == ('Istanbul is not Constantinople', 'Ottoman conquered the Byzantine', 'an apple a day keeps the medicine man away', 'banana is having a discount today', 'the repractical exam is today'), '\tarslan.get_rumours():\t', _)
    _=doruk.go_to(bazaar); print(_ == "Doruk moves from Plaza to Bazaar", '\tdoruk.go_to(bazaar):\t', _)
    _=doruk.lend(burhan, 100, 1); print(_ == "Doruk and Burhan are not at the same place", '\tdoruk.lend(burhan, 100, 1):\t', _)
    _=doruk.lend(doruk, 1, 0); print(_ == "Doruk cannot lend to himself", '\tdoruk.lend(doruk, 1, 0):\t', _)
    _=doruk.go_to(plaza); print(_ == "Doruk moves from Bazaar to Plaza", '\tdoruk.go_to(plaza):\t', _)
    _=doruk.lend(burhan, 80, 1); print(_ == "Doruk lends 80 Lari to Burhan at 1% interest", '\tdoruk.lend(burhan, 80, 1):\t', _)
    _=doruk.lend(arslan, 6, 2); print(_ == "Doruk does not have enough Lari to lend", '\tdoruk.lend(arslan, 6, 2):\t', _)
    _=burhan.lend(arslan, 40, 2); print(_ == "Burhan lends 40 Lari to Arslan at 2% interest", '\tburhan.lend(arslan, 40, 2):\t', _)
    _=burhan.lend(mustafa, 50, 2); print(_ == "Burhan lends 50 Lari to Mustafa at 2% interest", '\tburhan.lend(mustafa, 50, 2):\t', _)
    _=burhan.go_to(fountain); print(_ == "Burhan moves from Plaza to Fountain", '\tburhan.go_to(fountain):\t', _)
    _=doruk.settle(); print(_ == "Doruk has nothing to settle", '\tdoruk.settle():\t', _)
    _=burhan.settle(); print(_ == "Burhan has nothing to settle", '\tburhan.settle():\t', _)
    _=burhan.go_to(plaza); print(_ == "Burhan moves from Fountain to Plaza", '\tburhan.go_to(plaza):\t', _)
    _=burhan.settle(); print(_ == "Burhan collects 51.0 Lari from Mustafa, and collects 40.8 Lari from Arslan, and repays 80.8 Lari to Doruk", '\tburhan.settle():\t', _)
##test_q3()

###
### Question 1
###

def brake_at(dest, speed):
    while speed:
        speed //= 2
        dest -= speed
    return dest


def braking_points(curr, dest, speed):
    t = 0
    r = []
    while (speed):
        print(t, curr, speed) # for visualization
        # can we maintain the current speed?
        if curr + speed > brake_at(dest, speed):
            # no, we have to reduce
            speed //= 2
            r.append(curr)
        curr += speed
        t += 1
    print(t, curr, speed) # for visualization
    if curr > dest:
        return [] # oops we have exceeded our destination
    else:
        return r



# Tests
def test_q1a():
    print(brake_at(89, 4))
    print(brake_at(89, 10))
    print(brake_at(89, 20))

def test_q1b():
    print(braking_points(44, 89, 10))
    print(braking_points(71, 89, 20))
    print(braking_points(71, 89, 22))


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

    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows

### Your answer here.
# Q2A
def monthly_avg(fname, currency, year, category):
    data = read_csv(fname)
    col = data[0].index(category)
    del data[0]

    # filter out the currency and year
    data = filter(lambda row: int(row[0]) == year, data)
    data = filter(lambda row: row[3] == currency, data)

    d = {}
    for row in data:
        if row[1] not in d:
            d[row[1]] = []
        d[row[1]].append(float(row[col]))

    for month, prices in d.items():
        d[month] = round(sum(prices)/len(prices), 4)

    return d


# Q2B
def highest_gain(fname, year, category):
    data = read_csv(fname)
    col = data[0].index(category)
    del data[0]

    #filter out the required year
    data = filter(lambda row: int(row[0]) == year, data)

    # For each month, we need the max and min for each currency
    d = {}
    for row in data:
        if row[col] == '-':
            continue
        
        month, curr = row[1], row[3]
        if month not in d:
            d[month] = {}  # new dict for currency
        m = d[month]
        if  curr not in m:
            m[curr] = []
        try:
            m[curr].append(int(row[col]))
        except:
            m[curr].append(float(row[col]))

    # process the dict
    for mth, m in d.items():
        for curr, volume in m.items():
            m[curr] = round((max(volume)/min(volume) - 1) * 100, 2)
        d[mth] = max(m.items(), key=lambda x:x[1])

    return d


# Q2C BONUS
month = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
         'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12 }

def max_single_sell(fname, currency, category):
    data = read_csv(fname)
    col = data[0].index(category)
    del data[0]

    data = sorted(filter(lambda row: row[3] == currency, data),
                  key=lambda x: (int(x[0]), month[x[1]], int(x[2])))
    for row in data:
        try:
            row[col] = int(row[col])
        except:
            row[col] = float(row[col])
    
    def helper(start, end):
        if start >= end:
            return (0, 0, 0)
        else:
            mid = (start + end) // 2
            low = min(data[start:mid+1], key=lambda x:x[col])
            high = max(data[mid+1:end+1], key=lambda x:x[col])
            split = ('-'.join(low[:3]), '-'.join(high[:3]), high[col] - low[col])
            return max(helper(start, mid),
                       helper(mid+1, end),
                       split,
                       key=lambda x:x[2])
    return helper(0, len(data)-1)


# Tests
def test_q2a():
    print(monthly_avg('crypto.csv', 'ETH', 2017, 'Close') == \
        {'Nov': 296.4443, 'Oct': 306.2474, 'Sep': 293.0473, 
         'Aug': 301.6094, 'Jul': 224.1239, 'Jun': 313.7343, 
         'May': 125.7494, 'Apr': 50.3367, 'Mar': 34.7916, 
         'Feb': 12.3711, 'Jan': 10.2013})

    print(monthly_avg('crypto.csv', 'BTC', 2013, 'High') == \
        {'Dec': 856.4419, 'Nov': 569.307, 'Oct': 161.9442, 
         'Sep': 134.164, 'Aug': 116.0023, 'Jul': 93.869, 
         'Jun': 111.3007, 'May': 123.949, 'Apr': 143.4667})

def test_q2b():
    print(highest_gain('crypto.csv', 2017, "Volume") == \
        {'Nov': ('XPR', 695.17), 'Oct': ('XPR', 3485.19), 
         'Sep': ('LTC', 1792.14), 'Aug': ('XPR', 5524.07), 
         'Jul': ('LTC', 1354.52), 'Jun': ('XPR', 1071.13), 
         'May': ('ETH', 2302.35), 'Apr': ('XPR', 4537.85), 
         'Mar': ('XPR', 7003.02), 'Feb': ('ETH', 1049.67), 
         'Jan': ('XPR', 1975.93)})
 
    print(highest_gain('crypto.csv', 2013, "Market Cap") == \
        {'Dec': ('XPR', 272.37), 'Nov': ('LTC', 1862.94), 
         'Oct': ('BTC', 88.94), 'Sep': ('XPR', 171.23), 
         'Aug': ('XPR', 109.9), 'Jul': ('BTC', 59.08), 
         'Jun': ('LTC', 52.22), 'May': ('LTC', 48.27), 
         'Apr': ('BTC', 7.15)})

##test_q2a()
test_q2b()




###
### Question 3
###

### Your answer here.
class Entity:
    def __init__(self, name, damage):
        self.name   = name
        self.damage = damage
        self.master = None  # This stores the immediate master
        
    def attack(self, other):
        if other == self:
            return self.name + ' cannot attack itself'
        if other == self._get_master():
            return self.name + ' cannot attack its master';
        elif self.master and other in self._get_master()._get_slaves():
            return self.name + ' cannot attack its master\'s slave'
        else:
            return '{} deals {} damage to {}'.format(self.name, self.get_damage(), other.name)

    def get_name(self):
        return self.name

    def get_damage(self):
        return self.damage

    def get_master(self):
        master = self._get_master()
        if master:
            return master.name
        else:
            return None

    ## Internal helper method to get the ultimate master object
    def _get_master(self):
        # This uses iteration
        master = self.master
        while master and master.master:
            master = master.master
        return master

        # Using recursion
        if self.master and self.master.master:  # if I have a grandmaster
            return self.master._get_master()    # return master's ultimate master
        else:
            return self.master                  # master is the ultimate


class Overmind(Entity):
    def __init__(self, name, dmg):
        super().__init__(name,dmg)
        self.slaves = []  # This stores a list of direct slaves

    ## Internal helper method to get all direct and indirect slaves
    def _get_slaves(self):
        res = []
        for slave in self.slaves:
            if type(slave) == Overmind:
                res.extend(slave._get_slaves())  # Use recusrion to accumulate all slaves
            res.append(slave)
        return res

    def get_slaves(self):
        return tuple(s.name for s in self._get_slaves())

    # Override Entity.get_damage to give the correct damage
    def get_damage(self):
        # damage is sum of all slave's damage
        return sum(s.get_damage() for s in self.slaves) + self.damage
    
    def attack(self, other):
        if other in self._get_slaves():
            return self.name + ' cannot attack its slave'
        else:
            return super().attack(other)
        
    def mind_control(self, other):
        if other == self:
            return self.name + ' cannot mind-control itself'
        elif other in self._get_slaves():
            return other.name + ' is already a slave of ' + self.name
        elif type(other) == Overmind and self in other._get_slaves():
            return self.name + ' cannot mind-control its master'
        elif other._get_master() and other._get_master() == self._get_master():
            return self.name + ' and ' + other.name + ' have the same master'
        else:
            previous = other.master  # stores previous master
            other.master = self  # before assigning to new master
            self.slaves.append(other)            
            if previous:
                previous.slaves.remove(other)  # remove other from previous master
                return self.name + ' over-mind-controls ' + other.name + ' from ' + previous.name
            else:
                return self.name + ' mind-controls ' + other.name


####################################################################
# Alternate method for Q3 using union-search                       # 
# where you store the ultimate master and all slaves,              #
# rather than just the immediate master and slaves                 #
#                                                                  # 
# Here retreival is simple but managing changes in complicated     #
# This is NOT recommended. Just to show how complicated things get #
####################################################################

class Entity:
    def __init__(self, name, damage):
        self.name   = name
        self.damage = damage
        self.master = None  # This stores the ultimate master
        
    def attack(self, other):
        if other == self:
            return f'{self.name} cannot attack itself'  # This f-string style is only available from Python 3.6.2
        if other == self.master:
            return f'{self.name} cannot attack its master';
        elif self.master and other in self.master.slaves:
            return f'{self.name} cannot attack its master\'s slave'
        else:
            return f'{self.name} deals {self.get_damage()} damage to {other.name}'

    def get_name(self):
        return self.name
        
    def get_damage(self):
        return self.damage

    def get_master(self):        
        if self.master:
            return self.master.name
        else:
            return None


class Overmind(Entity):
    def __init__(self, name, dmg):
        super().__init__(name, dmg)
        self.slaves = []  # This stores all slaves, including slave of slaves.

    def get_slaves(self):
        return tuple(s.name for s in self.slaves)

    #def get_damage(self):
    # We do not need this if damage is updated every time there is a mind-control
    
    def attack(self, other):
        if other in self.slaves:
            return self.name + ' cannot attack its slave'
        else:
            return super().attack(other)
        
    def mind_control(self, other):
        if other == self:
            return self.name + ' cannot mind-control itself'
        elif other in self.slaves:
            return other.name + ' is already a slave of ' + self.name
        elif type(other) == Overmind and self in other.slaves:
            return self.name + ' cannot mind-control its master'
        elif other.master and other.master == self.master:
            return self.name + ' and ' + other.name + ' have the same master'
       
        # This is where it gets complicated.
        # So let's do this step by step.

        # store the old master
        previous = other.master  
        
        # Step 1.
        # Update other and its slaves to their new ultimate master
        master = self.master
        if not master:
            master = self
        other.master = master
        if isinstance(other, Overmind):
            for slave in other.slaves:
                slave.master = master

        # Step 2.
        # Update new ultimate master and all sub-masters with their new slaves and damage
        master = self.master
        while master:
            # add new slaves to master
            self.damage += other.damage
            master.slaves.append(other)
            if isinstance(other, Overmind):
                master.slaves.extend(other.slaves)

            # find next sub-master
            for slave in master.slaves:
                if isinstance(slave, Overmind) and self in slave.slaves:
                    master = slave
                    break
            else:
                master = None  # exit the while loop

        # Step 3.
        # Update self slaves and damage
        self.damage += other.damage
        self.slaves.append(other)
        if isinstance(other, Overmind):
            self.slaves.extend(other.slaves)
    
        # Step 4.
        # Remove other and slaves from all old masters (if any)
        #   Start from ultimate master, remove all other.slaves,
        #   
        while previous:            
            previous.slaves.remove(other)
            previous.damage -= other.damage
            #  - remove all other's slaves from master
            if isinstance(other, Overmind):
                for slave in other.slaves:
                    previous.slaves.remove(slave)

            #  - find the next sub-master
            for slave in previous.slaves:
                if isinstance(slave, Overmind) and other in slave.slaves:
                    previous = slave
                    break
            else: # this is a special use of else that is beyond our syllabus
                return self.name + ' over-mind-controls ' + other.name + ' from ' + previous.name
                    
        return self.name + ' mind-controls ' + other.name


# Tests
def test_q3():
    demodog    = Entity('Demodog', 10)
    demogorgon = Entity('Demogorgon', 50)
    dartagnan  = Entity("D'artagnan", 20)
    mindflayer = Overmind('Mindflayer', 25)
    mindreader = Overmind('Mindreader', 5)
    eleven = Overmind('Eleven', 5)

    _=demodog.attack(demodog); print(_ == "Demodog cannot attack itself", '\tdemodog.attack(demodog):\t', _)
    _=demodog.attack(demogorgon); print(_ == "Demodog deals 10 damage to Demogorgon", '\tdemodog.attack(demogorgon):\t', _)
    _=demodog.get_master(); print(_ == None, '\tdemodog.get_master():\t', _)
    _=mindreader.mind_control(mindreader); print(_ == "Mindreader cannot mind-control itself", '\tmindreader.mind_control(mindreader):\t', _)
    _=mindreader.mind_control(demodog); print(_ == "Mindreader mind-controls Demodog", '\tmindreader.mind_control(demodog):\t', _)
    _=mindreader.mind_control(demogorgon); print(_ == "Mindreader mind-controls Demogorgon", '\tmindreader.mind_control(demogorgon):\t', _)
    _=mindreader.get_slaves(); print(tuple(sorted(_)) == ('Demodog', 'Demogorgon'), '\tmindreader.get_slaves():\t', _)
    _=demodog.get_master(); print(_ == "Mindreader", '\tdemodog.get_master():\t', _)
    _=mindreader.attack(demodog); print(_ == "Mindreader cannot attack its slave", '\tmindreader.attack(demodog):\t', _)
    _=demodog.attack(mindreader); print(_ == "Demodog cannot attack its master", '\tdemodog.attack(mindreader):\t', _)
    _=demodog.attack(demogorgon); print(_ == "Demodog cannot attack its master's slave", '\tdemodog.attack(demogorgon):\t', _)
    _=mindflayer.attack(eleven); print(_ == "Mindflayer deals 25 damage to Eleven", '\tmindflayer.attack(eleven):\t', _)
    _=mindflayer.mind_control(mindreader); print(_ == "Mindflayer mind-controls Mindreader", '\tmindflayer.mind_control(mindreader):\t', _)
    _=mindflayer.attack(eleven); print(_ == "Mindflayer deals 90 damage to Eleven", '\tmindflayer.attack(eleven):\t', _)
    _=mindflayer.mind_control(demodog); print(_ == "Demodog is already a slave of Mindflayer", '\tmindflayer.mind_control(demodog):\t', _)
    _=mindreader.mind_control(mindflayer); print(_ == "Mindreader cannot mind-control its master", '\tmindreader.mind_control(mindflayer):\t', _)
    _=mindflayer.mind_control(dartagnan); print(_ == "Mindflayer mind-controls D'artagnan", '\tmindflayer.mind_control(dartagnan):\t', _)
    _=mindreader.mind_control(dartagnan); print(_ == "Mindreader and D'artagnan have the same master", '\tmindreader.mind_control(dartagnan):\t', _)
    _=mindflayer.get_slaves(); print(tuple(sorted(_)) == ("D'artagnan", 'Demodog', 'Demogorgon', 'Mindreader'), '\tmindflayer.get_slaves():\t', _)
    _=eleven.mind_control(mindreader); print(_ == "Eleven over-mind-controls Mindreader from Mindflayer", '\televen.mind_control(mindreader):\t', _)
    _=eleven.get_slaves(); print(tuple(sorted(_)) == ('Demodog', 'Demogorgon', 'Mindreader'), '\televen.get_slaves():\t', _)
    _=eleven.attack(mindflayer); print(_ == "Eleven deals 70 damage to Mindflayer", '\televen.attack(mindflayer):\t', _)
    _=mindflayer.attack(eleven); print(_ == "Mindflayer deals 45 damage to Eleven", '\tmindflayer.attack(eleven):\t', _)
    _=mindreader.attack(mindflayer); print(_ == "Mindreader deals 65 damage to Mindflayer", '\tmindreader.attack(mindflayer):\t', _)
    _=eleven.mind_control(dartagnan); print(_ == "Eleven over-mind-controls D'artagnan from Mindflayer", '\televen.mind_control(dartagnan):\t', _)
    _=mindflayer.get_slaves(); print(tuple(sorted(_)) == (), '\tmindflayer.get_slaves():\t', _)
    _=mindreader.mind_control(mindflayer); print(_ == "Mindreader mind-controls Mindflayer", '\tmindreader.mind_control(mindflayer):\t', _)
    _=mindreader.get_slaves(); print(tuple(sorted(_)) == ('Demodog', 'Demogorgon', 'Mindflayer'), '\tmindreader.get_slaves():\t', _)
    _=eleven.get_slaves(); print(tuple(sorted(_)) == ("D'artagnan", 'Demodog', 'Demogorgon', 'Mindflayer', 'Mindreader'), '\televen.get_slaves():\t', _)
    _=mindflayer.mind_control(mindreader); print(_ == "Mindflayer cannot mind-control its master", '\tmindflayer.mind_control(mindreader):\t', _)
    _=mindflayer.mind_control(dartagnan); print(_ == "Mindflayer and D'artagnan have the same master", '\tmindflayer.mind_control(dartagnan):\t', _) 

# Uncomment to test question 3
#test_q3()



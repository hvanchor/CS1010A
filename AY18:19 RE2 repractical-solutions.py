###
### Question 1
###

# Q1A
def num_triangles(n):
    if n == 0:
        return 1
    else:
        return 3 * num_triangles(n-1) + 2

# Q1B
def area(n):
    if n == 0:
        return 1
    else:
        return area(n-1)*3/4

# Q1C
def row(n):
    if n == 0:
        return [1]
    else:
        prev = row(n-1)
        r = [1]
        for i in range(len(prev) - 1):
            r.append((prev[i] + prev[i+1]) % 2)
        r.append(1)
        return r


# Tests
def test_q1a():
    print(num_triangles(0))
    print(num_triangles(1))
    print(num_triangles(2))
    print(num_triangles(3))
    

def test_q1b():
    print(area(0))
    print(area(1))
    print(area(2))
    print(area(3))


def test_q1c():
    print(row(0))
    print(row(1))
    print(row(2))
    print(row(3))
    for i in range(16):        
        print(" "*(15-i), *row(i))

# Uncomment to test question 1
##test_q1a()
##test_q1b()
##test_q1c()   


    

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
def monthly_max(fname, location, year):
    data = read_csv(fname)

    del data[0]
    data = filter(lambda row: row[0] == location and int(row[1]) == year, data)

    d = {}
    for row in data:
        month = row[2]
        if month not in d:
            d[month] = []
        d[month].append(float(row[5]))

    for k, v in d.items():
        d[k] = round(sum(v)/len(v), 2)

    return d


# Q2B
def windest_location(fname, year):
    data = read_csv(fname)

    del data[0]
    data = filter(lambda row: int(row[1]) == year, data)

    d = {}
    for row in data:
        month = row[2]
        if month not in d:
            d[month] = {}

        location = row[0]
        month = d[month]
        if location not in month:
            month[location] = []
        month[location].append(float(row[4]))

    for month, locs in d.items():
        for loc, value in locs.items():
            locs[loc] = round(sum(value)/len(value), 2)

        d[month] = max(locs.items(), key=lambda x:x[1])

    return d



# Tests
def test_q2a():
    print(monthly_max("wind.csv", "Changi", 2013) == \
        {'Jan': 32.51, 'Feb': 29.63, 'Mar': 31.86, 'Apr': 33.29,
         'May': 30.48, 'Jun': 30.54, 'Jul': 30.91, 'Aug': 33.98, 
         'Sep': 33.22, 'Oct': 32.56, 'Nov': 28.88, 'Dec': 30.79})
    print(monthly_max("wind.csv", "Paya Lebar", 2015) == \
        {'Jan': 38.35, 'Feb': 39.59, 'Mar': 36.0, 'Apr': 33.06,
         'May': 32.39, 'Jun': 31.9, 'Jul': 37.14, 'Aug': 33.64, 
         'Sep': 30.51, 'Oct': 27.75, 'Nov': 29.11, 'Dec': 36.84})
    print(monthly_max("wind.csv", "Marina Barrage", 2018) == \
        {'Jan': 31.09, 'Feb': 33.93, 'Mar': 31.85})


def test_q2b():
    print(windest_location("wind.csv", 2015) == \
        {'Jan': ('Paya Lebar', 18.0), 'Feb': ('Paya Lebar', 18.84), 
         'Mar': ('Paya Lebar', 13.91), 'Apr': ('Paya Lebar', 10.44), 
         'May': ('East Coast Parkway', 10.87), 
         'Jun': ('East Coast Parkway', 13.03), 
         'Jul': ('East Coast Parkway', 15.75), 
         'Aug': ('East Coast Parkway', 14.66), 
         'Sep': ('East Coast Parkway', 13.01), 
         'Oct': ('East Coast Parkway', 10.06), 
         'Nov': ('Paya Lebar', 8.36), 'Dec': ('Paya Lebar', 11.73)})
    print(windest_location("wind.csv", 2017) == \
        {'Jan': ('Marina Barrage', 16.34), 'Feb': ('Marina Barrage', 18.16), 
         'Mar': ('Marina Barrage', 13.65), 'Apr': ('Marina Barrage', 12.46), 
         'May': ('East Coast Parkway', 11.67), 
         'Jun': ('East Coast Parkway', 11.67), 
         'Jul': ('East Coast Parkway', 14.9), 
         'Aug': ('East Coast Parkway', 13.97), 
         'Sep': ('East Coast Parkway', 11.93), 
         'Oct': ('East Coast Parkway', 10.75), 
         'Nov': ('East Coast Parkway', 10.78), 
         'Dec': ('East Coast Parkway', 11.02)})
    print(windest_location("wind.csv", 2018) == \
        {'Jan': ('Paya Lebar', 12.88), 'Feb': ('Paya Lebar', 20.0), 'Mar': ('Paya Lebar', 13.64)})

# Uncomment to test question 2
##test_q2a()
##test_q2b()   




###
### Question 3
###

class Pilot:
    def __init__(self, name, level):
        self.name = name
        self.level= level
        self.partners = {}
        self.jaeger = None

    def train(self, partner):
        if partner == self:
            return f"{self.name} cannot train with self"
        
        # update self
        if partner not in self.partners:
            self.partners[partner] = 0
        self.partners[partner] += 1

        # update partner
        if self not in partner.partners:
            partner.partners[self] = 0
        partner.partners[self] += 1

        return f"{self.name} trains with {partner.name}"

    def show_partners(self):
        return tuple(map(lambda p: (p[0].name, p[1]), self.partners.items()))

    def board(self, jaeger):
        if self.jaeger:
            return f"{self.name} is already on {self.jaeger.name}"        
        jaeger.pilots.append(self)
        self.jaeger = jaeger
        return f"{self.name} boards {jaeger.name}"

    def alight(self):
        if self.jaeger == None:
            return f"{self.name} is not on a Jaeger"
        jaeger = self.jaeger
        jaeger.pilots.remove(self)
        self.jaeger = None
        return f"{self.name} alights from {jaeger.name}"


class Jaeger:
    def __init__(self, name):
        self.name = name
        self.pilots = []
        
    def drift(self):
        if len(self.pilots) < 2:
            return f"{self.name} has insufficient pilots"
        
        # get required training level
        #level = max(map(lambda pilot: pilot.level, self.pilots))

        # check each pilot has trained sufficiently
        for pilot in self.pilots:
            for partner in self.pilots:
                if pilot == partner:
                    continue  # skip comparing with self
                
                if partner not in pilot.partners or pilot.partners[partner] < max(pilot.level, partner.level):
                    return f"{pilot.name} and {partner.name} are not compatible"

        return f"Drift successful. {self.name} is operational"





def test_q3():
    raleigh = Pilot("Raleigh", 3)
    yancy = Pilot("Yancy", 2)
    mako = Pilot("Mako", 5)

    gipsy = Jaeger("Gipsy Danger")
    crimson = Jaeger("Crimson Typhoon")      
           
    _=raleigh.show_partners(); print(tuple(sorted(_)) == (), "\traleigh.show_partners():\t", _)
    _=raleigh.train(yancy); print(_ == "Raleigh trains with Yancy", "\traleigh.train(yancy):\t", _)
    _=raleigh.show_partners(); print(tuple(sorted(_)) == (('Yancy', 1),), "\traleigh.show_partners():\t", _)
    _=yancy.show_partners(); print(tuple(sorted(_)) == (('Raleigh', 1),), "\tyancy.show_partners():\t", _)
    _=yancy.train(raleigh); print(_ == "Yancy trains with Raleigh", "\tyancy.train(raleigh):\t", _)
    _=raleigh.board(gipsy); print(_ == "Raleigh boards Gipsy Danger", "\traleigh.board(gipsy):\t", _)
    _=yancy.board(gipsy); print(_ == "Yancy boards Gipsy Danger", "\tyancy.board(gipsy):\t", _)
    _=gipsy.drift(); print(_ == "Raleigh and Yancy are not compatible", "\tgipsy.drift():\t", _)
    _=raleigh.train(yancy); print(_ == "Raleigh trains with Yancy", "\traleigh.train(yancy):\t", _)
    _=gipsy.drift(); print(_ == "Drift successful. Gipsy Danger is operational", "\tgipsy.drift():\t", _)
    _=yancy.board(crimson); print(_ == "Yancy is already on Gipsy Danger", "\tyancy.board(crimson):\t", _)
    _=yancy.alight(); print(_ == "Yancy alights from Gipsy Danger", "\tyancy.alight():\t", _)
    _=gipsy.drift(); print(_ == "Gipsy Danger has insufficient pilots", "\tgipsy.drift():\t", _)
    _=mako.alight(); print(_ == "Mako is not on a Jaeger", "\tmako.alight():\t", _)
    _=mako.board(gipsy); print(_ == "Mako boards Gipsy Danger", "\tmako.board(gipsy):\t", _)
    _=gipsy.drift(); print(_ == "Raleigh and Mako are not compatible", "\tgipsy.drift():\t", _)
    _=mako.train(raleigh); print(_ == "Mako trains with Raleigh", "\tmako.train(raleigh):\t", _)
    _=mako.show_partners(); print(tuple(sorted(_)) == (('Raleigh', 1),), "\tmako.show_partners():\t", _)
    _=raleigh.show_partners(); print(tuple(sorted(_)) == (('Mako', 1), ('Yancy', 3)), "\traleigh.show_partners():\t", _)
    _=mako.train(raleigh); print(_ == "Mako trains with Raleigh", "\tmako.train(raleigh):\t", _)
    _=mako.train(raleigh); print(_ == "Mako trains with Raleigh", "\tmako.train(raleigh):\t", _)
    _=mako.train(raleigh); print(_ == "Mako trains with Raleigh", "\tmako.train(raleigh):\t", _)
    _=mako.train(raleigh); print(_ == "Mako trains with Raleigh", "\tmako.train(raleigh):\t", _)
    _=gipsy.drift(); print(_ == "Drift successful. Gipsy Danger is operational", "\tgipsy.drift():\t", _)
    _=yancy.board(gipsy); print(_ == "Yancy boards Gipsy Danger", "\tyancy.board(gipsy):\t", _)
    _=gipsy.drift(); print(_ == "Mako and Yancy are not compatible", "\tgipsy.drift():\t", _)
    _=yancy.train(mako); print(_ == "Yancy trains with Mako", "\tyancy.train(mako):\t", _)
    _=yancy.train(mako); print(_ == "Yancy trains with Mako", "\tyancy.train(mako):\t", _)
    _=yancy.train(mako); print(_ == "Yancy trains with Mako", "\tyancy.train(mako):\t", _)
    _=yancy.train(mako); print(_ == "Yancy trains with Mako", "\tyancy.train(mako):\t", _)
    _=yancy.train(mako); print(_ == "Yancy trains with Mako", "\tyancy.train(mako):\t", _)
    _=gipsy.drift(); print(_ == "Drift successful. Gipsy Danger is operational", "\tgipsy.drift():\t", _)

# Uncomment to test question 3
test_q3()

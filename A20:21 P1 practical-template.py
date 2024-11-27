##############
# Question 1 #
##############

# Your answer here.
# Q1
def pyramids(n):
    def bottom(n):
        if n<=2:
            return n
        else:
            return bottom(n-1) + bottom(n-2)
    if n == 1:
        return 1
    else:
        return bottom(n)*pyramids(n-1)


# Tests
def test_q1():
    print(pyramids(1)==1)
    print(pyramids(2)==2)
    print(pyramids(3)==6)
    print(pyramids(4)==30)

# Uncomment to test question 1
#test_q1()


##############
# Question 2 #
##############
import csv

def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of lists
    containing rows in the csv file and its entries.
    """
    with open(csvfilename, encoding='utf-8') as csvfile:
        rows = [row for row in csv.reader(csvfile)]
    return rows

# Your answer here.
# Q2

def top_k_timestamps(filename, date, k):
    data = list(filter(lambda x: x[0] == date, read_csv(filename)[1:]))
    data = list(map(lambda x: (x[1], sum(map(int, x[2:]))), data))
    sorted_lst = sorted(data, key=lambda x: x[1], reverse=True)
    if k == 0 or k > len(data):
        return sorted_lst[:k]
    cutoff = sorted_lst[k-1][1]
    return list(filter(lambda x: x[1] >= cutoff, sorted_lst))




def player_daily_stats(filename, start_date, end_date):
    data = filter(lambda x: start_date <= x[0] <= end_date, read_csv(filename))
    d = {}
    for date, time, player, _ in data:
        if date not in d:
            d[date] = {}
        hour = time[:2]
        if hour not in d[date]:
            d[date][hour] = []
        d[date][hour].append(int(player))
    for k, v in d.items():
        for hour, player_count in v.items():
            v[hour] = round(sum(player_count)/len(player_count), 2)
        hour_average = list(v.items())
        d[k] = {
            'max': max(hour_average, key=lambda x: x[1]),
            'min': min(hour_average, key=lambda x: x[1]),
        }
    return d


# Tests
def test_q2a():
    test1 = top_k_timestamps("among_us.csv", "2020-10-24", 1)
    print(test1)
    print(test1 == [('23:50', 263111)])
    test2 = top_k_timestamps("among_us.csv", "2020-10-24", 3)
    print(test2)
    print(test2 == [('23:50', 263111), ('23:40', 259451), ('23:30', 257646)])
    test3 = top_k_timestamps("among_us.csv", "2020-11-01", 5)
    print(test3)
    print(test3 == [('04:00', 440435), ('03:50', 420450), ('05:00', 418154), ('03:40', 417638), ('05:10', 414781)])

def test_q2b():
    test1 = player_daily_stats("among_us.csv", "2020-10-24","2020-10-25")
    print(test1)
    print(test1 == {
        '2020-10-24':{'max':('23', 148503.83), 'min':('22', 136173.0)},
        '2020-10-25':{'max':('05',  279875.67), 'min':('17', 83682.83)}
    })
    test2 = player_daily_stats("among_us.csv", "2020-10-26","2020-11-01")
    print(test2)
    print(test2 == {
        '2020-10-26':{'max':('04', 321269.17), 'min':('16', 68468.83)},
        '2020-10-27':{'max':('04', 281635.0),  'min':('16', 66024.17)},
        '2020-10-28':{'max':('04', 268729.33), 'min':('16', 64382.33)},
        '2020-10-29':{'max':('04', 263688.67), 'min':('16', 61390.17)},
        '2020-10-30':{'max':('04', 262891.17), 'min':('16', 59494.0)},
        '2020-10-31':{'max':('05', 313064.67), 'min':('17', 65617.5)},
        '2020-11-01':{'max':('05', 278808.17), 'min':('17', 70535.83)}
    })

# Uncomment to test question 2
##test_q2a()
## test_q2b()


##############
# Question 3 #
##############

# Your answer here.
# Q3
class Place:
    def __init__(self, name, tasks):
        self.name = name
        self.tasks = tasks
        self.people = []


class Crewmate:
    def __init__(self, name, place):
        self.name = name
        self.place = place
        self.tasks = {}
        self.alive = True
        place.people.append(self)

    def move(self, place):
        self.place.people.remove(self)
        self.place = place
        self.place.people.append(self)
        return f"{self.name} moves to {place.name}"

    def do_task(self, tasks):
        if tasks not in self.place.tasks:
            return f"No such task {tasks} in {self.place.name}"
        place_name = self.place.name
        if place_name not in self.tasks:
            self.tasks[place_name] = []
        if tasks in self.tasks[place_name]:
            return f"Task {tasks} in {self.place.name} already done"
        else:
            self.tasks[place_name].append(tasks)
            return f"{self.name} does {tasks} in {self.place.name}"




class Impostor(Crewmate):
    def do_task(self, tasks):
        return "Impostors cannot do tasks"

    def kill(self):
        alive = list(filter(lambda x : type(x) != Impostor and x.alive == True, self.place.people))
        if len(alive) == 0:
            return "Nobody to kill"
        else:
            victim = alive[0]
            victim.alive = False
            return f"{self.name} kills {victim.name} at {self.place.name}"


# Tests
def test_q3():
    cafe = Place("Cafeteria",  ["fix wires", "download data"])
    weapons = Place("Weapons", ["shoot asteroids", "fix wires"])

    ben = Impostor("@evilprof", cafe)
    waikay =  Impostor("@waisosus", cafe)
    kenghwee = Crewmate("@hweelingdead", cafe)
    jonathan = Crewmate("@lordjon", cafe)

    _=kenghwee.do_task("shoot asteroids"); print(_ == "No such task shoot asteroids in Cafeteria", "\tkenghwee.do_task(\"shoot asteroids\"):\t", _)
    _=jonathan.do_task("fix wires"); print(_ == "@lordjon does fix wires in Cafeteria", "\tjonathan.do_task(\"fix wires\"):\t", _)
    _=jonathan.do_task("fix wires"); print(_ == "Task fix wires in Cafeteria already done", "\tjonathan.do_task(\"fix wires\"):\t", _)
    _=jonathan.move(weapons); print(_ == "@lordjon moves to Weapons", "\tjonathan.move(weapons):\t", _)
    _=jonathan.do_task("fix wires"); print(_ == "@lordjon does fix wires in Weapons", "\tjonathan.do_task(\"fix wires\"):\t", _)
    _=waikay.move(weapons); print(_ == "@waisosus moves to Weapons", "\twaikay.move(weapons):\t", _)
    _=waikay.do_task("adjust aiming"); print(_ == "Impostors cannot do tasks", "\twaikay.do_task(\"adjust aiming\"):\t", _)
    _=kenghwee.move(weapons); print(_ == "@hweelingdead moves to Weapons", "\tkenghwee.move(weapons):\t", _)
    _=ben.kill(); print(_ == "Nobody to kill", "\tben.kill():\t", _)
    _=waikay.kill(); print(_ in ["@waisosus kills @hweelingdead at Weapons", "@waisosus kills @lordjon at Weapons"], "\twaikay.kill():\t", _)
    _=ben.move(weapons); print(_ == "@evilprof moves to Weapons", "\tben.move(weapons):\t", _)
    _=ben.kill(); print(_ in ["@evilprof kills @lordjon at Weapons", "@evilprof kills @hweelingdead at Weapons"], "\tben.kill():\t", _)
    _=ben.kill(); print(_ == "Nobody to kill", "\tben.kill():\t", _)
    _=kenghwee.move(cafe); print(_ == "@hweelingdead moves to Cafeteria", "\tkenghwee.move(cafe):\t", _)
    _=kenghwee.do_task("fix wires"); print(_ == "@hweelingdead does fix wires in Cafeteria", "\tkenghwee.do_task(\"fix wires\"):\t", _)

# Uncomment to test question 3
test_q3()

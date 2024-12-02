##############
# Question 1 #
##############

# Your answer here.
# Q1
def jump(target):
    def jumper(curr):
        if curr == target:
            return 0
        case1 = curr + curr//2 + 1
        case2 = curr + (target-curr)//2 + 1
        if case1 > target:
            return 1 + jumper(case2)
        if case2 > target:
            return 1 + jumper(case1)
        else:
            return 1 + min(jumper(case1), jumper(case2))
    return jumper(0)



# Tests
def test_q1():
    print('\nQ1 ' + '-'*30)
    print('pass', 'code'.ljust(8), 'result', sep='\t')
    print('-'*33)

    _ = jump(1); print(_==1, 'jump(1) ', _, sep='\t')
    _ = jump(2); print(_==1, 'jump(2) ', _, sep='\t')
    _ = jump(3); print(_==2, 'jump(3) ', _, sep='\t')
    _ = jump(4); print(_==2, 'jump(4) ', _, sep='\t')
    _ = jump(5); print(_==2, 'jump(5) ', _, sep='\t')
    _ = jump(6); print(_==2, 'jump(6) ', _, sep='\t')
    _ = jump(7); print(_==2, 'jump(7) ', _, sep='\t')
    _ = jump(8); print(_==2, 'jump(8) ', _, sep='\t')
    _ = jump(9); print(_==3, 'jump(9) ', _, sep='\t')
    _ = jump(10); print(_==2, 'jump(10) ', _, sep='\t')
    _ = jump(11); print(_==3, 'jump(11) ', _, sep='\t')
    _ = jump(12); print(_==3, 'jump(12) ', _, sep='\t')
    _ = jump(13); print(_==3, 'jump(13) ', _, sep='\t')
    _ = jump(14); print(_==3, 'jump(14) ', _, sep='\t')
    _ = jump(15); print(_==3, 'jump(15) ', _, sep='\t')
    _ = jump(16); print(_==3, 'jump(16) ', _, sep='\t')
    _ = jump(17); print(_==4, 'jump(17) ', _, sep='\t')
    _ = jump(18); print(_==3, 'jump(18) ', _, sep='\t')
    _ = jump(19); print(_==4, 'jump(19) ', _, sep='\t')
    _ = jump(20); print(_==4, 'jump(20) ', _, sep='\t')

# Uncomment to test question 1
test_q1()


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

# Note: You are allowed to modify the parameters of
#       get_enrollment as long as the execution 
#       behaviour remains consistent.
def get_enrollment(filename, module_code, *class_code):
    data = read_csv(filename)
    data = list(filter(lambda x: x[1] == module_code, data))
    if len(class_code) != 0:
        data = list(filter(lambda x: x[2] == class_code[0], data))
    l = []
    for row in data:
        if row[0] not in l:
            l.append(row[0])
    return len(l)


def top_k_busy(filename, start_date, end_date, k):
    data = read_csv(filename)
    data = filter(lambda x: start_date <= x[3] <= end_date, data)
    d = {}
    def time(t):
        hour, minute = map(int,t.split(':'))
        return hour * 60 + minute
    for row in data:
        student_id = int(row[0])
        if student_id not in d:
            d[student_id] = []
        duration = time(row[5]) - time(row[4])
        d[student_id].append(duration)
    for row in d:
        minutes = d[row]
        d[row] = round(sum(minutes)/60, 1)
    duration = sorted(d.items(), key = lambda x: -x[1])
    if k == 0:
        return []
    elif k > len(duration):
        return duration
    elif k < len(duration):
        kth = duration[k - 1][1]
        duration = list(filter(lambda p: p[1] >= kth, duration))
    return duration



# Tests
def test_q2a():
    print('\nQ2A ' + '-'*60)
    print('pass', 'code'.ljust(42), 'result', sep='\t')
    print('-'*64)

    filename = "modreg_timetable_trimmed.csv"
    test = get_enrollment(filename, "GEQ1000")
    print(test==81, 'get_enrollment(filename, "GEQ1000")       ', test, sep='\t')
    test = get_enrollment(filename, "ACC1701", "LV2")
    print(test==10, 'get_enrollment(filename, "ACC1701", "LV2")', test, sep='\t')
    test = get_enrollment(filename, "CFG1002", "L02")
    print(test==59, 'get_enrollment(filename, "CFG1002", "L02")', test, sep='\t')
    test = get_enrollment(filename, "CS1010S")
    print(test==261, 'get_enrollment(filename, "CS1010S")       ', test, sep='\t')
    test = get_enrollment(filename, "CS1010S", "R01")
    print(test==30, 'get_enrollment(filename, "CS1010S", "R01")', test, sep='\t')
    test = get_enrollment(filename, "CS1010S", "T01")
    print(test==5, 'get_enrollment(filename, "CS1010S", "T01")', test, sep='\t')

def test_q2b():
    print('\nQ2B ' + '-'*70)
    print('pass', 'code'.ljust(51), 'result', sep='\t')
    print('-'*74)

    filename = "modreg_timetable_trimmed.csv"
    test = top_k_busy(filename, "2021-01-01", "2021-04-30", 1)
    print(test == [(239, 446.5)], 'top_k_busy(filename, "2021-01-01", "2021-04-30", 1)', test, sep='\t')
    test = top_k_busy(filename, "2021-01-01", "2021-04-30", 3)
    print(test == [(239, 446.5), (152, 396.0), (22, 383.0)], 'top_k_busy(filename, "2021-01-01", "2021-04-30", 3)', test, sep='\t')
    test = top_k_busy(filename, "2021-02-01", "2021-02-28", 3)
    print(test == [(239, 103.5), (57, 93.0), (152, 93.0)] or
          test == [(239, 103.5), (152, 93.0), (57, 93.0)], 'top_k_busy(filename, "2021-02-01", "2021-02-28", 3)', test, sep='\t')

# Uncomment to test question 2
##test_q2a()
##test_q2b()


##############
# Question 3 #
##############

# Your answer here.
# Q3
class Titan:
    def __init__(self, height):
        self.height = height
        self.alive = True
        self.eaten = []

    def eat(self, scout):
        if not self.alive:
            return "Titan is already dead!"
        else:
            return scout.attack(self)


class Scout:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
        self.eaten = False

    def attack(self, titan):
        if self.eaten:
            return f"{self.name} is currently eaten!"
        elif not titan.alive:
            return "Titan is already dead!"
        elif titan.height >= self.skill:
            self.eaten = True
            titan.eaten.append(self)
            return f'A {titan.height}m Titan eats {self.name}!'
        else:
            titan.alive = False
            output = f'{self.name} kills a {titan.height}m Titan!'
            while titan.eaten:
                scout = titan.eaten.pop()
                scout.eaten = False
                output += f' {scout.name} has been freed!'
            return output



# Tests
def test_q3():
    print('\nQ3  ' + '-'*40)
    print('pass', 'code'.ljust(20), 'result', sep='\t')
    print('-'*44)

    t3 = Titan(3)
    t5 = Titan(5)
    t10 = Titan(10)

    eren = Scout("Eren", 5)  # suicidal maniac
    armin = Scout("Armin", 7)
    mikasa = Scout("Mikasa", 999)  # much imba <3

    _=eren.attack(t3); print(_ == "Eren kills a 3m Titan!", "eren.attack(t3):".ljust(20), _, sep='\t')
    _=t3.eat(eren); print(_ == "Titan is already dead!", "t3.eat(eren):".ljust(20), _, sep='\t')
    _=eren.attack(t3); print(_ == "Titan is already dead!", "eren.attack(t3):".ljust(20), _, sep='\t')
    _=eren.attack(t5); print(_ == "A 5m Titan eats Eren!", "eren.attack(t5):".ljust(20), _, sep='\t')
    _=eren.attack(t10); print(_ == "Eren is currently eaten!", "eren.attack(t10):".ljust(20), _, sep='\t')
    _=t5.eat(eren); print(_ == "Eren is currently eaten!", "t5.eat(eren):".ljust(20), _, sep='\t')
    _=t5.eat(armin); print(_ == "Armin kills a 5m Titan! Eren has been freed!", "t5.eat(armin):".ljust(20), _, sep='\t')
    _=eren.attack(t10); print(_ == "A 10m Titan eats Eren!", "eren.attack(t10):".ljust(20), _, sep='\t')
    _=armin.attack(t10); print(_ == "A 10m Titan eats Armin!", "armin.attack(t10):".ljust(20), _, sep='\t')
    _=mikasa.attack(t10); print(_ == "Mikasa kills a 10m Titan! Armin has been freed! Eren has been freed!", "mikasa.attack(t10):".ljust(20), _, sep='\t')

# Uncomment to test question 3
test_q3()

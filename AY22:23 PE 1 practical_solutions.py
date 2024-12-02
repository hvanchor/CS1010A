##############
# Question 1 #
##############

########## Grading Scheme ##########
# 5: Fully correct
# 4: Fails only edge cases eg. duplicate intervals and/or empty input
# 3: Pass all cases where each interval merges at most once eg. merge_intervals((7,8),(5,6),(2,3),(8,9),(1,2),(4,5),(10,11))
# 2: Attempt to check all pairwise merges: Sort by intervals and then recurse/iterate through sorted intervals OR iterate through intervals with nested loops OR correct recursive call with *intervals together with a relevant loop
# 1: Get min and max and return [(min,max)] OR single loop OR correct recursive call with no loop OR wrong recursive call but with a loop 
# 0: Hardcode for public TCs, wrong recursive call with intervals instead of *intervals, loop(s)/recursion but with no merge function call, loop/recursion always terminates early eg. for i in intervals: return

# To qualify for any marks, loop and/or recursion MUST have merge function call, or equivalent operations to correctly check if two intervals can merge.

####################################

def merge(a, b):
    if a[1] < b[0] or b[1] < a[0]:
        return False
    else:
        return (min(a[0], b[0]), max(a[1], b[1]))

# Recursion
def merge_intervals(*intervals):
    if intervals == ():
        return []
    else:
        result = []
        new = intervals[0]
        for interval in merge_intervals(*intervals[1:]):
            if not merge(new, interval):
                result.append(interval)
            else:
                new = merge(new, interval)
        result.append(new)
        return result

# Iteration with sorting
def merge_intervals(*intervals):
    ints = sorted(intervals)
    i = 0
    while i < len(ints) - 1:
        m = merge(ints[i], ints[i+1])
        if m:
            ints[i] = m
            ints.pop(i+1)
        else:
            i += 1
    return ints

# Iteration without sorting
def merge_intervals(*intervals):
    intervals = list(intervals)
    res = []
    i = 0
    while intervals:
        new = intervals.pop(0)
        merged = False
        for interval in intervals:
            m = merge(new, interval)
            if m:
                intervals.remove(interval)
                intervals.append(m)
                merged = True
                break
        if not merged:
           res.append(new)
    return res

def test_q1():
    print(merge_intervals((1, 2), (3, 4)))
    print(merge_intervals((1, 2), (2, 4)))
    print(merge_intervals((1, 2), (3, 4), (2, 6)))
    print(merge_intervals((7, 12), (3, 9), (1, 4)))
    print(merge_intervals((7, 9), (3, 5), (10, 13), (1, 15)))

# Uncomment to test question 1
# test_q1()

###############
# Helper for Q2
###############

import csv

def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of lists
    containing rows in the csv file and its entries.
    """
    with open(csvfilename, encoding='utf-8') as csvfile:
        return list(csv.reader(csvfile))    

###############
# Question 2a #
###############

########## Grading Scheme ##########
# Each mark will only be awarded in full after fulfilling the
# respective stated requirement for all possible cases.
#
# Partial marks have been awarded as much as possible,
# and have been listed according to each student’s unique code.
#
# Passing all the public test cases is in no way an indication that
# your code has fulfilled all of the criteria.

## [+1] filter channel title
## [+1] filter at least one of views>1000 or likes>1000
## [+1] consider both likes and views
## [+1] remove duplicate video id entries OR [+1] collate sum of likes & views in unique video ids
## [+1] return count

####################################

# Note: We have chosen to accept two possible solutions due to vague PDF description

# remove duplicating video id entries
def get_video_id(channel_title, filename):
    data = read_csv(filename)[1:]
    data = list(filter(lambda x: x[1] == channel_title, data))
    data = list(filter(lambda x: int(x[2]) > 1000 and int(x[3]) > 1000, data))
    unique_ids = []
    for row in data:
        if row[0] not in unique_ids:
            unique_ids.append(row[0])
    return len(unique_ids)

# collate sum of likes & views in unique video ids
def get_video_id_alternate(channel_title, filename):
    data = read_csv(filename)[1:]
    data = list(filter(lambda x: x[1] == channel_title, data))
    unique_ids = {}
    for row in data:
        if row[0] not in unique_ids:
            unique_ids[row[0]] = [0,0]
        unique_ids[row[0]][0] += int(row[2])
        unique_ids[row[0]][1] += int(row[3])
    result = unique_ids.values()
    result = list(filter(lambda x: x[0] > 1000 and x[1] > 1000, result))
    return len(result)

def test_q2a():
    filename = 'YouTubeStat.csv'
    _ = get_video_id('NFL', filename); print(_==13, "get_video_id('NFL', 'YouTubeStat.csv')", _, sep='\t')
    _ = get_video_id('HBO', filename); print(_==2, "get_video_id('HBO', 'YouTubeStat.csv')", _, sep='\t')
    _ = get_video_id('20th Century Fox', filename); print(_==4, "get_video_id('20th Century Fox', 'YouTubeStat.csv')", _, sep='\t')

# Uncomment to test question 2a
# test_q2a()

###############
# Question 2b #
###############

########## Grading Scheme ##########

## [+1] Group by channel title
## [+0.5] Calculate total likes and total views correctly
## [+1.5] Calculate the ratio of total views to likes correctly,
##        handles likes == 0 and round off to 1 dp
## [+1] Sorting and return top-k channels
## [+0.5] Handle ties
## [+0.5] Handle edge cases where k > len(data)

####################################

def top_k_channels(k, filename):
    data = read_csv(filename)[1:]
    table = {}
    for video_id, channel_title, view, likes in data:
        if channel_title not in table:
            table[channel_title] = []
        table[channel_title].append((int(view), int(likes)))
        
    result = []
    for key, value in table.items():
        tot_view, tot_likes = 0, 0
        for val in value:          
            tot_view += val[0]
            tot_likes += val[1]
        if tot_likes == 0:
            ratio = 0
        else:
            ratio = round(tot_view / tot_likes, 1)
        result.append((key, ratio))
    
    result.sort(key = lambda x: x[1], reverse = True)

    while (k < len(result)) and (result[k-1][1] == result[k][1]):
        k += 1
    return result[:k]

def test_q2b():
    filename = 'YouTubeStat.csv'
    _ = top_k_channels(2, filename); print(_==[('Made by Google', 2183792.0), ('MarenMorris', 939565.8)], "top_k_channels(2, 'YouTubeStat.csv')", _, sep='\t')
    _ = top_k_channels(5, filename); print(_==[('Made by Google', 2183792.0), ('MarenMorris', 939565.8), ('Douglas Thron', 929068.2), ('Tinder', 875988.2), ('Huckabee', 279484.8)], "top_k_channels(5, 'YouTubeStat.csv')", _, sep='\t')
    _ = top_k_channels(7, filename); print(_==[('Made by Google', 2183792.0), ('MarenMorris', 939565.8), ('Douglas Thron', 929068.2), ('Tinder', 875988.2), ('Huckabee', 279484.8), ('Jhené Aiko', 252895.5), ('Las Vegas Metropolitan Police', 198139.4)], "top_k_channels(7, 'YouTubeStat.csv')", _, sep='\t')
    _ = top_k_channels(8, filename); print(_==[('Made by Google', 2183792.0), ('MarenMorris', 939565.8), ('Douglas Thron', 929068.2), ('Tinder', 875988.2), ('Huckabee', 279484.8), ('Jhené Aiko', 252895.5), ('Las Vegas Metropolitan Police', 198139.4), ('Snapchat', 138256.2)], "top_k_channels(8, 'YouTubeStat.csv')", _, sep='\t')

# Uncomment to test question 2a
# test_q2b()

##############
# Question 3 #
##############

########## Grading Scheme ##########
# [-0.5] Wrongly return strings as per PDF
### COVID Class - 1.5 Marks
### Init
# [+0.5] Correctly initialise COVID name
### Mutate Method
# [+0.5] Correctly return new COVID object
# [+0.5] Correctly add variant(s) to child
### Person Class - 3.5 Marks
### Init
# [+0.5] Initialise Person with name, infected variants and immune variants
### Infect method
# [+0.5] Correctly check immunity before infecting
# [+0.5] Correctly update infected variants
# [+0.5] Correctly update immune variants
### Recover method
# [+0.5] Correctly implement recover method - checks if infected and clears infected variant(s)
### Meet method
# Not awarded if you do not use infect and your implementation is wrong
# Correctly - updates parent variants of other Person's infected variants into self's immunity
# [+0.5] Correctly infect self with other variants
# [+0.5] Correctly infect other with self variants

####################################

## Only storing direct parent for COVID class
class COVID:
    def __init__(self, name):
        self.name = name
        self.parent = None
        
    def mutate(self, name):
        variant = COVID(name)
        variant.parent = self
        return variant

class Person:
    def __init__(self, name):
        self.name = name
        self.immune = []
        self.infected = []

    def infect(self, variant):
        if variant not in self.immune:
            self.infected.append(variant)
            name = variant.name
            while variant and variant not in self.immune:
                self.immune.append(variant)
                variant = variant.parent
            return f'{self.name} contracted {name}'
        else:
            return f'{self.name} is immune to {variant.name}'

    def recover(self):
        if self.infected:
            self.infected.clear()
            return f'{self.name} recovers from COVID'
        else:
            return f'{self.name} is COVID negative'

    def meet(self, person):
        for variant in self.infected:
            person.infect(variant)
        for variant in person.infected:
            self.infect(variant)
            
## Storing entire parent lineage for COVID class
class COVID:
    def __init__(self, name):
        self.name = name
        self.parent = []
        
    def mutate(self, name):
        variant = COVID(name)
        variant.parent.extend(self.parent + [self])
        return variant

class Person:
    def __init__(self, name):
        self.name = name
        self.immune = []
        self.infected = []

    def infect(self, variant):
        if variant not in self.immune:
            self.infected.append(variant)
            self.immune.append(variant)
            self.immune.extend(variant.parent)
            return f'{self.name} contracted {variant.name}'
        else:
            return f'{self.name} is immune to {variant.name}'

    def recover(self):
        if self.infected:
            self.infected.clear()
            return f'{self.name} recovers from COVID'
        else:
            return f'{self.name} is COVID negative'

    def meet(self, person):
        for variant in self.infected:
            person.infect(variant)
        for variant in person.infected:
            self.infect(variant)

# Tests
def test_q3():
    alpha = COVID('Alpha')
    delta = alpha.mutate('Delta')
    bravo = COVID('Bravo')
    gamma = bravo.mutate('Gamma')
    lambd = bravo.mutate('Lambda')
    omicron = lambd.mutate('Omicron')
    waikay = Person('Wai Kay')
    ashish = Person('Ashish')
    nitya = Person('Nitya')
    _=waikay.infect(delta); print(_ == 'Wai Kay contracted Delta', "\twaikay.infect(delta)  \t", repr(_))
    _=waikay.infect(alpha); print(_ == 'Wai Kay is immune to Alpha', "\twaikay.infect(alpha)  \t", repr(_))
    _=waikay.recover(); print(_ == 'Wai Kay recovers from COVID', "\twaikay.recover()      \t", repr(_))
    _=waikay.infect(delta); print(_ == 'Wai Kay is immune to Delta', "\twaikay.infect(delta)  \t", repr(_))
    _=waikay.meet(ashish); print(_ == None, "\twaikay.meet(ashish)   \t", repr(_))
    _=waikay.infect(lambd); print(_ == 'Wai Kay contracted Lambda', "\twaikay.infect(lambd)  \t", repr(_))
    _=waikay.infect(bravo); print(_ == 'Wai Kay is immune to Bravo', "\twaikay.infect(bravo)  \t", repr(_))
    _=waikay.infect(omicron); print(_ == 'Wai Kay contracted Omicron', "\twaikay.infect(omicron)\t", repr(_))
    _=waikay.meet(ashish); print(_ == None, "\twaikay.meet(ashish)   \t", repr(_))
    _=ashish.infect(omicron); print(_ == 'Ashish is immune to Omicron', "\tashish.infect(omicron)\t", repr(_))
    _=waikay.infect(gamma); print(_ == 'Wai Kay contracted Gamma', "\twaikay.infect(gamma)  \t", repr(_))
    _=nitya.infect(alpha); print(_ == 'Nitya contracted Alpha', "\tnitya.infect(alpha)   \t", repr(_))
    _=nitya.meet(ashish); print(_ == None, "\tnitya.meet(ashish)    \t", repr(_))
    _=nitya.infect(omicron); print(_ == 'Nitya is immune to Omicron', "\tnitya.infect(omicron) \t", repr(_))
    _=ashish.infect(alpha); print(_ == 'Ashish is immune to Alpha', "\tashish.infect(alpha)  \t", repr(_))
    _=nitya.infect(delta); print(_ == 'Nitya contracted Delta', "\tnitya.infect(delta)   \t", repr(_))
    _=nitya.infect(gamma); print(_ == 'Nitya contracted Gamma', "\tnitya.infect(gamma)   \t", repr(_))
    _=ashish.recover(); print(_ == 'Ashish recovers from COVID', "\tashish.recover()      \t", repr(_))
    _=ashish.recover(); print(_ == 'Ashish is COVID negative', "\tashish.recover()      \t", repr(_))
    _=ashish.infect(gamma); print(_ == 'Ashish contracted Gamma', "\tashish.infect(gamma)  \t", repr(_))

# Uncomment to test question 3
# test_q3()

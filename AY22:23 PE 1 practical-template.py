##############
# Question 1 #
##############
def merge(a, b):
    if a[1] < b[0] or b[1] < a[0]:
        return False
    else:
        return (min(a[0], b[0]), max(a[1], b[1]))


def merge_intervals(*intervals):
    inter = sorted(intervals)
    i = 0
    while i < len(inter) - 1:
        mer = merge(inter[i], inter[i+1])
        if mer:
            inter[i] = mer
            inter.pop(i+1)
        else:
            i += 1
    return inter


def test_q1():
    print(merge_intervals((1, 2), (3, 4)))
    print(merge_intervals((1, 2), (2, 4)))
    print(merge_intervals((1, 2), (3, 4), (2, 6)))
    print(merge_intervals((7, 12), (3, 9), (1, 4)))
    print(merge_intervals((7, 9), (3, 5), (10, 13), (1, 15)))


# Uncomment to test question 1
#test_q1()


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

def get_video_id(channel_title, filename):
    data = filter(lambda x: x[1] == channel_title, read_csv(filename)[1:])
    l = []
    count = 0
    for row in data:
        v_id, views, likes = row[0], int(row[2]), int(row[3])
        if views > 1000 and likes > 1000:
            if v_id not in l:
                l.append(v_id)
                count += 1
    return count
    
            
            


def test_q2a():
    filename = 'YouTubeStat.csv'
    _ = get_video_id('NFL', filename); print(_==13, "get_video_id('NFL', 'YouTubeStat.csv')", _, sep='\t')
    _ = get_video_id('HBO', filename); print(_==2, "get_video_id('HBO', 'YouTubeStat.csv')", _, sep='\t')
    _ = get_video_id('20th Century Fox', filename); print(_==4, "get_video_id('20th Century Fox', 'YouTubeStat.csv')", _, sep='\t')


# Uncomment to test question 2a
#test_q2a()

###############
# Question 2b #
###############


def top_k_channels(k, filename):
    data = read_csv(filename)[1:]
    d = {}
    for row in data:
        v_id, channel, views, likes = row[0], row[1], int(row[2]), int(row[3])
        if channel not in d:
            d[channel] = []
            channel_l = []
        if v_id not in channel_l:
            d[channel].append((views, likes))
            channel_l.append(v_id)
    result = []    
    for channel, vl in d.items():
        tot_view, tot_like = 0, 0
        for v in vl:
            tot_view += v[0]
            tot_like += v[1]
        if tot_like == 0:
            ratio = 0
        else:
            ratio = round(tot_view/tot_like, 1)
        result.append((channel, ratio))

    result = sorted(result, key = lambda x: x[1], reverse = True)

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
#test_q2b()

##############
# Question 3 #
##############

# Your answer here.
# Q3

class COVID:
    def __init__(self, name):
        self.name = name
        self.parent = None

    def mutate(self, new):
        variant = COVID(new)
        variant.parent = self
        return variant
        

class Person:
    def __init__(self, name):
        self.name = name
        self.immunity = []
        self.covid = []

    def infect(self, covid):
        if covid not in self.immunity:
            self.covid.append(covid)
            name = covid.name
            while covid and covid not in self.immunity:
                self.immunity.append(covid)
                covid = covid.parent
            return f"{self.name} contracted {name}"
        else:
            return f"{self.name} is immune to {covid.name}"

    def recover(self):
        if self.covid:
            self.covid.clear()
            return f"{self.name} recovers from COVID"
        else:
            return f"{self.name} is COVID negative"

    def meet(self, person):
        if self.covid:
            for covid in self.covid:
                if covid not in person.covid:
                    person.infect(covid)
        if person.covid:
            for covid in person.covid:
                if covid not in self.covid:
                    self.infect(covid)

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
test_q3()

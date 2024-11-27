##############
# Question 1 #
##############
#######
# q1a #
#######
'''
# OBSERVE CASES
game = [[0,10], [20,30], [40,50]]
caseA = valid_move(game, 20, 30) # within group
caseB = valid_move(game, 14, 16) # outside of group
caseC = valid_move(game, 15, 25) # outside/inside
caseD = valid_move(game, 25, 35) # inside/outside
caseE = valid_move(game, 15, 35) # both outside but contain group
caseF = valid_move(game, 25, 45) # both inside, but across two groups
caseG = valid_move(game, 15, 55) # both outside, but across two groups
caseH = valid_move([[0,10], [20,30], [40,50]], 5 , 45) # span across 3 groups
caseI = valid_move([[2, 4]], 1, 5) # across single and only group


Grading scheme (code compiles)
An eval test case is one of the private test case (so case A&B counts as one and not two).
5: Passes all eval test cases
4: Passes up to 5 eval test cases.
3: Passes 3 eval test cases (with at least 1 from the first 3 eval test cases)
2: Passes 2 eval test cases (with at least 1 from first 3 eval test cases) and shows some partially correct logic in code (does not just return True all the time).
1: Passes 1 eval test case from first 3 eval test cases, and shows some partially correct logic in code (important to check the logic because some people’s code just simply returns True/False always, even if they have for loops, etc) OR checks whether start or end is in the list represented by the pile OR checks whether start or end is within the range represented by that pile (works for sorted)
0: Brute force to pass public test cases/blank submission

Grading scheme (code does not compile) - max 3 marks
3: Minor syntax error (code runs correctly when fixed)
2: Code has multiple MINOR bugs but will run correctly when fixed
1: "Code" is mixed with pseudocode explaining correct algorithm OR checks whether start/end is in the list represented by the pile OR checks whether start/end is within the range of represented by that pile (works for sorted)
0: "Code"
'''
def valid_move(game, start, end):
 return 1 == len(tuple(filter(lambda interval: any(interval[0] <= x <= interval[1] for x in range(start, end+1)), game)))

def valid_move(game, start, end):
    removed = False
    for left, right in game:
        if start <= right and left <= end:
            if removed:
                return False
            else:
                removed = True
    return removed


#######
# q1b #
#######
'''
game = [[0,10], [20,30], [40,50]]
caseA_ = make_move(game, 15, 35) # remove group totally, exceed boundary
caseA  = make_move(game, 20, 30) # remove group totally, matching exact boundary

caseB_ = make_move(game, 25, 35) # remove right half only, exceed boundary
caseB  = make_move(game, 25, 30) # remove right half only, matching exact boundary

caseC_  = make_move(game, 15, 25) # remove left half only, exceed boundary
caseC = make_move(game, 20, 25) # remove left half only, matching exact boundary

caseD = make_move(game, 25, 25) # splits group into two
caseE = make_move(game, 21, 29) # leaves only 1 match in group(s)

Grading scheme (code compiles)
5: Correct output for input all n
4: Passes ABCDE but fails at least one other OR Code returns a new list but would be correct if it returns the original list
3: Passes D and E and (1 or 2 other private test cases)
2: Passes all 3 public test cases OR Passes D and E
1: Locates the correct pile that will have some matchsticks removed from it OR returns the original game with attempted modification OR locate the correct remaining matchsticks
0: Brute force to pass public test cases/blank submission

Grading scheme (code does not compile) - max 3 marks
3: Minor syntax error (code runs correctly when fixed)
2: Code has multiple MINOR bugs but will run correctly when fixed
1: "Code" is mixed with pseudocode explaining correct algorithm
0: "Code"
'''
def make_move(game, start, end):
    if not valid_move(game, start, end):
        raise Exception('Invalid Move')
    for i in range(len(game)):
        if i >= len(game): break
        left, right = game[i]
        # 4 cases
        # remove whole cluster
        if start <= left and right <= end:
            game.pop(i)
        # remove left part of cluster
        elif start <= left and left <= end < right:
            game[i][0] = end + 1
        # remove right part of cluster
        elif left < start <= right and right <= end:
            game[i][1] = start - 1
        # split cluster into two
        elif left < start and end < right:
            game.insert(i+1, [end + 1, game[i][1]])
            game[i][1] = start - 1
    return game


##############
# Question 2 #
##############
#######
# q2a #
#######
'''
Grading scheme
If the student used a get_distance function that does not round off, then try their code with the get_distance function with rounding, then mark accordingly
[+1] Extracts longitude and latitude from row  [0.5 for pseudocode/minor mistake]
[+1] Use get_distance correctly and convert lat and long to floats [0.5 if did not float]
[+1] Sort by distance               [0.5 for pseudocode/minor mistake] !!!Have to be paired with the id to be awarded the mark
[+1] Extract top k                  [0.5 for pseudocode/minor mistake]
[+1] Handles tie cases (this is checked by the evaluation test case) [no marks for pseudocode]
     i.e no out-of-index errors etc. 

[-0.5] Student returned distance instead of ids
'''
def k_nearest_listings(fname, latitude, longitude, k):
    data = read_csv(fname)[1:] # drop header

    # 1. sort via distance latitude [4] and longitude [5]
    data = sorted(data, key=lambda row: get_distance(float(row[4]),
                                                     float(row[5]),
                                                     latitude,
                                                     longitude)
                 )
    # if there is an error in the try-block below, means k >= len(data)
    try:
        # 2. obtain the k-th closest listing (0-indexing)
        k_listing = data[k-1]
        k_dist = get_distance(float(k_listing[4]), float(k_listing[5]), latitude, longitude)

        # 3. keep moving the pointer k forward when encounter a tie
        while get_distance(float(data[k][4]), float(data[k][5]), latitude, longitude) == k_dist:
            k += 1
    
    finally:
        # 4. get top k entries and extract listing id [0] as integer
        return list(map(lambda row: int(row[0]), data[:k]))

#######
# q2b #
#######
'''
Grading scheme
[+1] Extract prices per row (does not necessarily need to store)     [0.5 if did not int]
[+1] Filter by region            [0.5 if select neighbourhood col instead]
[+1] Filter by at least 1 review [0 if not comparing int correctly]
[+1] Compute averages correctly  [0.5 if did not round]
[+1] Returns dictionary with correct neighbourhood → price format
     !!! Do not accept hard-coded keys into neighbourhood,
         since neighbourhoods may change per region !!!
'''
def neighbourhood_price_per_region(fname, region):
    data = read_csv(fname)[1:] # drop header
    # 1. filter by at least 1 review [7] and region [2]
    data = list(filter(lambda row: int(row[7])>0 and row[2] == region, data))
    # 2. store neighbourhood [3] as key, and prices [6] as value in a list
    neighbourhood_prices = {}
    for row in data:
        if row[3] not in neighbourhood_prices:
            neighbourhood_prices[row[3]] = []
        neighbourhood_prices[row[3]].append(int(row[6]))

    # 3. convert to average price
    for neighbourhood, prices in neighbourhood_prices.items():
        neighbourhood_prices[neighbourhood] = round(sum(prices)/len(prices),2)
    return neighbourhood_prices


##############
# Question 3 #
##############
class Doll:
    # [+0.5] all methods definitions and arguments exist.
    #        (check method signature, method name and num of args)

    # [+1] for name, mother, daughter attributes
    # [+0.5] for additional attribute to maintain series
    #   `-> [0] if student used an attribute called self.series which would
    #           result in name conflict with the method. Mark everything
    #           else as if self.set was used as the attribute instead


    def __init__(self, name):
        self.name = name
        self.mother = None
        self.daughter = None
    # if stored self.name instead of self object (refer to encase)
        self.set = [self]

    # [+0.5] returns name correctly
    def get_name(self):
        return self.name

    # [+1]   returns both mother and daughter object correctly
    #   `-> [0.5] returns mother and/or daughter's name instead of object
    def get_mother(self):
        return self.mother

    def get_daughter(self):
        return self.daughter

    # [+0.5] correct ordering of checks and string correct associated with respective check
    #        No need to minus marks if typo in returned string '''
    def encase(self, other):
        if self.daughter:
            return f"{self.name} already contains {self.daughter.name}"
        elif self.mother:
            return f"{self.name} is currently encased in {self.mother.name}"
        elif other.mother:
            return f"{other.name} is currently encased in {other.mother.name}"
        else:
    # [+0.5] updates self.daughter
    # [+0.5] updates other.mother '''
            self.daughter = other
            other.mother = self
    
    # [+1] updates all states for series correctly
    #    -> [0.5] updates states for series, but incorrectly ''' OR if name stored in self.set instead of object since it will not update state of set correctly
    #       [0] if missing self.set attribute		
            self.set.remove(self)
            other.set.append(self)	
            self.set = other.set
            return f'{self.name} encases {other.name}'        

    # [+0.5] correct ordering of checks and string correct associated with respective check
    #       No need to minus marks if typo in returned string ''
    def release(self):
        if self.mother:
            return f'{self.name} is currently encased in {self.mother.name}'
        elif not self.daughter:
            return f'{self.name} does not contain any dolls'
        else:
    # [+1]   updates both self.daughter AND other.mother correctly AND does not change self.set/other.set
    	# [0.5] updates only one correctly, due to order-of-operations
            # OR lost reference to daughter's name
            # OR updates both self.daughter and other.mother correctly and
            # changes self.set or self.series''
            msg = f'{self.name} releases {self.daughter.name}'   
            self.daughter.mother = None
            self.daughter = None
            return msg

    # [+0.5] returning a count based on dolls in the series e.g. use len()
    # [+0.5] filter on dolls with mothers present or equivalent '''
    # [0] if missing self.set attribute	
    def num_encased(self):
        return len(list(filter(lambda doll: doll.mother is not None, self.set)))
    
    # [+0.5] iterates through all dolls in the state and extracts out doll names from doll objects
    #    Assume state maintains correct series
    #    No need to deduct if return list or map object instead '''
    #  [0] if missing self.set attribute	
    def series(self):
        return tuple(map(lambda doll: doll.name, self.set))
    
    # [+1] checks arbitrarily deep correctly
    #   |-> [0.5] for minor errors
    #   `-> [0] marks for shallow check
    #     may need to also grade helper functions, if used '''
    #  [0] marks if student uses self.set or series to check
    def deeply_contains(self, other):        
        if self.daughter == other:
            return True
        elif self.daughter:
            return self.daughter.deeply_contains(other)
        else:
            return False

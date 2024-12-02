##############
# Question 1 #
##############

#  Grading Scheme

## Recursive Solution
## [+1] Attempt at coding some base case AND recursion
## [+0.5] Correct handling for the case where pos in board[1] (ladders)
## [+0.5] Correct handling for the case where pos in board[2] (chutes)
## [+1] Attempt at recursive relation (some semblance of a sum of six
##      recursive calls using moves in range(1,7))
## [+1] Correct recursive relation
## [+1] Fully correct solution

## Iterative Solution
## [+1] Attempt at coding iteration (must involve board[0] and pos)
## [+0.5] Correct handling for the case where i in board[1] (ladders)
## [+0.5] Correct handling for the case where i in board[2] (chutes)
## [+1] Attempt at iteratively calculating the answer for i (some semblance
##      of a sum of the six previous answers)
## [+1] Correct iterative relation
## [+1] Fully correct solution



def num_plays(pos, board):
    if pos < 1:
        return 0
    elif pos >= board[0]:
          return 1
    else:
        if (pos in board[2]):
            # player is on top of a chute
            return 0
        elif (pos in board[1]):
            # player is at the bottom of a ladder
            pos = board[1][pos]
        res = 0
        for moves in range(1, 7):
            res += num_plays(pos + moves, board)
        return res

def test_q1():
    board1 = (14, {2: 12, 7: 12}, {13: 3, 9: 4})
    board2  = (10, {5: 8}, {9: 1, 7: 4})
    _ = num_plays(13, board1); print(_==0, 'num_plays(13, board1) ', _, sep='\t')
    _ = num_plays(12, board1); print(_==5, 'num_plays(12, board1) ', _, sep='\t')
    _ = num_plays(1, board2); print(_==143, 'num_plays(1, board2) ', _, sep='\t')
    _ = num_plays(3, board2); print(_==37, 'num_plays(3, board2) ', _, sep='\t')
    _ = num_plays(5, board2); print(_==5, 'num_plays(5, board2) ', _, sep='\t')

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
        rows = [row for row in csv.reader(csvfile)]
    return rows

###############
# Question 2a #
###############

#  Grading Scheme
# Each mark will only be awarded in full after fulfilling the respective
# stated requirement for all possible cases. 
# Partial marks have been awarded as much as possible, and have been listed
# according to each student’s unique code. 
# Passing all the public test cases is in no way an indication that your
# code has fulfilled all of the criterias.

## [+1] successfully filtered data for the input area
## [+1] checked for invalid area and returned an empty tuple
## [+1] identified the oldest year 
## [+1] successfully filtered houses built in the oldest year
## [+1] returned highest price (float) of the house built in oldest year (int)


def get_antiques(fname, area):
    data = read_csv(fname)[1:]
    
    data = list(filter(lambda x:x[-1] == str(area), data))
    
    if not data:
        return ()
    
    oldest = min(map(lambda x: int(x[-2]), data))
    data = filter(lambda x:x[-2] == str(oldest), data)

    return (oldest, max(map(lambda x: float(x[0]), data)))


def test_q2a():
    _ = get_antiques("house_data.csv", 98001); print(_==(1903, 230000.0), "num_subscribers('house_data.csv', 98001) ", _, sep='\t')
    _ = get_antiques("house_data.csv", 98002); print(_==(1908, 111300.0), "num_subscribers('house_data.csv', 98002) ", _, sep='\t')
   
    
# Uncomment to test question 2a
# test_q2a()

###############
# Question 2b #
###############

#  Grading Scheme
## [+0.5] Convert price to float
## [+1] Group by zipcode
## [+0.5] Calculate price/sqft correctly
## [+1] Get average price
## [+1] Sorting and top-k
## [+0.5] Handle ties
## [+0.5] Handle edge cases where k > len(data)


def topk_expensive_neighbourhoods(fname, k):
    # Read data
    data = read_csv(fname)[1:]
    
    # Create a dictionary to store groups
    grouped_data = {}
    # Iterate through the data
    for price, bedrooms, bathrooms, sqft_living, floors, yr_built, zipcode in data:
        # Convert to integers, then add to corresponding zipcodes
        # It's important to convert price to float instead of int because of the raw data's formatting
        price, sqft_living, zipcode = float(price), int(sqft_living), int(zipcode)
        if zipcode not in grouped_data:
            grouped_data[zipcode] = []
        grouped_data[zipcode].append(price / sqft_living)

    # Convert list to average
    for zipcode in grouped_data:
        prices = grouped_data[zipcode]
        grouped_data[zipcode] = round(sum(prices) / len(prices), 2)
    
    # Sort dictionary items, both method works
    result = sorted(grouped_data.items(), key=lambda pair: -pair[1])
    ## result = sorted(grouped_data.items(), key=lambda pair: pair[1], reverse=True)

    # Handle edge cases
    if k == 0:
        return []
    elif k > len(result):
        return result
    
    # Get the value of the kth person, filter everyone with value at least that
    kth_val = result[k - 1][1]
    return list(filter(lambda pair: pair[1] >= kth_val, result))
 

def test_q2b():
    _ = topk_expensive_neighbourhoods("house_data.csv", 1); print(_==[(98039, 568.24)], "topk_expensive_neighbourhoods('house_data.csv', 1)", _, sep='\t')
    _ = topk_expensive_neighbourhoods("house_data.csv", 2); print(_==[(98039, 568.24), (98004, 475.61)], "topk_expensive_neighbourhoods('house_data.csv', 2)", _, sep='\t')

    
# Uncomment to test question 2b
# test_q2b()

##############
# Question 3 #
##############

# Your answer here.
# Q3

#  Grading Scheme
## [+2] Correct implementation of sell method
##     [+0.5] Correctly handles sale of non-existent Token instance
##     [+0.5] Correctly handles insufficient buyer balance
##     [+0.5] Correctly transfers ownership of token (uses Token instances)
##        THEN [+0.5] Uses token_bought AND token_sold method to buy/sell
##
## [+3] Correct implementation of Contract class
##     [+0.5] init method has no errors and at least stores the args given
##     [+0.5] Correctly handles minting of less than 1 NFT AND correctly
##            handles insufficient funds
##     [+0.5] Correctly mints tokens (i.e. creates Token instances))
##        THEN [+0.5] Uses token_bought method in mint to transfer Token
##                    instance
##     [+0.5] Attempts to keep track of minted tokens (use of iteration or
##            pop/remove)
##        THEN [+0.5] Mints and and returns the correct number of token AND
##                    correctly handles maximum supply minted

class Token:
    def __init__(self, ID, metadata):
        self.id = ID
        self.metadata = metadata
       
class Wallet:
    def __init__(self, address, amount):
        self.address = address
        self.balance = amount
        self.tokens = []
 
    def get_balance(self):
        return self.balance
 
    def token_bought(self, token, buying_price):
        self.tokens.append(token)
        self.balance -= buying_price
 
    def token_sold(self, token, selling_price):
        self.tokens.remove(token)
        self.balance += selling_price
 
    def sell(self, buyer, sell_price, token_id):
        tkn = list(filter(lambda x:x.id == token_id, self.tokens))
        if not tkn:
            return f'NFT #{token_id} does not exist in wallet {self.address}.'
        elif buyer.balance < sell_price:
            return "Buyer does not have enough funds to make the purchase."
        else:
            tkn = tkn[0]
            self.token_sold(tkn, sell_price)
            buyer.token_bought(tkn, sell_price)
            return f'NFT #{token_id} transferred from wallet {self.address} to wallet {buyer.address}.'
   
class Contract:
    def __init__(self, name, price, tokens):
        self.name = name
        self.price = price
        self.tokens = tokens
 
    def mint(self, wallet, num):
        if num < 1:
            return "You need to mint at least one NFT."
        elif wallet.get_balance() < (num * self.price):
            return "Buyer does not have enough funds to mint."
        elif num > len(self.tokens):
            return "Max supply of NFTs exceeded."
        else:
            out = ""
            for _ in range(num):
                tkn = Token(*self.tokens.pop(0)) ## Use of unpacking operator here
                wallet.token_bought(tkn, self.price)
                out += f'NFT #{tkn.id} minted to wallet {wallet.address}, '
            return out

def test_q3():
    kelvin_wallet = Wallet('0x1234abcde', 0.03)
    ashish_wallet = Wallet('0x36912CDEF', 0.09)
    nft_data = [(1, '001.jpg'), (2, '002.jpg'), (3, '003.jpg')]
    nft_contract = Contract('0x2468defAB', 0.03, nft_data)
    _=nft_contract.mint(kelvin_wallet, 0); print(_ == 'You need to mint at least one NFT.', "\tnft_contract.mint(kelvin_wallet, 0)  \t", repr(_))
    _=nft_contract.mint(kelvin_wallet, 2); print(_ == 'Buyer does not have enough funds to mint.', "\tnft_contract.mint(kelvin_wallet, 2)  \t", repr(_))
    _=nft_contract.mint(kelvin_wallet, 1); print(_ == 'NFT #1 minted to wallet 0x1234abcde, ', "\tnft_contract.mint(kelvin_wallet, 1)   \t", repr(_))
    _=kelvin_wallet.sell(ashish_wallet, 0.1, 1); print(_ == 'Buyer does not have enough funds to make the purchase.', "\tkelvin_wallet.sell(ashish_wallet, 0.1, 1) \t", repr(_))
    _=kelvin_wallet.sell(ashish_wallet, 0.03, 2); print(_ == 'NFT #2 does not exist in wallet 0x1234abcde.', "\tkelvin_wallet.sell(ashish_wallet, 0.03, 2)   \t", repr(_))
    _=kelvin_wallet.sell(ashish_wallet, 0.09, 1); print(_ == 'NFT #1 transferred from wallet 0x1234abcde to wallet 0x36912CDEF.', "\tkelvin_wallet.sell(ashish_wallet, 0.09, 1) \t", repr(_))
    _=nft_contract.mint(kelvin_wallet, 3); print(_ == 'Max supply of NFTs exceeded.', "\tnft_contract.mint(kelvin_wallet, 3) \t", repr(_))
    _=nft_contract.mint(kelvin_wallet, 2) ; print(_ == 'NFT #2 minted to wallet 0x1234abcde, NFT #3 minted to wallet 0x1234abcde, ', "\tnft_contract.mint(kelvin_wallet, 2) \t", repr(_))

    
# Uncomment to test question 3
# test_q3()

##############
# Question 1 #
##############
import random
import token


def num_plays(pos, board):
    num_squares = board[0]
    ladders = board[1]
    chutes = board[2]
    if pos < 1:
        return 0
    elif pos >= num_squares:
        return 1
    else:
        if pos in chutes:
            return 0
        elif pos in ladders:
            pos = ladders[pos]
        count = 0
        for i in range(1,7):
            count += num_plays(pos + i, board)
        return count


def test_q1():
    board1 = (14, {2: 12, 7: 12}, {13: 3, 9: 4})
    board2  = (10, {5: 8}, {9: 1, 7: 4})
    _ = num_plays(13, board1); print(_==0, 'num_plays(13, board1) ', _, sep='\t')
    _ = num_plays(12, board1); print(_==5, 'num_plays(12, board1) ', _, sep='\t')
    _ = num_plays(1, board2); print(_==143, 'num_plays(1, board2) ', _, sep='\t')
    _ = num_plays(3, board2); print(_==37, 'num_plays(3, board2) ', _, sep='\t')
    _ = num_plays(5, board2); print(_==5, 'num_plays(5, board2) ', _, sep='\t')

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
        rows = [row for row in csv.reader(csvfile)]
    return rows

###############
# Question 2a #
###############

def get_antiques(fname, area):
    data = list(filter(lambda x: x[6] == str(area), read_csv(fname)[1:]))
    if not data:
        return ()
    oldest = min(map(lambda x: int(x[5]), data))
    data = filter(lambda x: x[5] == str(oldest), data)
    expensive = max(map(lambda x: float(x[0]), data))
    return (oldest, expensive)


def test_q2a():
    _ = get_antiques("house_data.csv", 98001); print(_==(1903, 230000.0), "num_subscribers('house_data.csv', 98001) ", _, sep='\t')
    _ = get_antiques("house_data.csv", 98002); print(_==(1908, 111300.0), "num_subscribers('house_data.csv', 98002) ", _, sep='\t')
   
    
# Uncomment to test question 2a
#test_q2a()

###############
# Question 2b #
###############


def topk_expensive_neighbourhoods(fname, k):
    data = list(read_csv(fname)[1:])
    d = {}
    for rows in data:
        zip = rows[6]
        price = float(rows[0])
        sq_ft = int(rows[3])
        if zip not in d:
            d[zip] = []
        d[zip].append(price/sq_ft)
    for zip in d:
        prices = d[zip]
        d[zip] = round(sum(prices)/len(prices), 2)
    prices = sorted(d.items(), key = lambda x: -x[1])
    if k == 0:
        return []
    elif k > len(prices):
        return prices
    kth_val = prices[k-1][1]
    return list(filter(lambda x: x[1] >= kth_val, prices))


def test_q2b():
    _ = topk_expensive_neighbourhoods("house_data.csv", 1); print(_==[(98039, 568.24)], "topk_expensive_neighbourhoods('house_data.csv', 1)", _, sep='\t')
    _ = topk_expensive_neighbourhoods("house_data.csv", 2); print(_==[(98039, 568.24), (98004, 475.61)], "topk_expensive_neighbourhoods('house_data.csv', 2)", _, sep='\t')

    
# Uncomment to test question 2b
#test_q2b()

##############
# Question 3 #
##############

# Your answer here.
# Q3
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
        tkn = list(filter(lambda x: x.id == token_id, self.tokens))
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
    def __init__(self, name, value, tokens):
        self.name = name
        self.value = value
        self.tokens = tokens

    def mint(self, wallet, n):
        if n < 1:
            return "You need to mint at least one NFT."
        elif wallet.get_balance() < (n * self.value):
            return "Buyer does not have enough funds to mint."
        elif n > len(self.tokens):
            return "Max supply of NFTs exceeded"
        else:
            output = ""
            for i in range(n):
                tkn = Token(*self.tokens.pop(0))  ## Use of unpacking operator here
                wallet.token_bought(tkn, self.value)
                output += f'NFT #{tkn.id} minted to wallet {wallet.address}, '
            return output


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

##############
# Question 1 #
##############

def num_walls(size):
    if size < 1:
        return 0
    elif size == 1:
        return 6
    return num_walls(size-1) + 3*(2*size-1) + 4

def test_q1():
    _ = num_walls(0); print(_==0, 'num_walls(0) ', _, sep='\t')
    _ = num_walls(1); print(_==6, 'num_walls(1) ', _, sep='\t')
    _ = num_walls(2); print(_==19, 'num_walls(2) ', _, sep='\t')
    _ = num_walls(3); print(_==38, 'num_walls(3) ', _, sep='\t')
    _ = num_walls(4); print(_==63, 'num_walls(4) ', _, sep='\t')
    _ = num_walls(5); print(_==94, 'num_walls(5) ', _, sep='\t')
    _ = num_walls(6); print(_==131, 'num_walls(6) ', _, sep='\t')
    _ = num_walls(7); print(_==174, 'num_walls(7) ', _, sep='\t')
    _ = num_walls(8); print(_==223, 'num_walls(8) ', _, sep='\t')
    _ = num_walls(9); print(_==278, 'num_walls(9) ', _, sep='\t')
    _ = num_walls(10); print(_==339, 'num_walls(10) ', _, sep='\t')
    _ = num_walls(11); print(_==406, 'num_walls(11) ', _, sep='\t')
    _ = num_walls(12); print(_==479, 'num_walls(12) ', _, sep='\t')
    _ = num_walls(13); print(_==558, 'num_walls(13) ', _, sep='\t')
    _ = num_walls(14); print(_==643, 'num_walls(14) ', _, sep='\t')
    _ = num_walls(15); print(_==734, 'num_walls(15) ', _, sep='\t')
    _ = num_walls(16); print(_==831, 'num_walls(16) ', _, sep='\t')
    _ = num_walls(17); print(_==934, 'num_walls(17) ', _, sep='\t')
    _ = num_walls(18); print(_==1043, 'num_walls(18) ', _, sep='\t')
    _ = num_walls(19); print(_==1158, 'num_walls(19) ', _, sep='\t')
    _ = num_walls(20); print(_==1279, 'num_walls(20) ', _, sep='\t')

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

def num_days(start_date, end_date):
    ''' Returns the number of days from start_date until end_date '''
    import datetime
    date_format = "%Y-%m-%d"
    start = datetime.datetime.strptime(start_date, date_format)
    end = datetime.datetime.strptime(end_date, date_format)
    return (end - start).days

###############
# Question 2a #
###############

def num_subscribers(filename, event, resource):
    data = read_csv(filename)[1:]
    data = list(filter(lambda r: r[0] == event, data))
    data = list(filter(lambda r: r[1] == resource, data))
    user_ids = {}
    for event, resource, user_id, date, time in data:
        user_ids[user_id] = 1
    return len(user_ids)

def test_q2a():
    _ = num_subscribers('email_logs.csv','Comment','Final Review: Question 5',); print(_==4, "num_subscribers('email_logs.csv','Comment','Final Review: Question 5',)", _, sep='\t')
    _ = num_subscribers('email_logs.csv','Announcement','Desparado Remedial for PE',); print(_==754, "num_subscribers('email_logs.csv','Announcement','Desparado Remedial for PE',)", _, sep='\t')
    _ = num_subscribers('email_logs.csv','Forum Reply','L11',); print(_==182, "num_subscribers('email_logs.csv','Forum Reply','L11',)", _, sep='\t')
    _ = num_subscribers('email_logs.csv','Forum Reply','M14',); print(_==36, "num_subscribers('email_logs.csv','Forum Reply','M14',)", _, sep='\t')
    _ = num_subscribers('email_logs.csv','Forum Reply','M15',); print(_==11, "num_subscribers('email_logs.csv','Forum Reply','M15',)", _, sep='\t')
    
# Uncomment to test question 2a
# test_q2a()

###############
# Question 2b #
###############

def top_k_avg_emails(filename, start_date, end_date, k):
    ''' Returns the top_k user_ids that have the
        largest average number of emails/day received
        between start_date and end_date inclusive, correct to 2 d.p.
    '''
    data = read_csv(filename)[1:]
    data = list(filter(lambda r: start_date <= r[3] <= end_date, data))
    days = num_days(start_date, end_date) + 1
    d = {}
    for event, resource, user_id, date, time in data:
        user_id = int(user_id)
        if user_id not in d:
            d[user_id] = 0
        d[user_id] += 1
    for user_id, num_emails in d.items():
        d[user_id] = round(num_emails / days, 2)
    results = sorted(d.items(), key=lambda p: p[1], reverse=True)
    if k > len(results):
        return results
    kth = results[k - 1][1]
    return list(filter(lambda p: p[1] >= kth, results))

def test_q2b():
    _ = top_k_avg_emails('email_logs.csv','2021-11-05','2021-11-05',2,); print(_==[(199368, 51.0), (903753, 51.0)], "top_k_avg_emails('email_logs.csv','2021-11-05','2021-11-05',2,)", _, sep='\t')
    _ = top_k_avg_emails('email_logs.csv','2021-11-06','2021-11-06',5,); print(_==[(527072, 45.0), (611569, 41.0), (983325, 39.0), (301261, 39.0), (199945, 38.0)], "top_k_avg_emails('email_logs.csv','2021-11-06','2021-11-06',5,)", _, sep='\t')
    _ = top_k_avg_emails('email_logs.csv','2021-11-05','2021-11-06',1,); print(_==[(527072, 44.0)], "top_k_avg_emails('email_logs.csv','2021-11-05','2021-11-06',1,)", _, sep='\t')
    _ = top_k_avg_emails('email_logs.csv','2021-11-05','2021-11-07',2,); print(_==[(527072, 41.67), (199368, 40.33)], "top_k_avg_emails('email_logs.csv','2021-11-05','2021-11-07',2,)", _, sep='\t')
    _ = top_k_avg_emails('email_logs.csv','2021-11-05','2021-11-11',3,); print(_==[(527072, 21.86), (301261, 21.29), (983325, 20.71)], "top_k_avg_emails('email_logs.csv','2021-11-05','2021-11-11',3,)", _, sep='\t')

    
# Uncomment to test question 2b
test_q2b()

##############
# Question 3 #
##############

# Your answer here.
# Q3
class Player:
    def __init__(self, name):
        self.name = name
        self.game = None
        self.state = 'alive'
        self.voted = False

    def join(self, game):
        if self.state == 'dead':
            return f'{self.name} is dead'
        if self.state == 'home':
            return f'{self.name} has gone home'
        if self.game:
            return f'{self.name} is currently playing {self.game.name}'
        else:
            self.game = game
            game.players.append(self)
            return f'{self.name} is now playing {game.name}'

    def leave(self, reason):
        if not self.game:
            return f'{self.name} is not playing any game'        
        game = self.game
        game.players.remove(self)
        self.game = None
        game.count_votes()
        if reason == 'win':            
            return f'{self.name} has won {game.name}'
        elif reason == 'lose':
            self.state = 'dead'
            return f'Bang! {self.name} has lost {game.name}'
        elif self.voted:
            self.state = 'home'                    

    def vote(self):
        if not self.game:
            return f'{self.name} is not playing any game'
        self.voted = True
        self.game.count_votes()
        return f'{self.name} votes to stop'

class Game:
    def __init__(self, name):
        self.name = name
        self.players = []

    def count_votes(self):
        yes = len(tuple(filter(lambda p: p.voted, self.players)))
        no = len(self.players) - yes
        if yes > no:
            for player in self.players:
                player.leave('vote')

def test_q3():
    darren = Player('Darren')
    linus = Player('Linus')
    matthew = Player('Matthew')
    nigel = Player('Nigel')
    russell = Player('Russell')
    sean = Player('Sean')
    terry = Player('Terry')
    zero_point = Game('Zero Point')
    pepsi_cola = Game('Pepsi Cola 1-2-3')
    _=darren.join(zero_point); print(_ == 'Darren is now playing Zero Point', "\tdarren.join(zero_point)  \t", repr(_))
    _=darren.join(pepsi_cola); print(_ == 'Darren is currently playing Zero Point', "\tdarren.join(pepsi_cola)  \t", repr(_))
    _=linus.join(zero_point); print(_ == 'Linus is now playing Zero Point', "\tlinus.join(zero_point)   \t", repr(_))
    _=matthew.join(zero_point); print(_ == 'Matthew is now playing Zero Point', "\tmatthew.join(zero_point) \t", repr(_))
    _=nigel.join(zero_point); print(_ == 'Nigel is now playing Zero Point', "\tnigel.join(zero_point)   \t", repr(_))
    _=russell.join(zero_point) ; print(_ == 'Russell is now playing Zero Point', "\trussell.join(zero_point) \t", repr(_))
    _=darren.vote()  ; print(_ == 'Darren votes to stop', "\tdarren.vote()            \t", repr(_))
    _=linus.vote()   ; print(_ == 'Linus votes to stop', "\tlinus.vote()             \t", repr(_))
    _=linus.vote()   ; print(_ == 'Linus votes to stop', "\tlinus.vote()             \t", repr(_))
    _=sean.vote(); print(_ == 'Sean is not playing any game', "\tsean.vote()              \t", repr(_))
    _=sean.leave('win'); print(_ == 'Sean is not playing any game', "\tsean.leave('win')        \t", repr(_))
    _=matthew.leave('lose')   ; print(_ == 'Bang! Matthew has lost Zero Point', "\tmatthew.leave('lose')    \t", repr(_))
    _=russell.leave('win')    ; print(_ == 'Russell has won Zero Point', "\trussell.leave('win')     \t", repr(_))
    _=darren.join(pepsi_cola); print(_ == 'Darren has gone home', "\tdarren.join(pepsi_cola)  \t", repr(_))
    _=linus.join(pepsi_cola); print(_ == 'Linus has gone home', "\tlinus.join(pepsi_cola)   \t", repr(_))
    _=matthew.join(pepsi_cola); print(_ == 'Matthew is dead', "\tmatthew.join(pepsi_cola) \t", repr(_))
    _=nigel.join(pepsi_cola); print(_ == 'Nigel is now playing Pepsi Cola 1-2-3', "\tnigel.join(pepsi_cola)   \t", repr(_))
    _=russell.join(pepsi_cola); print(_ == 'Russell is now playing Pepsi Cola 1-2-3', "\trussell.join(pepsi_cola) \t", repr(_))
    _=nigel.vote() ; print(_ == 'Nigel votes to stop', "\tnigel.vote()             \t", repr(_))
    _=sean.join(pepsi_cola); print(_ == 'Sean is now playing Pepsi Cola 1-2-3', "\tsean.join(pepsi_cola)    \t", repr(_))
    _=terry.join(pepsi_cola); print(_ == 'Terry is now playing Pepsi Cola 1-2-3', "\tterry.join(pepsi_cola)   \t", repr(_))
    _=sean.vote()  ; print(_ == 'Sean votes to stop', "\tsean.vote()              \t", repr(_))
    _=terry.vote() ; print(_ == 'Terry votes to stop', "\tterry.vote()             \t", repr(_))
    _=russell.vote() ; print(_ == 'Russell is not playing any game', "\trussell.vote()           \t", repr(_))
    jgp = Game('Ji Gu Pa')
    _=sean.join(jgp); print(_ == 'Sean has gone home', "\tsean.join(jgp)           \t", repr(_))
    _=terry.join(jgp); print(_ == 'Terry has gone home', "\tterry.join(jgp)          \t", repr(_))
    _=russell.join(jgp); print(_ == 'Russell is now playing Ji Gu Pa', "\trussell.join(jgp)        \t", repr(_))
    _=russell.leave('win'); print(_ == 'Russell has won Ji Gu Pa', "\trussell.leave('win')     \t", repr(_))

    
# Uncomment to test question 3
# test_q3()

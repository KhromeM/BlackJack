from random import shuffle


deck =[('9', 'spades'), ('3', 'hearts'), ('8', 'hearts'), ('4', 'clubs'), ('queen', 'clubs'), ('8', 'diamonds'), ('king', 'hearts'), ('7', 'spades'), ('10', 'spades'), ('king', 'spades'), ('4', 'diamonds'), ('ace', 'spades'), ('2', 'hearts'), ('9', 'clubs'), ('2', 'diamonds'), ('5', 'clubs'), ('king', 'clubs'), ('10', 'hearts'), ('4', 'hearts'), ('king', 'diamonds'), ('ace', 'diamonds'), ('ace', 'clubs'), ('6', 'clubs'), ('2', 'spades'), ('3', 'diamonds'), ('jack', 'diamonds'), ('8', 'clubs'), ('9', 'diamonds'), ('6', 'hearts'), ('3', 'spades'), ('7', 'hearts'), ('6', 'diamonds'), ('9', 'hearts'), ('5', 'spades'), ('6', 'spades'), ('ace', 'hearts'), ('7', 'clubs'), ('10', 'clubs'), ('jack', 'clubs'), ('2', 'clubs'), ('5', 'hearts'), ('jack', 'spades'), ('10', 'diamonds'), ('3', 'clubs'), ('queen', 'diamonds'), ('5', 'diamonds'), ('8', 'spades'), ('7', 'diamonds'), ('queen', 'spades'), ('queen', 'hearts'), ('jack', 'hearts'), ('4', 'spades')]
status =None
dealer = None
player = None
worth = {'ace':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'jack':10,'queen':10,'king':10}
player_worth = None
house_worth = None
b = 1
name = input("Enter your name: ")


class Player():
    balance = 1000
    def __init__(self,name):
        self.name = name

    def deal(self):
        global player_worth, status
        status = 1
        shuffle(deck)
        x = deck.pop()
        y = deck.pop()
        print(x)
        print(y)
        player_worth = worth[x[0]] + worth[y[0]]

    def bustchecker(self):
        global status
        if player_worth > 21:
            status = 0

    def hit(self):
        global player_worth
        x = deck.pop()
        print(x)
        player_worth += worth[x[0]]
        Player.bustchecker(self)

    def choose(self):
        p = input("Type 'stay' to stay, 'hit' to hit: ")
        if p.lower() == 'stay':
            return None
        else:
            Player.hit(self)
            if status == 0 :
                return None
            Player.choose(self)


class Dealer():

    def __init__(self):
        pass

    def deal(self):
        global house_worth
        x = deck.pop()
        y = deck.pop()
        print(x)
        print(y)
        house_worth = worth[x[0]] + worth[y[0]]

    def compare(self):
        if (player_worth > house_worth):
            player_wins()
        elif player_worth < house_worth:
            house_wins()
        else:
            tie_game()


def player_wins():
    global b
    player.balance += 200
    print(f"You won!")
    print(f"$200 has been added to your balance. Total balance: ${player.balance}. ")
    y = input(f"Play again? Yes or No: ")
    if y.lower() == 'no':
        b = 0
    else:
        b = 2


def house_wins():
    global b
    print(f"You lost")
    print(f"Your balance: ${player.balance} ")
    y = input(f"Play again? Yes or No: ")
    if y.lower() == 'no':
        b =0
    else:
        b = 2

def tie_game():
    global b
    player.balance += 100
    print(f"Tie game!")
    print(f"$100 has been returned to your balance. Total balance: ${player.balance}. ")
    y = input(f"Play again? Yes or No: ")
    if y.lower == 'no':
        b = 0
    else:
        b = 2

def game_start():
    player.balance -= 100
    print(f"$100 has been taken from your balance. Total balance: ${player.balance}.")

def clear(x):
    for n in range(x):
        print("                                                         ")


dealer = Dealer()
player = Player(name)

while True:
    b = 1
    clear(30)
    game_start()
    player.deal()
    clear(4)
    player.choose()
    if status == 0:
        print('You lost')
        house_wins()
    if b == 0:
        break
    if b == 2:
        continue
    clear(4)
    print('The house draws:')
    dealer.deal()
    clear(4)
    dealer.compare()
    if b == 0:
        break
    if b == 2:
        continue





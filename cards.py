#!/usr/local/bin/python3

#Defining the 'card' class
class card:

    def __init__(self, cardName):
        self.suit = cardName[len(cardName)-1].upper()
        self.title = cardName[:len(cardName)-1].upper()
    
        if self.title == 'J':
            self.rank = 11
        elif self.title == 'Q':
            self.rank = 12
        elif self.title == 'K':
            self.rank = 13
        elif self.title == 'A':
            self.rank = 14
        else:
            self.rank = int(self.title)


    def __str__(self):
        return str(self.title) + str(self.suit)


    def __repr__(self):
        return str(self.title) + str(self.suit)

#Defining various hand categories        
def StraightFlush(myHand):
    for Suit in myHand.cardsInHand:  
        if len(Suit) == 5:  #We are concerned with only THAT suit which contains 5 cards.
            for i in range(1, len(Suit)):  #sort the suit having the cards on the basis of rank
                tmp = Suit[i]
                k = i
                while k > 0 and tmp.rank < Suit[k-1].rank:
                    Suit[k] = Suit[k-1]
                    k -= 1
                Suit[k] = tmp
            for i in range(0, 4):   # Checking whether the ranks of the sorted cards are consecutive or not.
                if Suit[i].rank+1 != Suit[i+1].rank:
                   return False
            return True
    return False

def FourOfAKind(myHand):
    modifiedHand = []
    for Suit in myHand.cardsInHand:
        modifiedHand = modifiedHand + Suit

    for i in range(1, len(modifiedHand)): #Sorting the hand on the basis of ranks of the respective cards
        tmp = modifiedHand[i]
        k = i
        while k > 0 and tmp.rank < modifiedHand[k-1].rank:
            modifiedHand[k] = modifiedHand[k-1]
            k -= 1
        modifiedHand[k] = tmp

    ctr = 0
    for i in range(0, len(modifiedHand)-1):
        if modifiedHand[i].rank == modifiedHand[i+1].rank:
            while i < 4 and modifiedHand[i].rank == modifiedHand[i+1].rank:
                ctr += 1
                i += 1
            i -= 1
            if ctr == 3:
                return True
            else:
                ctr = 0
    return False

def FullHouse(myHand):
    modifiedHand = []
    for Suit in myHand.cardsInHand:
        modifiedHand = modifiedHand + Suit
    for i in range(1, len(modifiedHand)): #Sorting the hand on the basis of ranks of the respective cards
        tmp = modifiedHand[i]
        k = i
        while k > 0 and tmp.rank < modifiedHand[k-1].rank:
            modifiedHand[k] = modifiedHand[k-1]
            k -= 1
        modifiedHand[k] = tmp
    Variation = 0
    for i in range(0, len(modifiedHand)-1):
        if modifiedHand[i].rank != modifiedHand[i+1].rank:
            Variation += 1
    if Variation == 1:
        ctr = 0
        i = 0
        while modifiedHand[i].rank == modifiedHand[i+1].rank:
            ctr += 1
            i += 1
        if ctr == 1 or ctr == 2:
            return True
        else:
            return False
    else:
        return False

def ThreeOfAKind(myHand):
    modifiedHand = []
    for Suit in myHand.cardsInHand:
        modifiedHand = modifiedHand + Suit

    for i in range(1, len(modifiedHand)): #Sorting the hand on the basis of ranks of the respective cards
        tmp = modifiedHand[i]
        k = i
        while k > 0 and tmp.rank < modifiedHand[k-1].rank:
            modifiedHand[k] = modifiedHand[k-1]
            k -= 1
        modifiedHand[k] = tmp
    
    ctr = 1
    for i in range(0, len(modifiedHand)-1):
        if modifiedHand[i].rank == modifiedHand[i+1].rank:  #If the rank of one is equal to its next card...
            while i < 4 and modifiedHand[i].rank == modifiedHand[i+1].rank: #Run a loop as long from that card, as long as the ranks of all succeeding cards are equal
                ctr += 1 #Keep counting the number of cards with the equal ranks
                i += 1 #While adjusting i accordingly
            if ctr == 3:  #If the number of cards with equal rank is 3
                return True 
            else:
                ctr = 1 #Else, reset the value of the counter, for any pattern which could appear at a later stage
    return False #Program never encountered any set of three cards during the program run. This means that the the hand category is absent from this hand.
    
def Flush(myHand):
    for suit in myHand.cardsInHand:
        if len(suit) != 5 and len(suit) != 0: #There may either be 5 cards of one suit in a hand, or none
            return False
    return True

def Straight(myHand):
    modifiedHand = []
    for suit in myHand.cardsInHand:
        modifiedHand = modifiedHand + suit
    for i in range(1, len(modifiedHand)): #Sorting the hand on the basis of ranks of the respective cards
        tmp = modifiedHand[i]
        k = i
        while k > 0 and tmp.rank < modifiedHand[k-1].rank:
            modifiedHand[k] = modifiedHand[k-1]
            k -= 1
        modifiedHand[k] = tmp
    for i in range(0, len(modifiedHand)-1): #Rank of a card in the sorted hand must be one plus than it's predecessor
        if modifiedHand[i].rank + 1 != modifiedHand[i+1].rank:
            return False
    return True

def TwoPairs(myHand):
    modifiedHand = []
    for suit in myHand.cardsInHand:
        modifiedHand = modifiedHand + suit
    for i in range(1, len(modifiedHand)): #Sorting the hand on the basis of ranks of the respective cards
        tmp = modifiedHand[i]
        k = i
        while k > 0 and tmp.rank < modifiedHand[k-1].rank:
            modifiedHand[k] = modifiedHand[k-1]
            k -= 1
        modifiedHand[k] = tmp
    pairs = 0
    for i in range(0, 3):
        if i < 3 and modifiedHand[i].rank == modifiedHand[i+1].rank and modifiedHand[i].rank != modifiedHand[i+2].rank:
            pairs += 1
    if modifiedHand[4].rank == modifiedHand[3].rank and modifiedHand[3].rank != modifiedHand[2].rank:
        pairs += 1
    if pairs == 2:
        return True
    else:
        return False

def OnePair(myHand):
     modifiedHand = []
     for suit in myHand.cardsInHand:
         modifiedHand = modifiedHand + suit
     for i in range(1, len(modifiedHand)): #Sorting the hand on the basis of ranks of the respective cards
         tmp = modifiedHand[i]
         k = i
         while k > 0 and tmp.rank < modifiedHand[k-1].rank:
             #
             modifiedHand[k] = modifiedHand[k-1]
             k -= 1
         modifiedHand[k] = tmp
     pairs = 0
     for i in range(0, 3):
         if i < 3 and modifiedHand[i].rank == modifiedHand[i+1].rank and modifiedHand[i].rank != modifiedHand[i+2].rank:
             pairs += 1
     if modifiedHand[4].rank == modifiedHand[3].rank and modifiedHand[3].rank != modifiedHand[2].rank:
         pairs += 1
     if pairs == 1:
         return True
     else:
         return False
#End Hand categories defintion


def whichHand(S):
    if StraightFlush(S):
        return " a Straight Flush"
    elif FourOfAKind(S):
        return "Four of a kind"
    elif FullHouse(S):
        return "a Full House"
    elif Flush(S):
        return "a Flush"
    elif Straight(S):
        return "a Straight"
    elif ThreeOfAKind(S):
        return "Three of a kind"
    elif TwoPairs(S):
        return "Two pairs"
    elif OnePair(S):
        return "a pair"
    else:
        return "a high card"        


#Defining the 'hand' class
class hand:
    
    def __init__(self):
        self.cardsInHand = [[], [], [], []]

    def __repr__(self):
        return str(self.cardsInHand)

    def __str__(self):
        return str(self.cardsInHand)

    def addCard(self, cardList):
        for item in cardList:
            suits = {'D' : self.cardsInHand[0],
                     'C' : self.cardsInHand[1],
                     'S' : self.cardsInHand[2],
                     'H' : self.cardsInHand[3]}
            suits[card(item).suit].append(card(item))

    def clear(self):
        self.cardsInHand = [[], [], [], []]

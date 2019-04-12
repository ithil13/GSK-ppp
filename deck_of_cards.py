import random

class Card():
    def __init__(self, suit, rank, num):
        self.suit = suit
        self.rank = rank
        self.num_val = num
        self.face_up = False
    
    def turn_face_up(self):
        self.face_up = True

    def turn_face_down(self):
        self.face_up = False
        
    def __str__(self):
        if self.face_up:
            return "{}{}  ".format(self.suit, self.rank)
        else:
            return "[#] "


class Deck():
    def __init__(self):
        '''Creates a deck of 52 cards'''
        self.cards = []
        self.discards = []

        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for num in range(13):
            for char in "SHDC":
                self.cards.append(Card(char, ranks[num], num+1))

    def shuffle(self):
        random.shuffle(self.cards) 
    
    def deal(self):
        return self.cards.pop()

    def draw(self):
        if len(self.cards) == 0:
            self.cards = self.discards
            self.discards = []
            self.shuffle()
        card = self.deal()
        card.turn_face_up()
        self.discards.append(card)
        return self.discards[-1]
    
    def need_reshuffle(self):
        if len(self.cards) == 0:
            return True
        return False

    def get_discard(self):
        if len(self.discards) > 0:
            return self.discards[-1]

    def remove_discard(self):
        self.discards.pop(-1)

    def __str__(self):
        if len(self.cards) > 0 and len(self.discards) > 0:
            return "Deck: [#]  Discards: " + str(self.discards[-1])
        elif len(self.cards) > 0 and len(self.discards) == 0:
            return "Deck: [#]  Discards empty"
        else:
            return "Deck empty  Discards: " + str(self.discards[-1])
import os
from queue import Queue
from deck_of_cards import Deck

class PyramidNode:
    def __init__(self, card=None, top_left=None, top_right=None):
        self.card = card
        self.top_left = top_left
        self.top_right = top_right
        self.low_left = None
        self.low_right = None
    
    def remove_card(self):
        self.card = "empty"

    def __str__(self):
        if self.card == "empty": 
            return "    "
        else:
            return str(self.card)

class Pyramid:
    def __init__(self):
        self.top = None
        self.available = []
        self.deck = Deck()
        self.deck.shuffle()
        self.shuffle_count = 3
        self.discards = PyramidNode()

    def deal(self):
        return self.deck.deal()
    
    def draw(self):
        if self.deck.need_reshuffle():
            self.shuffle_count -= 1
        self.discards.card = self.deck.draw()

    def deal_board(self):
        self.top = PyramidNode(self.deck.deal())
        Q = Queue()
        Q.push(self.top)
        for _ in range(21):
            current = Q.pop()
            # adding to the left edge of pyramid
            if current.top_left == None:
                current.low_left = PyramidNode(self.deck.deal(), top_right=current)
                Q.push(current.low_left)
            # connecting to the left
            else:
                current.low_left = current.top_left.low_left.low_right
                current.low_left.top_right = current
            # adding to the right
            current.low_right = PyramidNode(self.deck.deal(), top_left=current)
            Q.push(current.low_right)
        # bottom row
        while Q.is_empty() == False:
            current = Q.pop()
            current.card.turn_face_up()
            self.available.append(current)
    
    def remove_card(self, node):
        if node == self.discards:
            self.deck.remove_discard()
            self.discards = PyramidNode(self.deck.get_discard())
        else:
            node.remove_card()
            self.available.remove(node)
            # check if card at top_left is free
            if node.top_left != None and node.top_left.low_left.card == "empty":
                self.available.append(node.top_left)
                node.top_left.card.turn_face_up()
            # check if card at top_right is free
            if node.top_right != None and node.top_right.low_right.card == "empty":
                self.available.append(node.top_right)
                node.top_right.card.turn_face_up()

    def __str__(self):
        if self.game_won():
            return "YOU'VE WON!"
        if self.game_lost():
            return "GAME OVER!"
        return_str = " " * 12
        Q = Queue()
        Q.push(self.top)  
        indent = 10
        while Q.is_empty() == False:
            current = Q.pop()
            if current.low_left != None:
                # adding child cards to queue
                if current.top_left == None:
                    Q.push(current.low_left)
                Q.push(current.low_right)
            return_str += str(current)
            # end of row
            if current.top_right == None:
                return_str += "\n" + (" " * indent)
                indent -= 2
        return return_str

    def search_board(self, in_val):
        for node in self.available:
            if in_val.upper() == str(node).strip():
                return node
    
    def get_discard(self):
        return str(self.discards).strip()
    
    def game_over(self):
        if self.game_lost() or self.game_won():
            return True
        return False

    def game_won(self):
        if self.top.card == "empty":
            return True
        return False

    # set game over conditions
    def game_lost(self):
        if self.shuffle_count == 0:
            return True
        return False

def play_game():
    board = Pyramid()
    board.deal_board()
    print_game(board)
    while not board.game_over():
        c1 = input("Select a card: ")
        if c1.upper() == "D":
            board.draw()
        else:
            card1 = validate_input(board, c1)
            if card1 != None:
                if card1.card.num_val == 13:
                    board.remove_card(card1)
                else:
                    c2 = input("Select card 2: ")
                    card2 = validate_input(board, c2)
                    if card2 != None:
                        if card1.card.num_val + card2.card.num_val == 13:
                            board.remove_card(card1)
                            board.remove_card(card2)
        print_game(board)

def print_game(board):
    os.system("cls")
    print(board)
    if not board.game_over():
        print(board.deck)
        print()
        print("Write 'D' to draw from the deck")

def validate_input(board, in_val):
    if in_val.upper() == board.get_discard():
        return board.discards
    return board.search_board(in_val)

if __name__ == "__main__":
    play = "y"
    while play.lower() == "y":
        play_game()
        play = input("Play again? (Y/N) ")


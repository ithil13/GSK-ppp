This is a simple game of pyramid solitaire, where you can remove a pair of 
cards from the board if their combined value is 13. Since the king has a 
value of 13 by itself it does not need to be a part of a pair. The game 
ends when the board is clear or the deck has been emptied 3 times.

To make the game I have used the following classes:
Card and Deck,
Queue and Node,
Pyramid and PyramidNode

Card and Deck are used to initialize the deck of cards and have methods for
drawing and shuffling the deck and turning cards face up or face down.

Initializing the gameboard and printing it is done row by row from the top of 
the board and this is what I've used the Queue for.

The Pyramid classes are used for the gameboard and the methods needed to play. 
Each node is connected to two parent nodes and two child nodes and they share a child 
node with the node next to it. 

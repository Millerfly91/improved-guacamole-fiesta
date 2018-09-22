import random
from BoardGame.Board import Board


class GamePlay2:

    board = None
    board2 = None

    def setupBoard(self):
        boardbounds = input('What size board would you like to play?'
                            "'enter' for default board."
                            ' (i.e. 4x5 , 10x10, 25x50) ')
        if boardbounds == "":
            length = 10
            width = 10
        else:
            bound = boardbounds.split('x')
            length = int(bound[0])
            width = int(bound[1])

        self.board = Board(length, width)

        boardbounds2 = input('What size board2 would you like to play?'
                            "'enter' for default board."
                            ' (i.e. 4x5 , 10x10, 25x50) ')
        if boardbounds2 == "":
            length = 10
            width = 10
        else:
            bound = boardbounds2.split('x')
            length = int(bound[0])
            width = int(bound[1])

        self.board2 = Board(length, width)

        self.board.print_board()
        self.board2.print_board()

    # def setupPlayers(self):



test = GamePlay2()
test.setupBoard()
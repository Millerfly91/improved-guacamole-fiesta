import random
import re
from BoardGame.Board import Board
from BoardGame.Base_character import baseCharacter


class GamePlay2:

    board = None

    def setupBoard(self):
        boardbounds = input('What size board would you like to play?'
                            "\n'enter' for default board."
                            '\n(i.e. 4x5 , 10x10, 25x50) ')
        if boardbounds == "":
            length = 10
            width = 10
        else:
            bound = boardbounds.split('x')
            length = int(bound[0])
            width = int(bound[1])

        self.board = Board(length, width)
        self.board.print_board()

    def initializeCharacter(self, thisplayer):
        player = baseCharacter()
        player.token = input("What token would {} like to be? ".format(thisplayer))
        position = self.randomBoardPosition()
        player.charlocation = position
        player.charname = thisplayer
        player.health = 10
        player.defence = 10
        player.speed = 3
        return player

    def setupCharacters(self):
        chardict = {}
        player = 1
        players = input('\nEnter the names of the people playing, '
                        'separated by a comma. ')
        playernames = players.split(',')

        for thisplayer in playernames:
            newchar = self.initializeCharacter(thisplayer)
            newchar.player = player
            chardict.__setitem__('Player'+str(player), newchar)
            player += 1
            self.placeCharacter(newchar)

        self.printCharacters(chardict)

    def printCharacters(self, chardict):
        charlist = list(chardict.keys())

        for name in charlist:
            print(chardict.get(name))

    def placeCharacter(self, player):
        row = player.charlocation[0]
        column = player.charlocation[1]
        token = player.token
        print(row, column)
        self.board.set_value(token, row, column)

    def randomBoardPosition(self):
        row = random.randint(0, self.board.get_total_rows() - 1)
        column = random.randint(0, self.board.get_total_columns() - 1)
        return row, column

    def placeTarget(self):
        targettoken = '$'
        position = self.randomBoardPosition()
        self.board.set_value(targettoken, position[0], position[1])

    def setupGame(self):
        self.setupBoard()
        self.setupCharacters()
        self.placeTarget()
        self.board.print_board()

    def characterMovement(self):
        roll = random.randint(1, 6)
        directional = input("You have rolled a {}."
                            "\n How would you like to use your turn?"
                            "\n (ex. Up 2, Left 1)".format(roll))
        self.validateMove(roll, directional)
        moves = directional.split(', ')
        # totalmoves = sum(moves)

        print(moves)

    def validateMove(self, roll, movement):
        steps = re.findall(r'\d+', movement)
        stepcount = 0
        for num in stepslist:
            stepcount += int(num)
        if stepcount != roll:
            raise ValueError('Movement is not equal to dice roll. Re evaluate your move.'
                             'Your roll was {}.'.format(roll))

    def playGame(self):
        self.characterMovement()

test = GamePlay2()
test.setupGame()
test.playGame()
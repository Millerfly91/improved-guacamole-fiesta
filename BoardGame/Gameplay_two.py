import random
import re
from BoardGame.Board import Board
from BoardGame.Base_character import baseCharacter


class GamePlay2:

    board = None
    chardict = {}
    targetlocation = ()
    charactertokens = []

    def setupboard(self):
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
        # self.board.print_board()

    def initializecharacter(self, thisplayer):
        player = baseCharacter()
        player.token = input("What token would {} like to be? ".format(thisplayer))
        position = self.randomboardposition()
        player.charlocation = position
        player.charname = thisplayer
        player.health = 10
        player.defence = 10
        player.speed = 3
        self.charactertokens.append(player.token)
        return player

    def setupcharacters(self):
        player = 1
        players = input('\nEnter the names of the people playing, '
                        'separated by a comma. ')
        playernames = players.split(',')

        for thisplayer in playernames:
            newchar = self.initializecharacter(thisplayer)
            newchar.player = player
            self.chardict.__setitem__('Player'+str(player), newchar)
            player += 1
            self.placecharacter(newchar)
            # print('chardict = ', list(self.chardict))

        self.printcharacterstats()

    def printcharacterstats(self):
        charlist = self.chardict.values()

        for name in charlist:
            print(self.chardict.get(name))

    def placecharacter(self, player):
        row = player.charlocation[0]
        column = player.charlocation[1]
        token = player.token
        self.board.set_value(token, row, column)
        # self.characterlocations.append(player.charlocation)

    def randomboardposition(self):
        row = random.randint(0, self.board.get_total_rows() - 1)
        column = random.randint(0, self.board.get_total_columns() - 1)
        return row, column

    def placetarget(self):
        targettoken = '$'
        position = self.randomboardposition()
        self.board.set_value(targettoken, position[0], position[1])
        self.targetlocation = position

    def setupgame(self):
        self.setupboard()
        self.setupcharacters()
        self.placetarget()
        self.board.print_board()

    def charactermovement(self, player):
        charname = self.chardict.get(player).charname
        charlocation = self.chardict.get(player).charlocation
        roll = random.randint(1, 6)
        directional = input("\n{} is at {} and has rolled a {}."
                            "\nHow would you like to use your turn?" 
                            "\n (ex. Up 2, Left 1) ".format(charname, charlocation, roll))
        self.validatemove(roll, directional)
        movesets = directional.split(', ')
        print('movesets = ', movesets)
        for singlemove in movesets:
            self.removeoldtoken(player)
            self.tokenmovement(singlemove, player)

    def removeoldtoken(self, player):
        # resets the characters previous token location
        currenttoken = self.chardict.get(player).charlocation
        row = int(currenttoken[0])
        column = int(currenttoken[1])
        self.board.set_value('0', row, column)

    def tokenmovement(self, moves, player):
        location = self.chardict.get(player).charlocation
        charlocation = list(location)
        token = self.chardict.get(player).token
        row = int(charlocation[0])
        column = int(charlocation[1])
        move = moves.split(' ')
        steps = int(move[1])
        print(row, column)

        if 'left' in move[0]:
            column = column - steps
        elif 'right' in move[0]:
            column = column + steps
        elif 'up' in move[0]:
            row = row - steps
        elif 'down' in move[0]:
            row = row + steps

        self.board.set_value(token, row, column)
        # charlocation[0] = row
        # charlocation[1] = column
        self.chardict.get(player).charlocation = row, column


    def validatemove(self, roll, movement):
        steps = re.findall(r'\d+', movement)
        stepcount = 0
        for num in steps:
            stepcount += int(num)
        if stepcount != roll:
            raise ValueError('Movement is not equal to dice roll. Re evaluate your move.'
                             'Your roll was {}.'.format(roll))

    def playgame(self):
        charlocations = []

        for player in self.chardict:
            charlocation = self.chardict.get(player).charlocation
            charlocations.append(charlocation)
        print(charlocations)

        while not charlocations.__contains__(self.targetlocation):
            for player in self.chardict:
                self.charactermovement(player)

            self.board.print_board()


test = GamePlay2()
test.setupgame()
test.playgame()

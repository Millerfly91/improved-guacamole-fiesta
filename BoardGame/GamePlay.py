import random
import re
from BoardGame import Board


def dice_roll(num1, num2):
    return random.randint(1, 6)


class GamePlay:

    board = Board.Board()
    characters = {}
    targetlocation = ()

    def movement(self, charname):
        diceroll = dice_roll(1, 6)
        mymove = input("You rolled a {}. How would you like to move? (ex. Rolled a 5. Up 2, Left 3.) ".format(diceroll))
        rawgo = mymove.split(',')
        for directional in rawgo:
            direction = directional.split(' ')
            print('direction is: ', direction)
            print('directional is: ', directional)
            self.moveCharDirection(directional, charname)
        #     pass direction to moveCharDirection

    def moveCharDirection(self, directional, charname):
        chartoken = self.characters.get(charname)[0]
        charlocation = self.characters.get(charname)[1]
        column = int(charlocation[0])
        row = int(charlocation[1])

        chardirection = directional.strip().split(' ')
        charsteps = int(chardirection[1])

        if 'left' in chardirection[0]:
            self.board.set_value(chartoken, row, column - charsteps)
        elif 'right' in chardirection[0]:
            self.board.set_value(chartoken, row, column + charsteps)
        elif 'up' in chardirection[0]:
            self.board.set_value(chartoken, row - charsteps, column)
        elif 'down' in chardirection[0]:
            self.board.set_value(chartoken, row + charsteps, column)

        self.board.set_value('O', row, column)
        self.board.print_board()


    def start_game(self):
        targetsymbol = '@'
        targetx = random.randint(1, 9)
        targety = random.randint(1, 9)
        self.targetlocation = (targetx, targety)
        # targetinfor = {targetsymbol, self.targetlocation}
        # create a dict to hold players
        playernames = input('Enter the names of the people playing, separated by a comma. ')
        # create a list of players from input
        players = playernames.split(',')
        # for every name in the list created, ask for a symbol and assign that player name to a key pair in a
        # dictionary with the symbol as the value
        for thisplayer in players:
            symbol = input('What character would {} like to be? '.format(thisplayer))
            xval = random.randint(1, 10)
            yval = random.randint(1, 9)
            self.board.set_value(symbol, yval, xval)
            locations = (xval, yval)
            self.characters.__setitem__(thisplayer, [symbol, locations])
        # set the target in a random location on the board
        self.board.set_value(targetsymbol, targety, targetx)
        self.board.print_board()

        print('characters are: ', self.characters)

    def play_game(self):
        print('target location is: ', self.targetlocation)
        # for key in self.characters.keys():
        self.movement(input('Enter name: '))


if __name__ == "__main__":
    test = GamePlay()
    test.start_game()
    test.play_game()

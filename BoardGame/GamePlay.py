import random
from BoardGame import Board


def dice_roll(num1, num2):
    return random.randint(1, 6)


class GamePlay:

    board = Board.Board()
    characters = {}
    targetlocation = ()

    # def movement(self):
    #     steps = dice_roll(1, 6)
    #     direction = input("How would you like to move? (ex. Rolled a 5. Up 2, Left 3.")
    #     go = direction.split(',')
    #     while moved < steps:
    #         if direction == 'up'
    #     print(steps)

    def start_game(self):

        targetsymbol = '@'
        targetx = random.randint(1, 10)
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
            self.board.set_value(symbol, xval, yval)
            locations = (xval, yval)
            self.characters.__setitem__(thisplayer, [symbol, locations])
        # set the target in a random location on the board
        self.board.set_value(targetsymbol, targetx, targety)
        self.board.print_board()

        print(self.characters)

    def play_game(self):
        print(self.targetlocation)
       # for key in self.characters.keys():

            # if self.characters.__getitem__(key)[1] == :
            #     print('You WIN!!!')



if __name__ == "__main__":
    test = GamePlay()
    test.start_game()
    test.play_game()
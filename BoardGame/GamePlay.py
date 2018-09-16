import random
from BoardGame import Board


def dice_roll(num1, num2):
    return random.randint(1, 6)

class GamePlay:

    board = Board.Board()
    board.printBoard()

    # def movement(self):
    #     steps = dice_roll(1, 6)
    #     direction = input("How would you like to move? (ex. Rolled a 5. Up 2, Left 3.")
    #     go = direction.split(',')
    #     while moved < steps:
    #         if direction == 'up'
    #     print(steps)

    def startlocation(self):
        self.board.setValue('player', 0, 0)
        self.board.printBoard()



if __name__ == "__main__":
    test = GamePlay()
    test.startlocation()
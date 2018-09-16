class Board:
    board = [
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"]
    ]

    def print_board(self):
        print("--------------------------BOARD------------------------")
        for row in self.board:
            print(row)

    def set_value(self, token, row, column):
        self.board[row][column] = token


if __name__ == "__main__":
    myBoard = Board()
    myBoard.printBoard()

    inVal = input("What character would you like to set this value to? ")
    myBoard.setValue(inVal, 5, 7)
    myBoard.printBoard()

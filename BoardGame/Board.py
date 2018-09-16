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

    def printBoard(self):
        for row in self.board:
            print(row)

    def setValue(self, token, row, column):
        self.board[row][column] = token

if __name__ == "__main__":
    myBoard = Board()
    myBoard.printBoard()

class Board:
    board = None
    rows_total = -1
    columns_total = -1

    def __init__(self, rows, columns):
        self.rows_total = rows
        self.columns_total = columns
        self.board = self.creatSetSizeBoard(rows, columns)

    def creatSetSizeBoard(self, rows, columns):
        newBoard = []
        columnCounter = 0
        while columnCounter < columns:
            newBoard
            newRow = []
            rowCounter = 0
            while rowCounter < rows:
                newRow.append('0')
                rowCounter += 1
            newBoard.append(newRow)
            columnCounter += 1
        return newBoard

    def print_board(self):
        print("--------------------------BOARD------------------------")
        for row in self.board:
            print(row)

    # Puts token at row row and column column.
    def set_value(self, token, row, column):
        self.board[row][column] = token

    def get_total_rows(self):
        return self.rows_total

    def get_total_columns(self):
        return self.columns_total


if __name__ == "__main__":
    myBoard = Board(100, 100)
    myBoard.print_board()

    inVal = input("What character would you like to set this value to? ")
    myBoard.setValue(inVal, 5, 7)
    myBoard.print_board()



# naive implementation


class TicTacToe:

    def __init__(self, n: int):
        self.board = [[None] * n for _ in range(n)]

        self.players = {
            1: 'X',
            2: 'O'
        }
        self.n = n

        # print(self.board)

    # player 1, or 2

    def move(self, row: int, col: int, player: int) -> int:
        symbo = self.players[player]
        self.board[row][col] = symbo

        # check row

        # win 0 or i
        # win = 0

        row_win = sum([1 for j in range(self.n)
                      if self.board[row][j] == symbo])

        if row_win == self.n:
            return player

        col_win = sum([1 for i in range(self.n)
                      if self.board[i][col] == symbo])

        if col_win == self.n:
            return player

        if row == col:
            dia_win = sum([1 for k in range(self.n)
                          if self.board[k][k] == symbo])
            if dia_win == self.n:
                return player

        if row == self.n - 1 - col:
            anti_dia_win = sum(
                [1 for i in range(self.n) if self.board[i][self.n - 1 - i] == symbo])

            if anti_dia_win == self.n:
                return player

        return 0

# own yass!!

# o (n)  2n (rows + cols) + 2   diagonal anti-diagonal


class TicTacToe:

    def __init__(self, n: int):
        self.n = n

        # player 1,  + 1
        # player 2,  - 1
        # check abs value

        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:

        val = 1 if player == 1 else -1

        # row
        self.rows[row] += val

        # col
        self.cols[col] += val

        if row == col:
            self.diagonal += val

        if row == self.n - col - 1:
            self.anti_diagonal += val

        # check status

        if abs(self.rows[row]) == self.n or abs(self.cols[col] == self.n or abs(self.diagonal)) == self.n or abs(self.anti_diagonal) == self.n:
            return player

        return 0


tic = TicTacToe(2)

tic.move(0, 0, 2)
tic.move(0, 1, 1)
print(tic.move(1, 1, 2))

# print(tic.board)

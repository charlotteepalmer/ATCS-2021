# Sliding Puzzle Game
# ATCS Final Project
# Charlotte Palmer
# 4/25/22

import sys

# Modified TicTacToe code
def perfect_board():
    perfect = []
    row1 = [1, 2, 3]
    row2 = [4, 5, 6]
    row3 = [7, 8, 0]
    perfect.append(row1)
    perfect.append(row2)
    perfect.append(row3)
    return perfect

class SlidingPuzzle:

    # Set up the board
    def __init__(self):
        self.board = perfect_board()

    # Find the position of the 0 (blank space) on the board
    def find_0(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)
        sys.exit("Error: there is no 0 on the board.")

    # Determine if the move is valid
    def is_valid_move(self, move):
        i, j = self.find_0()
        if move == 'u' and j == 0:
            return False
        if move == 'd' and j == 2:
            return False
        if move == 'l' and i == 0:
            return False
        if move == 'r' and i == 2:
            return False
        return True

    def make_move(self, move):
        i, j = self.find_0()
        if self.is_valid_move(move):
            if move == 'u':
                self.board[i][j] = self.board[i - 1][j]
                self.board[i - 1][j] = 0
            if move == 'd':
                self.board[i][j] = self.board[i + 1][j]
                self.board[i + 1][j] = 0
            if move == 'l':
                self.board[i][j] = self.board[i][j - 1]
                self.board[i][j - 1] = 0
            if move == 'r':
                self.board[i][j] = self.board[i][j + 1]
                self.board[i][j + 1] = 0
            return True
        return False

    def is_game_over(self):
        if self.board == perfect_board():
            return True
        return False


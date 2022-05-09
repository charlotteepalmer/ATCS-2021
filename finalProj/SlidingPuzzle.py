# Sliding Puzzle Game
# ATCS Final Project
# Charlotte Palmer
# 4/25/22
# Showing improvement from Data Science final project
# by creating functions instead of repeating code.

import sys
import random
from UI import *

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

    # Sets up the board
    def __init__(self):
        self.board = perfect_board()
        self.shuffle()
        print_board(self)
        self.explored = []

    # Finds the position of the 0 (blank space) on the board
    def find_0(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)
        sys.exit("Error: there is no 0 on the board.")

    # Determines if the move is valid
    def is_valid_move(self, move):
        i, j = self.find_0()
        if move == 'u' and i == 0:
            return False
        if move == 'd' and i == 2:
            return False
        if move == 'l' and j == 0:
            return False
        if move == 'r' and j == 2:
            return False
        return True

    # Moves the zero (the space) up, down, left, or right
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

    # Determines if the game is over
    def is_game_over(self):
        if self.board == perfect_board():
            return True
        return False

    # Randomly shuffles the board
    def shuffle(self):
        moves_list = ['u', 'd', 'l', 'r']
        for i in range(40):
            self.make_move(random.choice(moves_list))

    # Tried to used breadth first search, but it didn't work
    def bfs(self, current_path, current_board):
        if current_board == perfect_board():
            return current_path
        for move in ['u', 'd', 'l', 'r']:
            if self.is_valid_move():
                board_copy = current_board
                board_copy.make_move(move)
                if board_copy not in self.explored:
                    path_copy = current_path
                    path_copy.append(move)
                    solution = self.bfs(path_copy, board_copy)
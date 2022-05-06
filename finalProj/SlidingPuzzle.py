# Sliding Puzzle Game
# ATCS Final Project
# Charlotte Palmer
# 4/25/22

import sys
import random
from UI import *
from copy import deepcopy

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
        self.shuffle()
        print_board(self)
        self.explored = []

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
        if move == 'u' and i == 0:
            return False
        if move == 'd' and i == 2:
            return False
        if move == 'l' and j == 0:
            return False
        if move == 'r' and j == 2:
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

    def shuffle(self):
        moves_list = ['u', 'd', 'l', 'r']
        for i in range(40):
            self.make_move(random.choice(moves_list))

    def bfs(self, path, current):
        queue = []
        explored = []
        while queue:
            current = queue.pop(0)
            if current == perfect_board():
                return current
            for move in ['u', 'd', 'l', 'r']:
                if self.is_valid_move():
                    board_copy = current
                    board_copy.make_move(move)
                    if board_copy not in explored:
                        queue.append(board_copy)
                        explored.append(board_copy)

from SlidingPuzzle import *
from UI import *

board = SlidingPuzzleBoard()
board.array = perfect_board()
board.shuffle()
board.print_board()

solution = dfs([], board, 0)

if solution:
    print("The solution is:", solution)
    board.print_board()
    for move in solution:


# Testing methods
# print(game.find_0())
# print(game.is_valid_move('down'))
# print_board(game)
# game.make_move('u')
# print_board(game)
# print(board.is_game_over())
from SlidingPuzzle import *
from UI import *

board = SlidingPuzzleBoard()
board.array = perfect_board()
board.shuffle()
board.print_board()

solution = dfs([], board, 0)

if solution:
    print("I solved the SlidingPuzzle! The solution is:", solution)
    board.print_board()
    for move in solution:
        print("The move was: " + move)
        board.make_move(move)
        board.print_board()
else:
    print("Unable to solve this SlidingPuzzle. Please try another.")

# Testing methods
# print(game.find_0())
# print(game.is_valid_move('down'))
# print_board(game)
# game.make_move('u')
# print_board(game)
# print(board.is_game_over())
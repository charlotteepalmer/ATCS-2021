from SlidingPuzzle import *
from UI import *

game = SlidingPuzzle()
print(game.find_0())
print(game.is_valid_move('down'))
print_board(game)
game.make_move('d')
print_board(game)
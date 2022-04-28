
# Print the game instructions
def print_instructions():
    print("Welcome to SlidingPuzzle!")
    print("Watch the AI race to finish the game!")

# Print the board (used TicTacToe code)
def print_board(game):
    for i in range(3):
        for j in range(3):
            print(game.board[i][j], end="\t")
        print()
    print()

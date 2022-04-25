
# Prints the game instructions
def print_instructions(self):
    print("Welcome to SlidingPuzzle!")
    print("Watch the AI race to finish the game!")

# Prints the board (used TicTacToe code)
def print_board(self):
    print("\t" + str(0) + "\t" + str(1) + "\t" + str(2))
    for i in range(3):
        print(str(i) + "\t" + self.board[i][0] + "\t" + self.board[i][1] + "\t" + self.board[i][2])
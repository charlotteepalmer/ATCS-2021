import random
import time

class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        self.board = []
        row1 = ['-', '-', '-']
        row2 = ['-', '-', '-']
        row3 = ['-', '-', '-']
        self.board.append(row1)
        self.board.append(row2)
        self.board.append(row3)

    def print_instructions(self):
        # TODO: Print the instructions to the game
        print("Welcome to TicTacToe!")
        print("Player 1 is X and Player 2 is O")
        print("Take turns placing your piece - the first to 3 in a row wins!")

    def print_board(self):
        # TODO: Print the board
        print("\t" + str(0) + "\t" + str(1) + "\t" + str(2))
        for i in range(3):
            print(str(i) + "\t" + self.board[i][0] + "\t" + self.board[i][1] + "\t" + self.board[i][2])

    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid
        if row >= 0 and row <= 2 and col >= 0 and col <= 2:
            if self.board[row][col] == '-':
                return True
        return False

    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        #if self.is_valid_move(row, col):
        self.board[row][col] = player

    def minimax(self, player, depth):
        #self.print_board()
        #print()

        if self.check_win("O"):
            #print("win O")
            return (10, None, None)
        if self.check_tie():
            #print("tie")
            return (0, None, None)
        if self.check_win("X"):
            #print("win X")
            return (-10, None, None)
        if depth == 0:
            return (0, None, None)

        if player == "O":
            best = -100
            opt_row = -1
            opt_col = -1
            for row in range(3):
                for col in range(3):
                    if self.is_valid_move(row, col):
                        self.place_player("O", row, col)
                        score = self.minimax("X", depth - 1)[0]
                        if best < score:
                            best = score
                            opt_row = row
                            opt_col = col
                        self.place_player("-", row, col)

            return (best, opt_row, opt_col)

        if player == "X":
            worst = 100
            opt_row = -1
            opt_col = -1
            for row in range(3):
                for col in range(3):
                    if self.is_valid_move(row, col):
                        self.place_player("X", row, col)
                        score = self.minimax("O", depth - 1)[0]
                        if worst > score:
                            worst = score
                            opt_row = row
                            opt_col = col
                        self.place_player("-", row, col)

            return (worst, opt_row, opt_col)

    def minimax_alpha_beta(self, player, depth, alpha, beta):

        if self.check_win("O"):
            #print("win O")
            return (10, None, None)
        if self.check_tie():
            #print("tie")
            return (0, None, None)
        if self.check_win("X"):
            #print("win X")
            return (-10, None, None)
        if depth == 0:
            return (0, None, None)

        if player == "O":
            best = -100
            opt_row = -1
            opt_col = -1
            for row in range(3):
                for col in range(3):
                    if self.is_valid_move(row, col):
                        self.place_player("O", row, col)
                        score = self.minimax_alpha_beta("X", depth - 1, alpha, beta)[0]
                        self.place_player("-", row, col)
                        if best < score:
                            best = score
                            if best > alpha:
                                alpha = best
                            opt_row = row
                            opt_col = col
                            if beta <= alpha:
                                return (best, opt_row, opt_col)
            return (best, opt_row, opt_col)

        if player == "X":
            worst = 100
            opt_row = -1
            opt_col = -1
            for row in range(3):
                for col in range(3):
                    if self.is_valid_move(row, col):
                        self.place_player("X", row, col)
                        score = self.minimax_alpha_beta("O", depth - 1, alpha, beta)[0]
                        self.place_player("-", row, col)
                        if worst > score:
                            worst = score
                            if worst < beta:
                                beta = worst
                            opt_row = row
                            opt_col = col
                            if beta <= alpha:
                                return (worst, opt_row, opt_col)
            return (worst, opt_row, opt_col)

    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot
        row = int(input("Enter a row: "))
        col = int(input("Enter a column: "))
        while self.is_valid_move(row, col) == False:
            print("Please enter a valid move.")
            row = int(input("Enter a row: "))
            col = int(input("Enter a column: "))
        self.place_player(player, row, col)

    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        print(player + "'s Turn")
        if player == 'X':
            self.take_manual_turn(player)
        if player == 'O':
            self.take_minimax_turn(player)

    def take_random_turn(self, player):
        x, y = -1, -1
        while not self.is_valid_move(x, y):
            x, y = random.randint(0, 3), random.randint(0, 3)
        self.board[x][y] = player

    def take_minimax_turn(self, player):
        depth = 100
        start = time.time()
        alpha = -1000
        beta = 1000
        # normal minimax
        # score, row, col = self.minimax(player, depth)
        # alpha beta minimax
        score, row, col = self.minimax_alpha_beta(player, depth, alpha, beta)
        end = time.time()
        print("This turn took:", end - start, "seconds")
        if self.is_valid_move(row, col):
            self.place_player(player, row, col)
        else:
            print("invalid move")
            exit()

    def check_col_win(self, player):
        # TODO: Check col win
        for col in range(3):
            if self.board[0][col] == player and self.board[1][col] == player and self.board[2][col] == player:
                return True
        return False

    def check_row_win(self, player):
        # TODO: Check row win
        for row in range(3):
            if self.board[row][0] == player and self.board[row][1] == player and self.board[row][2] == player:
                return True
        return False

    def check_diag_win(self, player):
        # TODO: Check diagonal win
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        elif self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True
        return False

    def check_win(self, player):
        # TODO: Check win
        if self.check_col_win(player) or self.check_row_win(player) or self.check_diag_win(player):
            return True
        return False

    def check_tie(self):
        # TODO: Check tie
        if self.check_win("X") or self.check_win("O"):
            return False
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "-":
                    return False
        return True

    def play_game(self):
        # TODO: Play game
        player = "X"
        self.print_instructions()
        self.print_board()
        while True:
            self.take_turn(player)
            self.print_board()
            if self.check_win("X"):
                print("X wins!")
                break
            if self.check_win("O"):
                print("O wins!")
                break
            if self.check_tie():
                print("It's a tie.")
                break
            if player == "X":
                player = "O"
            elif player == "O":
                player = "X"

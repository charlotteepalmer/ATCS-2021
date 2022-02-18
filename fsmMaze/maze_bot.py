"""
An AI that uses Finite State Machines to solve a maze

@author: Ms. Namasivayam (TODO: replace with your name)
@version: 2022
"""
from fsm import FSM


class MazeBot:
    def __init__(self, maze_file):
        # The location of the bot
        self.x = None
        self.y = None

        # The map of the maze
        self.maze = None

        # The route the bot will take to get to the $
        self.path = None

        # Create an initialize the maze
        self.reset(maze_file)

        # TODO: Create the Bot's finite state machine (self.fsm) with initial state
        self.fsm = FSM("NS")

        self.add_state_transitions()

    def add_state_transitions(self):
        """
        TODO: Implement add state transitions
        Adds all the state transitions to the fsm
        """
        self.fsm.add_transition('#', 'NN', next_state='NW')
        self.fsm.add_transition('#', 'NW', next_state='NS')
        self.fsm.add_transition('#', 'NS', next_state='NE')
        self.fsm.add_transition('#', 'NE', next_state='NN')

        self.fsm.add_transition('#', 'BN', next_state='BW')
        self.fsm.add_transition('#', 'BW', next_state='BS')
        self.fsm.add_transition('#', 'BS', next_state='BE')
        self.fsm.add_transition('#', 'BE', next_state='BN')

        self.fsm.add_transition('X', 'NN', next_state='NW')
        self.fsm.add_transition('X', 'NW', next_state='NS')
        self.fsm.add_transition('X', 'NS', next_state='NE')
        self.fsm.add_transition('X', 'NE', next_state='NN')

        self.fsm.add_transition('X', 'BN', self.move_north)
        self.fsm.add_transition('X', 'BE', self.move_east)
        self.fsm.add_transition('X', 'BS', self.move_south)
        self.fsm.add_transition('X', 'BW', self.move_west)

        self.fsm.add_transition(' ', 'NN', self.move_north)
        self.fsm.add_transition(' ', 'NE', self.move_east)
        self.fsm.add_transition(' ', 'NS', self.move_south)
        self.fsm.add_transition(' ', 'NW', self.move_west)

        self.fsm.add_transition(' ', 'BN', self.move_north)
        self.fsm.add_transition(' ', 'BE', self.move_east)
        self.fsm.add_transition(' ', 'BS', self.move_south)
        self.fsm.add_transition(' ', 'BW', self.move_west)

        self.fsm.add_transition('B', 'NN', self.move_north, next_state='BN')
        self.fsm.add_transition('B', 'NW', self.move_west, next_state='BW')
        self.fsm.add_transition('B', 'NS', self.move_south, next_state='BS')
        self.fsm.add_transition('B', 'NE', self.move_east, next_state='BE')

        self.fsm.add_transition('B', 'BN', self.move_north, next_state='NN')
        self.fsm.add_transition('B', 'BW', self.move_west, next_state='NW')
        self.fsm.add_transition('B', 'BS', self.move_south, next_state='NS')
        self.fsm.add_transition('B', 'BE', self.move_east, next_state='NE')

        self.fsm.add_transition('$', 'NN', self.move_north, next_state='FIN')
        self.fsm.add_transition('$', 'NE', self.move_east, next_state='FIN')
        self.fsm.add_transition('$', 'NS', self.move_south, next_state='FIN')
        self.fsm.add_transition('$', 'NW', self.move_west, next_state='FIN')

        self.fsm.add_transition('$', 'BN', self.move_north, next_state='FIN')
        self.fsm.add_transition('$', 'BE', self.move_east, next_state='FIN')
        self.fsm.add_transition('$', 'BS', self.move_south, next_state='FIN')
        self.fsm.add_transition('$', 'BW', self.move_west, next_state='FIN')

    def reset(self, filename):
        """
        Resets the maze bot to have an empty path and sets the maze
        from the given filename. The bot starts at position 1, 1
        :param filename: The name of the file to read the maze in from
        """
        # The bot always starts at the Northwest corner of the maze
        self.x = 1
        self.y = 1

        # The path resets to empty
        self.path = []

        # Read in the maze from the file
        self.maze = []
        with open(filename) as f:
            line = f.readline().strip()
            self.maze.append(line)
            while line:
                line = f.readline().strip()
                self.maze.append(line)

    def move_south(self):
        """
        TODO: Implement move south
        Changes the bot's location 1 spot South
        and records the movement in self.path
        """
        self.y = self.y + 1
        self.path.append('SOUTH')

    def move_east(self):
        """
        TODO: Implement move east
        Changes the bot's location 1 spot East
        and records the movement in self.path
        """
        self.x = self.x + 1
        self.path.append('EAST')

    def move_north(self):
        """
        TODO: Implement move north
        Changes the bot's location 1 spot North
        and records the movement in self.path
        """
        self.y = self.y - 1
        self.path.append('NORTH')

    def move_west(self):
        """
        TODO: Implement move west
        Changes the bot's location 1 spot West
        and records the movement in self.path
        """
        self.x = self.x - 1
        self.path.append('WEST')

    def get_next_space(self):
        """
        TODO: Implement get next space
        Using the current state of the bot, returns the next space in the maze
            Ex. If the current state has the bot moving south, the next space in the
            maze would be self.maze[self.y+1][self.x]
        :return: The next spot in the maze Ex. "B", "#", " ", "X"
        """
        if self.fsm.current_state == "NS" or self.fsm.current_state == "BS":
            return self.maze[self.y + 1][self.x]

        if self.fsm.current_state == "NE" or self.fsm.current_state == "BE":
            return self.maze[self.y][self.x + 1]

        if self.fsm.current_state == "NN" or self.fsm.current_state == "BN":
            return self.maze[self.y - 1][self.x]

        if self.fsm.current_state == "NW" or self.fsm.current_state == "BW":
            return self.maze[self.y][self.x - 1]

    def print_maze(self):
        """
        Prints the 2D array representing the maze
        Prints an 'M' for the current location of the bot in the maze
        """
        for row in range(len(self.maze)):
            curr = ''
            for col in range(len(self.maze[row])):
                if row == self.y and col == self.x:
                    curr += 'M'
                else:
                    curr += self.maze[row][col]
            print(curr)

    def solve_maze(self):
        """
        Calls on the FSM to process the next input symbol from the maze
        in order to transition the bot between states until it reaches the "FIN" state
        """
        # TODO: Implement solve maze
        while self.fsm.current_state != "FIN":
            self.fsm.process(self.get_next_space())
        print("Determined the path:")
        print(self.path)
games = ['Monopoly', 'Chess', 'Checkers']
num = 0
list = ""
while num < 3:
    list = list + games[num] + " "
    num = num + 1
print("List of games: " + list)
new_game = ''
while new_game != 'quit':
    new_game = input("Enter a game you like, or enter 'quit': ")
    if new_game != 'quit':
        list = list + new_game + " "
print("List of games: " + list)
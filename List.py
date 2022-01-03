players = [23, 34, 56, 78, 66, 87]
# Print item number 1
print(players[1])
# Set item number 1 to 99
players[1] = 99
print(players[1])
# print items to the end of the list
print(players + [45, 67])
# Add actually to the end of the list
players.append(120)
print(players)
# set items from start to 2 to zero
players[:2] = [0, 0]
print(players)
# Clean the list
players[:] = []
print(players)
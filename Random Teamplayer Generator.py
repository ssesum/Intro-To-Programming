"""
To write a program to randomly choose from an array element and randomly sort them into 2 groups.
"""

#Initialize a list of players into a list

player_list = ['player1', 'player2', 'player3', 'player4', 'player5', 'player6']

#print ("The Fortnite players are: %s" % (player_list))

the_players = "The Fortnite players are: "
for name_variable in player_list:
    the_players += name_variable + ", "
print (the_players[0:len(the_players)-2])

#First, randomize and split into two teams

from random import choice


#We make two teams and will be storing two players per team

Team_A = []
Team_B = []

#We now must choose the random players, and must remove the chosen from the players_list

Player_A = choice(player_list)
Team_A.append(Player_A)
player_list.remove(Player_A)

Player_a = choice(player_list)
print("Team A: %s, %s" % (Player_A, Player_a))
Team_A.append(Player_a)
player_list.remove(Player_a)

Player_B = choice(player_list)
Team_B.append(Player_B)
player_list.remove(Player_B)

Player_b = choice(player_list)
print ("Team B: %s, %s" % (Player_B, Player_b))
Team_B.append(Player_b)
player_list.remove(Player_b)


print("Players left: ", player_list)

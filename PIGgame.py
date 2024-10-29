                                   #PIG game
import random
#ROLL Function
def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val,max_val)
    return roll

while True :
    players = input("Enter the number of players (2-->4) ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4")
    else:
        print("Invalid, try again")

max_score = 50
players_score = [0 for i in range(players)]


while max(players_score) < max_score : 
    for player_idx in range(players) :
        print("\nIt is player number: ",player_idx+1," turn!")
        print("Your total score is : ",players_score[player_idx],"\n")
        current_score = 0
        while True :
            should_roll = input("You want to roll ? (y) ")
            if should_roll != "y" :
                break

            value = roll()
            if value == 1 :
                current_score = 0
                print("You have rolled 1, your turn is done! ")
                break
            else :
                current_score += value
                print("You rolled this value  : ",value)
            print("Your score is: ",current_score)

        players_score[player_idx] += current_score
        print("Your total score is : ",players_score[player_idx])

max_score = max(players_score)
winning_idx=players_score.index(max_score)
print ("player number ", winning_idx + 1," is the winner with a score of: ",max_score)
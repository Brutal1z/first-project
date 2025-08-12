from random import randint

Max_score = 100 #Score to win

#Function to roll the dice
def roll():
    num = randint(1,6)
    return num

print("------------------------------------")
print("Hello welcome to Pig, the dice game.")
print("------------------------------------\n")

#Start the game
play = input("Do you want to play? (Y/N): ")
if play.lower() != "y":
    print("Goodbye then.")
    quit()

#Loop for the game
while True:
    number_of_players = input("How many players are going to play (2-6): ")

    #Checks if the input is a number and its within 2 and 6.
    if number_of_players.isdigit():
         number_of_players = int(number_of_players)
         if not 1 < number_of_players <= 6:
            print("You can only play with 2 to 6 people, choose accordingly!")
            continue #skips everything and restarts the loop
    else: 
        print("You need to insert a valid number!")
        continue

    #List that stores the players score
    players_scores = [0 for _ in range(number_of_players)]

    #Starts the game until someone reaches Max_score
    while max(players_scores) < Max_score:
        current_score = 0 #Restart the curent score to 0
        for i, score in enumerate(players_scores): #Determines whose turn it is
            print("------------------------------------")
            print(f"Player {i + 1} turn.") # i = index of the list
            print("------------------------------------\n")
            print(f"Your total score is {players_scores[i]}.\n")
            while True: #Loop to roll the dice as many times as the player wants    
                action = input("Do you want to roll the dice? (Y/N): ")
                if action.lower() != "y":
                    players_scores[i] += current_score
                    print(f"Your total score is {players_scores[i]}.\n")
                    current_score = 0
                    break
                    
                value = roll()
                print(f"You got a {value}")

                 #If the player gets 1 his turn ends and the current score restarts 
                if value != 1:             
                    current_score += value
                    print(f"Current score = {current_score}")
                else:
                    print("Your turn is over.")
                    print(f"Your total score is {players_scores[i]}.\n")
                    current_score = 0
                    break

    #player_scores.index(num) gives the index of the item on the list player_scores that is == to num
    print(f"The winner is Player {players_scores.index(max(players_scores))+1} with {max(players_scores)} points.\n\n")  
    continue_playing = input("Do you want to play again? (Y/N):")       
    if continue_playing.lower() != "y":
        break
        
print("Goodbye then.")   
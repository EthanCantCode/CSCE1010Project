#CSCE 1010
#Names: Ethan Trombley, Kallen Schulz, Dabin Choi

import random



#Variables
aiPoints = 0
playerPoints = 0
targetPoints = 3

#Array
moveSet = ["Rock", "Paper", "Scissors"]
aiMove = moveSet[0]
playerMove = moveSet[0]


game = True

print("Welcome to Tic Tac Toe")

while game == True:

    #Player move
    print("Please select one")
    print("1: Rock\n2: Paper\n3: Scissors")


    #intSelect (Integer Selection) is to check to make sure the player enters a valid input
    intSelect = True
    while intSelect == True:

        #Try catch statment to make sure to not break the code if the player enters a string variable
        try:

            pSelect = int(input("Type your selection here: "))
            if pSelect == 1:
                playerMove = moveSet[0]
                break
            elif pSelect == 2:
                playerMove = moveSet[1]
                break
            elif pSelect == 3:
                playerMove = moveSet[2]
                break
            else:
                print("\nPlease select a valid input (1, 2 or 3)\n")        
        except ValueError:
            print("\nPlease select a number\n")
      

    print(f"\nYou selected {playerMove}")
    


    #AI move is determined by a random selection of numbers ranging 0-2
    aiRandom = random.randint(0,2)

    if aiRandom == 0:
        aiMove = moveSet[0]
    elif aiRandom == 1:
        aiMove = moveSet[1]
    elif aiRandom == 2:
        aiMove = moveSet[2]
    else:
        print(aiRandom)

    print(f"AI selected {aiMove}\n")


    #We need to make a section that checks who wins
    if playerMove == aiMove:
        print("It's a tie!\n")
    elif playerMove == "Rock" and aiMove == "Scissors":
        print("You win!\n")
        playerPoints += 1
    elif playerMove == "Paper" and aiMove == "Rock":
        print("You win!\n")
        playerPoints += 1
    elif playerMove == "Scissors" and aiMove == "Paper":
        print("You win!\n")
        playerPoints += 1
    else:
        print("You lose!\n")
        aiPoints += 1
    print(f"Your points: {playerPoints}\nAI points: {aiPoints}\n")

    if playerPoints == targetPoints:
        print("You win the game!")
        game = False
        break

    elif aiPoints == targetPoints:
        print("You lose the game!")
        game = False
        break



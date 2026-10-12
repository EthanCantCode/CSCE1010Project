#CSCE 1010
#Names: Ethan Trombley, Kallen Schulz, Dabin Choi

import random



#Variables
aiPoints = 0
playerPoints = 0

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

    intSelect = True
    while intSelect == True:

        try:

            pSelect = int(input("Type your selection here: "))
            if pSelect == 1:
                playerMove == moveSet[0]
                break
            elif pSelect == 2:
                playerMove == moveSet[1]
                break
            elif pSelect == 3:
                playerMove == moveSet[2]
                break
            else:
                print("\nPlease select a valid input (1, 2 or 3)\n")        
                    

        except ValueError:
            print("\nPlease select a number\n")

        

    print(f"\nYou selected {playerMove}")
    


    #AI move
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





print(f"AI went {aiMove}")

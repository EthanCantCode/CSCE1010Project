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
aiRandom = random.randint(0,2)


#AI moveset (This block will be moved soon into a while loop)
if aiRandom == 0:
    aiMove = moveSet[0]
elif aiRandom == 1:
    aiMove = moveSet[1]
elif aiRandom == 2:
    aiMove = moveSet[2]
else:
    print(aiRandom)



print(f"AI went {aiMove}")

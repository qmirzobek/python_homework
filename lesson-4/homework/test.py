# Bonus Challenge
import random
choices=['rock','paper','scissors']
computerScore=0
userScore=0
while True:
    computerChoice=random.choice(choices)
    print("User score: ",userScore)
    print("Computer score: ",computerScore)
    # print(computerChoice)
    while True:
        userChoice=input('Enter your choice(rock, paper, scissors): ')
        if(userChoice.lower() in choices):
            break
    if(computerChoice=='rock'):
        if(userChoice.lower()=='rock'):
            print('Draw')
        elif(userChoice.lower()=='paper'):
            print('User got one point')
            userScore+=1
        else:
            print("Computer got one point")
            computerScore+=1
    elif(computerChoice=="paper"):
        if(userChoice.lower()=='paper'):
            print('Draw')
        elif(userChoice.lower()=='scissors'):
            print('User got one point')
            userScore+=1
        else:
            print("Computer got one point")
            computerScore+=1
    else:
        if(userChoice.lower()=='scissors'):
            print('Draw')
        elif(userChoice.lower()=='rock'):
            print('User got one point')
            userScore+=1
        else:
            print("Computer got one point")
            computerScore+=1
    if(userScore>=5):
        print('User won the game!')
        break
    elif(computerScore>=5):
        print('Computer won the game')
        break

    

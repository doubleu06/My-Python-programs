import random

computerScore = 0
playerScore = 0
computer = 0
player = 1
playOn = ''

tossOptions = [0,1]
toss = random.choice(tossOptions)
inputToss = int(input('Enter your toss choice 0/1 :'))
if inputToss == toss:
    print('you have win the toss.')
    playOn = 'Player'
else:
    print('You have lose the toss.')
    playOn = 'computer'

while computer != player:
    computer = random.randint(1,6)
    player = int(input('Enter a number between 1-6 :'))
    while player not in range(1,7):
        print('Enter a number between 1 - 6')
        player = int(input('Enter a number between 1-6 :'))
    print('Computer said :',computer)
    print('You said :',player)
    if computer != player:
        if playOn == 'computer':
            computerScore += computer
        else:
            playerScore += player

if playOn == 'computer':
    print('computer totals :',computerScore)
    print('You need',computerScore,'to win.')
    playOn = 'player'
else:
    print('Your total score :',playerScore)
    print('Computer needs',playerScore,'to win.')
    playOn = 'computer'

computer = 0
player = 1
if computerScore > 0 and playerScore == 0:
    while computer != player and playerScore < computerScore:
        computer = random.randint(1,6)
        player = int(input('Enter a number between 1-6 :'))
        while player not in range(1,7):
            print('Enter a number between 1 - 6')
            player = int(input('Enter a number between 1-6 :'))
        print('Computer said :',computer)
        print('You said :',player)
        if computer != player:
            if playOn == 'computer':
                computerScore += computer
            else:
                playerScore += player
    if playOn == 'computer':
        print('computer totals :',computerScore)   
    else:
        print('Your total score :',playerScore)
elif playerScore > 0 and computerScore == 0:
    while computer != player and computerScore < playerScore:
        computer = random.randint(1,6)
        player = int(input('Enter a number between 1-6 :'))
        while player not in range(1,7):
            print('Enter a number between 1 - 6')
            player = int(input('Enter a number between 1-6 :'))
        print('Computer said :',computer)
        print('You said :',player)
        if computer != player:
            if playOn == 'computer':
                computerScore += computer
            else:
                playerScore += player
    if playOn == 'computer':
        print('computer totals :',computerScore)   
    else:
        print('Your total score :',playerScore)

    
if computerScore < playerScore:
    print('You win.')
elif computerScore > playerScore:
    print('Computer win.')
else:
    print('Match draw.')
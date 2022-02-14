
print('KNOW YOUR RELATIONSHIP .....')
# get the first player name
playerFirst = input('Enter your name :')

# get the second player name
playerSecond = input('Enter the person name :')

# check for duplicates letter
for i in playerFirst:
    if i in playerSecond:

        # remove from both names
        playerFirst = playerFirst.replace(i,'')
        playerSecond = playerSecond.replace(i,'')


# attach the remaining characters
attachedWord = playerFirst + playerSecond


flames = ['F','L','A','M','E','S']

leftPart = []
rightPart = []
newFlames = []

# count the flames characters and remove the last character
# next count starts from the end point till one character left
while len(flames) > 1:
    if len(attachedWord) > len(flames):
        remained = len(attachedWord) - len(flames)
        while remained > len(flames):
            remained = remained - len(flames)
        remainingLength = remained
    else:
        remainingLength = len(attachedWord)
    
    leftPart = []
    rightPart = []
    newFlames = []
    if remainingLength == len(flames):
        flames.remove(flames[-1])
    else:
        for i in flames[0:remainingLength]:
            leftPart.append(i)
        for j in flames[remainingLength:]:
            rightPart.append(j)
        leftPart.pop()
        newFlames = rightPart + leftPart
        flames = newFlames

# tell the meaning of the character
if flames[0] == 'F':
    print('Relationship Status : Friends')
elif flames[0] == 'L':
    print('Relationship Status : Love')
elif flames[0] == 'A':
    print('Relationship Status : Affection')
elif flames[0] == 'M':
    print('Relationship Status : Marraige')
elif flames[0] == 'E':
    print('Relationship Status : Enemy')
else:
    print('Relationship Status : Siblings')     



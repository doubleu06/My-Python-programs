import random
fruitsList = ['apple','kiwi','strawberry','pomogranate','starfruit','walnut','banana','raisin','guava','date','coconut','papaya']
vegetableList = ['cauliflower','brinjal','drumstick','potato','bittergourd','cabbage','onion','chilli','tomato','capsicum']
objectList = ['chair','table','scissors','book','pencil','diary','bottle','tubelight','bed']
appliancesList = ['oven','computer','television','iron','washingmachine','mixer','sewingmachine','pressurecooker']
sportsList = ['cricket','polo','tabletennis','lawntennis','horseracing','football','basketball','baseball','paragliding','judo','boxing','swimming']
animalList = ['lion','tiger','giraffe','aligator','crocodile','rabbit','cheetah','leopard','jackal','fox','bison','snake','elephant']
birdList = ['sparrow','peacock','cuckoo','cock','ostrich','kiwi','hen','crow','maina','flamingo','swan','duck','eagle','woodpecker']
aquaticAnimalList = ['octopus','shark','whale','dolphin','turtle','starfish','eel','seahorse','piranha']
treeList = ['oak','sal','teak','banyan','ashok','gulmohar','willow','peepal']
countryList = ['india','pakistan','america','nepal','indonesia','bangladesh','japan','china','eslovakia','brazil','canada','maldives']
wordLists = [fruitsList,vegetableList,objectList,appliancesList,sportsList,animalList,birdList,aquaticAnimalList,treeList,countryList]
wordList = random.choice(wordLists)

word = random.choice(wordList)
word = word.replace('\n', '')
guessword = ''
for i in word:
    guessword += '*'
print('the game starts now.......\n\n')
if wordList == fruitsList:
    print('this is a fruit.')
elif wordList == vegetableList:
    print('this is a vegetable.')
elif wordList == objectList:
    print('this is an object.')
elif wordList == sportsList:
    print('this is a sport.')
elif wordList == animalList:
    print('this is an animal.')
elif wordList == birdList:
    print('this is a bird.')
elif wordList == aquaticAnimalList:
    print('this is an aquatic animal.')
elif wordList == treeList:
    print('this is a tree.')
elif wordList == countryList:
    print('this is a country.')
else:
    print('this is an appliance.')
print('your word is : ',guessword)

n = 0
guessed = {'',}
wrongCount = 4
while wrongCount > 0 and guessword != word:
    nextGuess = input('Guess a character : ')
    if nextGuess not in word:
        print(nextGuess, 'not in word.')
        wrongCount -= 1
        print(f'you have {wrongCount} attempt left.')
    elif nextGuess == '':
        print('you have not guessed anything.')
    elif nextGuess in guessed:
        print('you have already guessed the character.')
    else:
        print(nextGuess, 'is in word.')

        con = []
        count = 0
        for i in word:
            if i == nextGuess:
                con.append(count)
            count += 1

        guessList =[]
        for i in guessword:
            guessList.append(i)

        for j in con:
            guessList[j] = nextGuess
        guessword = ''.join(guessList)
        print(guessword)
    guessed.add(nextGuess)
    n += 1

print('the word was', word)





characters = {'A':'Z','B':'Y','C':'X','D':'W','E':'V','F':'U','G':'T','H':'S','I':'R','J':'Q','K':'P','L':'O',
'M':'N','N':'M','O':'L','P':'K','Q':'J','R':'I','S':'H','T':'G','U':'F','V':'E','W':'D','X':'C','Y':'B','Z':'A',' ': ' '}
characterList = []
word = input('enter a string :')

for i in word.upper():
    characterList.append(characters[i])

newWord = ''.join(characterList)
print('the encrypted version is :',newWord)
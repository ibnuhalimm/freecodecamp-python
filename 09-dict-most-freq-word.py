print('------------------------------------------')
print('  ***', 'Most Frequent Word in a File', '***')
print('------------------------------------------')
fileinput = input('Input the file: ')

try:
    fileopen = open(fileinput, 'r')
except:
    print('Unable to find the file.')
    quit()

words = list(fileopen.read().split())
dictwords = dict()

for word in words:
    dictwords[word] = dictwords.get(word, 0) + 1

freqword = None
biggestcount = None

for word,count in dictwords.items():
    if biggestcount is None or biggestcount < count:
        biggestcount = count
        freqword = word

print('\n-------------------------------------')
print('The most frequent word is', freqword)
print('It appears', biggestcount, 'times')
print('-------------------------------------')


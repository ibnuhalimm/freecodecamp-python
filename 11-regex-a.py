import re

fileopen = open('mbox.txt', 'r')

linenumber = 0
for line in fileopen:
    if(re.search('^Type', line)):
        print('We found this', '`', line.rstrip(), '`', 'on line', linenumber)
        break;
    linenumber = linenumber + 1

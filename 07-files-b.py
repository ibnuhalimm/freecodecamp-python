mbox = open('mbox.txt', 'r')
filechar = mbox.read()
replacednewline = filechar.replace('\n', '--')
print(replacednewline)
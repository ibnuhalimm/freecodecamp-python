fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

print('Your file contains this text:')
print('-------------------')
for line in fhand:
    print(line.rstrip())
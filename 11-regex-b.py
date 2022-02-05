import re

print("--- re.findall implementation ---\n")

text = "A message from cs@mail.com and support@mail.com about maintenance @2AM"
matches_string = re.findall('\\S+@\\S+', text)

print('Text :', text)
print('Result :', matches_string)
print('\n--------------------------------------')

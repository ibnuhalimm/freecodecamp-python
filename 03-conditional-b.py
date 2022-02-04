temp = "5 degrees"

try:
    fahr = float(temp)
    cel = (fahr - 32.0) * 5.0 / 9.0
except:
    cel = 0

print(cel)
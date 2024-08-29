number = 0b11111111
numberStr = "11111111"
origStr = numberStr
output = 0
while len(numberStr) > 0:
    output += int(numberStr[0]) * 2**(len(numberStr) - 1)
    numberStr = numberStr[1 : len(numberStr)]
    
print("Converting " + origStr + " to decimal yields %d" % output)

number = 11111111
output = ""
while number > 0:
    output += number % 2
    number /2

print("Converting " + origStr + "in decimal to bimnry yields %d" % output)

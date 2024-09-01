#Bonus problems

#Converting binary to decimal
number = 0b11111111
numberStr = "11111111"
origStr = numberStr
output = 0
while len(numberStr) > 0:
    output += int(numberStr[0]) * 2**(len(numberStr) - 1)
    numberStr = numberStr[1 : len(numberStr)]
    
print("Converting " + origStr + " to decimal yields %d" % output)

#Converting decimal to binary
#follows the remainder formula for converting decimal to binary
number = 11111111
sign = "0" if number > 0 else "1"
output = ""
while abs(number) > 0:
    output += str(number % 2)
    number = int(number/ 2)



print("Converting " + origStr + "in decimal to singed binary yields " + sign + output)

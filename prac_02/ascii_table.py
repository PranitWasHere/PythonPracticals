character = input("Enter a character: ")
print("The ASCII code for g is",ord(character))
LOWER = 33
UPPER = 127
while True:
    number = int(input("Enter a number between {0} and {1}: ".format(LOWER,UPPER)))
    if number < LOWER or number > UPPER:
        print("Invalid number")
        break
    print("The character for {0} is {1}".format(number,chr(number)))


for n in range(LOWER,UPPER+1,1):
    print("{:>3}{:>5}".format(n,chr(n)))

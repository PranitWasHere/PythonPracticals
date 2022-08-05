name_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=name_file)
name_file.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is", name)
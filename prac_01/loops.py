# a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c
stars = int(input("Number of stars: "))
for i in range(stars):
    print("*", end="")
print()

# d
stars = int(input("Number of stars: "))
for i in range(1,stars):
    print("*"*i)

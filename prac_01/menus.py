name = input("Enter name: ")
MENU = """(H)ello
(G)oodbye
(Q)uit"""
print(MENU)
choice = input()
while choice != "Q":
    if choice == "H":
        print("hello ",name)
    elif choice == "G":
        print("goodbye ",name)
    else:
        print("invalid message")
    print(MENU)
    choice = input()
print("Finished.")

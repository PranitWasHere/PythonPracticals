def main():
    COLORS = {"ALICEBLUE": "#f0f8ff", "BISTRE": "#3d2b1f"}
    color = input("Color: ").upper()
    while color != "":
        if color in COLORS:
            print(color, "is", COLORS[color])
        else:
            print("Invalid color.")
        color = input("color: ").upper()



main()
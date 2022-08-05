def to_celsius():
    temps=[]
    with open("temps_input.txt","r+") as file:
        for temp in file:
            # print(temp)
            celsius= 5 / 9 * (float(temp) - 32)
            temps.append(celsius)
            print(celsius)
    with open("temps_output.txt","a") as f:
        for temp in temps:
            f.write(str(temp)+"\n")

to_celsius()
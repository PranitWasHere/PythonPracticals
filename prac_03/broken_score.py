"""
CP1404 - Practical
Broken program to determine score status
"""

import random



def determine_score(score):
    if 0 <= score <= 100:
        if score < 50:
            return "Bad"
        elif 50 <= score < 90:
            return "Passable"
        else:
            return "Excellent"
    else:
        return "Invalid score"

def main():
    number_of_scores = int(input("Enter number of scores: "))
    with open("results.txt", "a") as file:
        for i in range(number_of_scores):
            score = random.randint(0,100)
            file.write(f"{score} is {determine_score(score)}\n")

if __name__ == '__main__':
    main()
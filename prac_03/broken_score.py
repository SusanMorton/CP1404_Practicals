"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random
def main():

    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    score_result = result_checker(score)
    print(score_result)
    random_score = random.randint(0, 100)
    print(random_score)
    random_result = result_checker(random_score)
    print(random_result)


def result_checker(score):

    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"



main()
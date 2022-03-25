#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created March 2022
# This program prompts a user to guess a number
# and tells them if they are correct or not (random number).

import random


def main():
    # this function gets a guess then checks if it is right

    # input
    guessed_number = int(input("Enter a number between 0 and 9: "))

    # process & output
    random_number = random.randint(0, 9)  # a number between 0 and 9
    if guessed_number == random_number:
        print("You Guessed Correctly!")
    else:
        print(
            "You Guessed Incorrectly. The correct number was {}.".format(random_number)
        )
    print("\nDone.")


if __name__ == "__main__":
    main()

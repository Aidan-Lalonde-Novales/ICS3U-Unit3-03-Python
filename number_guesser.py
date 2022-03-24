#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created March 2022
# This program prompts a user to guess a number
# and tells them if they are correct or not.

import constants


def main():
    # this function gets a guess then checks if it is right

    # input
    guessed_number = int(input("Enter a number between 0 and 9: "))

    # process & output
    if guessed_number == constants.RANDOM_NUMBER:
        print("You Guessed Correctly!")
    if guessed_number != constants.RANDOM_NUMBER:
        print("You Guessed Incorrectly.")
    print("\nDone.")


if __name__ == "__main__":
    main()

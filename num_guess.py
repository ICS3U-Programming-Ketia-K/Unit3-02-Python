#!/usr/bin/env python3

# Created by: Ketia Gaelle Kaze
# Created on: Dec 2021
# This program checks if the guessed number is right


import constants


def main():
    # this function checks if the guessed number is right

    # input
    guessed_number = int(input("Enter the guessed number between 0 and 9: "))
    print("")

    # process & output
    if guessed_number == constants.RIGHT_NUMBER:
        print("Congrats, you guessed right!")
    if guessed_number != constants.RIGHT_NUMBER:
        print("Oops, you guessed wrong:(")


if __name__ == "__main__":
    main()

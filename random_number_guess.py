#!/usr/bin/env python3

# Created by: Izza Khalid
# Created on: October 2019
# This program checks if the number you chose matches
# with user input

import random
some_variable = random.randint(1, 100)
# a number between 1 and 100


def main():
    # This function checks if the number you chose matches

    # input
    print("Quick! Pick a number between 0 and 100")
    print("")
    your_number = int(input("Enter the number of your choice: "))

    # process
    if your_number == some_variable:

    # output
        print("")
        print("You got it right")
    else:
        print("")
        print("Better luck next time")
        print("The random number was", some_variable,".")


if __name__ == "__main__":
    main()

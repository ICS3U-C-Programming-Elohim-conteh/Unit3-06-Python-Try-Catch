#!/usr/bin/env python3
# Created by: Elohim
# Created on: nov 2026
# This program uses a try statement


def main():
    # this function uses a try statement

    # input
    integer_as_string = input("Enter an integer: ")
    print("")

    # process & output
    try:
        integer_as_number = int(integer_as_string)
        print("You entered an integer correctly")
    except Exception:
        print("This was not an integer")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()

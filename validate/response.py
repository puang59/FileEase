#!/usr/bin/env python3
from click import prompt

def get_yes_no_input(question):
    while True:
        response = prompt(question)
        if response.lower() in ("yes", "y"):
            return True
        elif response.lower() in ("no", "n"):
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == '__main__':
    get_yes_no_input()

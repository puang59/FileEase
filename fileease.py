#!/usr/bin/env python3
from public.logoascii import logo

from click import echo, prompt, IntRange, style
import logging
from tabulate import tabulate

from modules._managing import manager
from modules._encrypt import encrypt
from modules._decrypt import decrypt
from modules._compress import compress
from modules._extract import extract

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def display_menu():
    echo(logo)
    echo(tabulate([['Your Ultimate CLI Companion for everything Files and Folders related!']], tablefmt="fancy_grid", numalign="center", stralign="center"))
    echo(style("~ puang59\n", fg='red', bold=True))
    echo(f"{style('######## MENU ########', fg='cyan', bold=True)}")
    menu = [
        [style("1)", fg="yellow"), style("Manage Files", fg="white")],
        [style("2)", fg="yellow"), style("Encrypt Files", fg="white")],
        [style("3)", fg="yellow"), style("Decrypt Files", fg="white")],
        [style("4)", fg="yellow"), style("Compress Files", fg="white")],
        [style("5)", fg="yellow"), style("Extract Files", fg="white")]
    ]

    echo(tabulate(menu, tablefmt="fancy_grid"))

def main():
    try:
        # loading extensions
        options = {
            1: manager,
            2: encrypt,
            3: decrypt,
            4: compress,
            5: extract
        }
        
        while True:
            display_menu()
            option = prompt('\nSelect an option (1/2/3/4/5)', type=IntRange(1, 5))

            selected_function = options.get(option) 
            if selected_function:
                selected_function()
            else:
                echo("Invalid option. Please select a valid option.")
    except Exception as e:
        logging.error(str(e))
        echo(f"An error occurred. Please check the log file for details.")

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import os
import shutil
import click

from tabulate import tabulate

from modules._managing import manager
from modules._encrypt import encrypt
from modules._decrypt import decrypt 

@click.command()
def mainMenu():
    logo_ascii = '''
    /$$$$$$$$ /$$ /$$           /$$$$$$$$
   | $$_____/|__/| $$          | $$_____/
   | $$       /$$| $$  /$$$$$$ | $$        /$$$$$$   /$$$$$$$  /$$$$$$
   | $$$$$   | $$| $$ /$$__  $$| $$$$$    |____  $$ /$$_____/ /$$__  $$
   | $$__/   | $$| $$| $$$$$$$$| $$__/     /$$$$$$$|  $$$$$$ | $$$$$$$$
   | $$      | $$| $$| $$_____/| $$       /$$__  $$ \____  $$| $$_____/
   | $$      | $$| $$|  $$$$$$$| $$$$$$$$|  $$$$$$$ /$$$$$$$/|  $$$$$$$
   |__/      |__/|__/ \_______/|________/ \_______/|_______/  \_______/
    '''

    colored_logo = click.style(logo_ascii, fg='green', bold=True)
    name = click.style('~ puang59 \n', fg='red', bold=True)
    click.echo(colored_logo)
    click.echo(name)

    click.echo(f"      {click.style('##### MENU #####', fg='cyan', bold=True)}")
    menu = [
        ["1", "Manage Files"],
        ["2", "Encrypt Files"],
        ["3", "Decrypt Files"],
        ["4", "Compress Files"],
    ]
    click.echo(tabulate(menu, headers=["Option", "Description"], tablefmt="grid"))

    option = click.prompt('\nSelect an option (1/2/3)', type=int)

    if option == 1:
        click.echo(f"\n{click.style('1) Manage Files', fg='magenta', bold=True)}")
        manager()
    elif option == 2:
        click.echo(f"\n{click.style('2) Encrypt Files', fg='magenta', bold=True)}")
        encrypt()
    elif option == 3:
        click.echo(f"\n{click.style('3) Decrypt Files', fg='magenta', bold=True)}")
        decrypt()
    else:
        click.echo("Yet to release!")
        
if __name__ == '__main__':
    mainMenu()

#!/usr/bin/env python3
from modules.validate.response import get_yes_no_input

import click
import os
from cryptography.fernet import Fernet

from datetime import datetime

key = Fernet.generate_key()
cipher_suite = Fernet(key)

@click.command()
def encrypt():
    try:
        # Ask the user for the directory containing the file

        click.echo(click.style('\n2) Encrypt Files', fg='magenta', bold=True))
        directory = click.prompt('Enter the directory containing the file to encrypt', type=click.Path(exists=False, file_okay=False, dir_okay=True))
        directory = os.path.expanduser(directory)  # Expand the ~ to the home directory

        # Validate if the expanded directory exists
        if not os.path.exists(directory) or not os.path.isdir(directory):
            click.echo(f"Directory '{directory}' does not exist.")
            return

        # List files in the specified directory
        files = os.listdir(directory)

        if not files:
            click.echo(f"No files found in the directory: {directory}")
            return

        click.echo("Files in the directory:")
        for index, file in enumerate(files, start=1):
            index = click.style(str(index), fg='green')
            click.echo(f"{index}. {file}")

        file_index = click.prompt('\nSelect a file to encrypt (enter the file number)', type=int)

        if file_index < 1 or file_index > len(files):
            click.echo("Invalid file number. Please select a valid file.")
            return

        selected_file = os.path.join(directory, files[file_index - 1])

        # Read the content of the selected file
        with open(selected_file, 'rb') as f:
            file_data = f.read()

        # Encrypt the file data
        encrypted_data = cipher_suite.encrypt(file_data)

        # Save the encrypted data in a new file with a ".enc" extension
        encrypted_file = selected_file + ".enc"

        with open(encrypted_file, 'wb') as f:
            f.write(encrypted_data)

        selected_files = click.style(selected_file, fg='magenta')
        encrypted_files = click.style(encrypted_file, fg='magenta')
        click.echo(f"\nFile {selected_files} encrypted and saved as {encrypted_files}")
        encTitle = click.style("Encrption Key:", fg='red')
        click.echo(f"{encTitle} {key.decode()}")

        confirmation = get_yes_no_input(f'\nDo you want to store the key? ({click.style("yes", fg="green")}/{click.style("no", fg="red")})')

        now = datetime.now()
        formatted_date = now.strftime("%B %d, %I:%M %p")

        if confirmation:
            with open('keys.txt', 'a') as f: 
                filename = os.path.basename(selected_file)
                key_str = f"[{formatted_date}] [{filename}] -> {key.decode()}\n"
                f.write(key_str)

            click.echo(f"{click.style('Stored in keys.txt', fg='green')}")
        else:
            click.echo(f"{click.style('Thank you', fg='green')}")

    except Exception as e:
        click.echo(f"Error: {str(e)}")

if __name__ == '__main__':
    encrypt()

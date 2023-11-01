#!/usr/bin/env python3

import click
import os
from cryptography.fernet import Fernet

@click.command()
def decrypt():
    try:
        # Ask the user for the directory containing the encrypted file
        directory = click.prompt('Enter the directory containing the encrypted file', type=click.Path(exists=False, file_okay=False, dir_okay=True))
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

        file_index = click.prompt('\nSelect the encrypted file to decrypt (enter the file number)', type=int)

        if file_index < 1 or file_index > len(files):
            click.echo("Invalid file number. Please select a valid file.")
            return

        selected_file = os.path.join(directory, files[file_index - 1])

        key = click.prompt("Enter the encryption key", hide_input=True)

        # Read the content of the selected encrypted file
        with open(selected_file, 'rb') as f:
            encrypted_data = f.read()

        cipher_suite = Fernet(key.encode())  # Create a cipher suite with the provided key

        # Decrypt the file data
        decrypted_data = cipher_suite.decrypt(encrypted_data)

        # Save the decrypted data in a new file with a ".dec" extension
        decrypted_file = os.path.splitext(selected_file)[0] + ".dec"

        with open(decrypted_file, 'wb') as f:
            f.write(decrypted_data)

        selected_files = click.style(selected_file, fg='magenta')
        decrypted_files = click.style(decrypted_file, fg='magenta')
        click.echo(f"\nFile {selected_files} decrypted and saved as {decrypted_files}")

    except Exception as e:
        click.echo(f"Error: {str(e)}")

if __name__ == '__main__':
    decrypt()

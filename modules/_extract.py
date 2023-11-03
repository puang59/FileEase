#!/usr/bin/env python3

import click
import os
import zipfile

@click.command()
def extract():
    """ A module to extarct zipped files """
    
    try:
        # Ask the user for the path to the ZIP archive they want to extract

        click.echo(click.style('\n5) Extract Files', fg='magenta', bold=True))
        zip_filepath = click.prompt('Enter the path to the ZIP archive you want to extract', type=str)

        # Expand the ~ in the path to the home directory
        zip_filepath = os.path.expanduser(zip_filepath)

        # Validate if the specified path exists
        if not os.path.exists(zip_filepath):
            click.echo(f"Path '{zip_filepath}' does not exist.")
            return

        # Specify the extraction directory
        extract_directory = click.prompt('Enter the directory to extract the files', type=click.Path(file_okay=False, dir_okay=True))

        # Expand the ~ in the path to the home directory
        extract_directory = os.path.expanduser(extract_directory)

        # Create the extraction directory if it doesn't exist
        os.makedirs(extract_directory, exist_ok=True)

        with zipfile.ZipFile(zip_filepath, 'r') as zipf:
            zipf.extractall(extract_directory)

        click.echo(f"Files from {zip_filepath} have been extracted to {extract_directory}")

    except Exception as e:
        click.echo(f"Error: {str(e)}")

if __name__ == '__main__':
    extract()

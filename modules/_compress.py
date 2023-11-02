#!/usr/bin/env python3

import click
import os
import zipfile

@click.command()
def compress():
    try:
        # Ask the user for the directory containing the files to compress

        click.echo(click.style('\n4) Compress Files', fg='magenta', bold=True))
        directory = click.prompt('Enter the directory containing the files to compress', type=click.Path(exists=False, file_okay=False, dir_okay=True))
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

        zip_filename = click.prompt('Enter a name for the ZIP archive (e.g., my_archive)', type=str)

        # Add .zip extension if not provided
        if not zip_filename.endswith('.zip'):
            zip_filename += '.zip'

        zip_location = click.prompt('Enter the location to store the ZIP file', type=str)

        # Expand the ~ in the path to the home directory
        zip_location = os.path.expanduser(zip_location)

        # Create a ZIP archive with the specified name and location
        zip_filepath = os.path.join(zip_location, zip_filename)

        with zipfile.ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in files:
                file_path = os.path.join(directory, file)
                zipf.write(file_path, arcname=file)

        zip_filename = click.style(zip_filename, fg='magenta')
        click.echo(f"\nFiles in the directory have been compressed into {zip_filename}")

    except Exception as e:
        click.echo(f"Error: {str(e)}")

if __name__ == '__main__':
    compress()

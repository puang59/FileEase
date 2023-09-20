#!/usr/bin/env python3

import os
import shutil
import click

@click.command()
def main():
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
    print(colored_logo)
    print(name)
    try:
        def folderPrompt():
            folderPath = click.prompt('What folder do you want to organize? (path) ')
            folderPath = os.path.expanduser(folderPath)  # Expand the ~ to the home directory
            files = os.listdir(folderPath)
            return folderPath, files  # Return folderPath and files

        try:
            folderPath, files = folderPrompt()
        except FileNotFoundError as e:
            print("Please try '~/<directory>'")
            folderPath, files = folderPrompt()

        organizeMethod = click.prompt(f"Do you want keyword organizing? ({click.style('yes', fg='green')}/{click.style('no', fg='red')}) ")

        if organizeMethod.lower() == "yes" or organizeMethod.lower() == "y":
            keyword = click.prompt("Enter Keyword ")
            masterFolderName = keyword
            totalFiles = 0
            for file in files:
                if keyword.lower() in file.lower():
                    totalFiles += 1

            confirmation = click.prompt(f"\n{click.style('Summary: ', fg='cyan')}\nMode -> Keyword organizing ({keyword})\nFolder -> {folderPath}\nMaster Folder -> {folderPath}/{keyword}\nFiles -> {totalFiles} items\n\nContinue? ({click.style('yes', fg='green')}/{click.style('no', fg='red')}) ")
            if confirmation.lower() == "yes" or confirmation.lower() == "y":
                pass
            elif confirmation.lower() == "no" or confirmation.lower() == "n":
                print("Terminating!!")
                return

            for file in files:
                if keyword.lower() in file.lower():  # Check if keyword is present in the file name
                    source_path = os.path.join(folderPath, file)
                    target_directory = os.path.join(folderPath, masterFolderName)
                    if os.path.isdir(source_path):
                        print(f"Skipping directory: {file}")
                        continue
                    os.makedirs(target_directory, exist_ok=True)  # Use exist_ok to avoid errors if the directory already exists
                    shutil.move(source_path, os.path.join(target_directory, file))
            click.echo("Done! Files are organized by keyword ;)")
            return  # Exit without asking for extensions
        elif organizeMethod.lower() == "no" or organizeMethod.lower() == "n":
            pass
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

        extensionsPrompt = click.prompt('Extensions (example - jpg, png, gif) ')

        if "," in extensionsPrompt:
            extensionsSplit = extensionsPrompt.split(',')
            extensionsList = [f'.{ext.strip()}' for ext in extensionsSplit]  # Add a dot (.) to each extension
        else:
            extensionsSplit = extensionsPrompt.split(' ')
            extensionsList = [f'.{ext.strip()}' for ext in extensionsSplit]  # Add a dot (.) to each extension

        diffFolderPrompt = click.prompt(
            f"Do you want to create different folders for different extensions? ({click.style('yes', fg='green')}/{click.style('no', fg='red')}) ")


        masterFolderPrompt = click.prompt(f'Do you want to create {click.style("Master Folder", fg="yellow")}? ({click.style("yes", fg="green")}/{click.style("no", fg="red")}) ')
        if masterFolderPrompt.lower() == 'yes' or masterFolderPrompt.lower() == 'y':
            pass
        elif masterFolderPrompt.lower() == 'no' or masterFolderPrompt.lower() == 'n':
            totalFiles = 0
            for file in files:
                filename, extension = os.path.splitext(file)
                if extension.lower() in extensionsList:
                    totalFiles += 1

            confirmation = click.prompt(f"\n{click.style('Summary: ', fg='cyan')}\nMode -> Extension organizing\nFolder -> {folderPath}\nMaster Folder -> None\nExtensions -> {extensionsPrompt}\nFiles -> {totalFiles} items\n\nContinue? ({click.style('yes', fg='green')}/{click.style('no', fg='red')}) ")

            if confirmation.lower() == "yes" or confirmation.lower() == "y":
                pass
            elif confirmation.lower() == "no" or confirmation.lower() == "n":
                print("Terminating!!")
                return

            for file in files:
                filename, extension = os.path.splitext(file)
                if extension.lower() in extensionsList:
                    target_directory = os.path.join(folderPath, folderPath, extension[1:])
                    os.makedirs(target_directory, exist_ok=True)  # Use exist_ok to avoid errors if the directory already exists
                    shutil.move(os.path.join(folderPath, file), os.path.join(target_directory, file))
            click.echo("Done! Your files are organized ;)")
            return
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

            for file in files:
                filename, extension = os.path.splitext(file)
                if extension.lower() in extensionsList:
                    target_directory = os.path.join(folderPath, masterFolderName, extension[1:])
                    os.makedirs(target_directory, exist_ok=True)  # Use exist_ok to avoid errors if the directory already exists
                    shutil.move(os.path.join(folderPath, file), os.path.join(target_directory, file))

        def masterFolderCheck():
            while True:

                masterFolderName = click.prompt(f'What would be the name of your Master folder? ({click.style("yes", fg="green")}/{click.style("no", fg="green")})')
                checkMaster = os.path.join(folderPath, masterFolderName)
                if os.path.exists(checkMaster):
                    overwritePrompt = click.prompt(
                        f"The folder '{masterFolderName}' already exists in the directory. Do you want to use it as your Master folder? " +
                        f"({click.style('yes', fg='green')}/{click.style('no', fg='red')}) ")
                    if overwritePrompt.lower() == "yes" or overwritePrompt.lower() == "y":
                        return masterFolderName
                else:
                    os.makedirs(checkMaster)
                    return masterFolderName

        masterFolderName = masterFolderCheck()

        if diffFolderPrompt.lower() == "yes" or diffFolderPrompt.lower() == "y":
            # Organizing files in different extension folders
            for file in files:
                filename, extension = os.path.splitext(file)
                if extension.lower() in extensionsList:
                    target_directory = os.path.join(folderPath, masterFolderName, extension[1:])
                    os.makedirs(target_directory, exist_ok=True)  # Use exist_ok to avoid errors if the directory already exists
                    shutil.move(os.path.join(folderPath, file), os.path.join(target_directory, file))
        elif diffFolderPrompt.lower() == "no" or diffFolderPrompt.lower() == "n":
            # Organizing files in Master folder
            for file in files:
                filename, extension = os.path.splitext(file)
                if extension.lower() in extensionsList:
                    target_directory = os.path.join(folderPath, masterFolderName)
                    os.makedirs(target_directory, exist_ok=True)  # Use exist_ok to avoid errors if the directory already exists
                    shutil.move(os.path.join(folderPath, file), os.path.join(target_directory, file))
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

        click.echo("Done! Your files are organized ;)")

    except (FileNotFoundError, PermissionError) as e:
        diffFolderPrompt = click.prompt(
            f"{click.style('Something went wrong!!!', fg='red')}\n\n")
        click.echo(f"Traceback:\n {e}")

if __name__ == '__main__':
    main()

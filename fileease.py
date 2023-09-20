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

        def get_yes_no_input(question):
            while True:
                response = click.prompt(question)
                if response.lower() == "yes" or response.lower() == "y":
                    return True
                elif response.lower() == "no" or response.lower() == "n":
                    return False
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

        while True:
            organizeMethod = get_yes_no_input(f"Do you want keyword organizing? ({click.style('yes', fg='green')}/{click.style('no', fg='red')}) ")
            if organizeMethod:
                keyword = click.prompt("Enter Keyword ")
                masterFolderName = keyword
                totalFiles = 0
                for file in files:
                    if keyword.lower() in file.lower():
                        totalFiles += 1

                confirmation = get_yes_no_input(f"\n{click.style('Summary: ', fg='cyan')}\nMode -> Keyword organizing ({keyword})\nFolder -> {folderPath}\nMaster Folder -> {folderPath}/{keyword}\nFiles -> {totalFiles-1} items\n\nContinue? ({click.style('yes', fg='green')}/{click.style('no', fg='red')}) ")
                if not confirmation:
                    print("Terminating!!")
                    return

                for file in files:
                    if keyword.lower() in file.lower():  # Check if keyword is present in the file name
                        source_path = os.path.join(folderPath, file)
                        target_directory = os.path.join(folderPath, masterFolderName)
                        if os.path.isdir(source_path):
                            # print(f"Skipping directory: {file}")
                            continue
                        os.makedirs(target_directory, exist_ok=True)  # Use exist_ok to avoid errors if the directory already exists
                        shutil.move(source_path, os.path.join(target_directory, file))
                        print(f"Moved {click.style(file, fg='magenta')} successfully")

                click.echo(f"{click.style('Done! Files are organized by keyword ;>', fg='green')}")
                return  # Exit without asking for extensions

            elif not organizeMethod:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        extensionsPrompt = click.prompt('Extensions (example - jpg, png, gif) ')

        if "," in extensionsPrompt:
            extensionsSplit = extensionsPrompt.split(',')
            extensionsList = [f'.{ext.strip()}' for ext in extensionsSplit]  # Add a dot (.) to each extension
        else:
            extensionsSplit = extensionsPrompt.split(' ')
            extensionsList = [f'.{ext.strip()}' for ext in extensionsSplit]  # Add a dot (.) to each extension

        diffFolderPrompt = get_yes_no_input(f"Do you want to create different folders for different extensions? ({click.style('yes', fg='green')}/{click.style('no', fg='red')}) ")
        masterFolderName = "None"

        if diffFolderPrompt:
            masterFolderPrompt = get_yes_no_input(f"Do you want to create {click.style('Master Folder', fg='yellow')}? ({click.style('yes', fg='green')}/{click.style('no', fg='red')}) ")
            if masterFolderPrompt:
                masterFolderName = click.prompt(f'What would be the name of your Master folder?')
                checkMaster = os.path.join(folderPath, masterFolderName)
                if os.path.exists(checkMaster):
                    overwritePrompt = get_yes_no_input(
                        f"The folder '{masterFolderName}' already exists in the directory. Do you want to use it as your Master folder? " +
                        f"({click.style('yes', fg='green')}/{click.style('no', fg='red')}) ")
                    if not overwritePrompt:
                        print("Terminating!!")
                        return
                else:
                    os.makedirs(checkMaster)
        else:
            masterFolderName = None

        totalFiles = 0
        for file in files:
            filename, extension = os.path.splitext(file)
            if extension.lower() in extensionsList:
                totalFiles += 1

        confirmation = get_yes_no_input(f"\n{click.style('Summary: ', fg='cyan')}\nMode -> Extension organizing \nFolder -> {folderPath}\nMaster Folder -> {folderPath}/{masterFolderName} \nFiles -> {totalFiles} items\n\nContinue? ({click.style('yes', fg='green')}/{click.style('no', fg='red')}) ")
        if not confirmation:
            print("Terminating!!")
            return

        for file in files:
            filename, extension = os.path.splitext(file)
            if extension.lower() in extensionsList:
                target_directory = folderPath
                if diffFolderPrompt:
                    if masterFolderName:
                        target_directory = os.path.join(folderPath, masterFolderName, extension[1:])
                    else:
                        target_directory = os.path.join(folderPath, extension[1:])
                os.makedirs(target_directory, exist_ok=True)  # Use exist_ok to avoid errors if the directory already exists
                shutil.move(os.path.join(folderPath, file), os.path.join(target_directory, file))
                print(f"Moved {click.style(file, fg='magenta')} successfully")

        click.echo(f"{click.style('Done! Files are organized ;>', fg='green')}")

    except (FileNotFoundError, PermissionError) as e:
        diffFolderPrompt = click.prompt(
            f"{click.style('Something went wrong!!!', fg='red')}\n\n")
        click.echo(f"Traceback:\n {e}")

if __name__ == '__main__':
    main()

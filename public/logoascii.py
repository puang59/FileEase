import click 

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
logo = click.style(logo_ascii, fg='green', bold=True)

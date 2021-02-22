import os
import sys


def clear_console():
    os.system('cls') if sys.platform.startswith('win32') else os.system('clear')


def title(title: str):
    print()
    print("****** " + title + " ******")
    print()


def subtitle(subtitle: str):
    print()
    print(subtitle + ":")
    print()

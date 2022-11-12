from colorama import Fore
from colorama import init as initColorama
from platform import system as osType
from os import system

# Colors for every possible message type
class clrs:
    Info = Fore.YELLOW
    Success = Fore.GREEN
    Error = Fore.RED
    Ask = Fore.CYAN

# Initiating colorama
initColorama(autoreset=True)

# Print information function
def info(txt):
    try:
        print(clrs.Info+txt)
    except:
        return None

# Print an error message
def error(txt):
    try:
        print(clrs.Error+txt)
    except:
        return None

# Print a success message
def success(txt):
    try:
        print(clrs.Success+txt)
    except:
        return None

# Print a question (input())
def ask(txt):
    try:
        return input(clrs.Ask+txt)
    except:
        return input(txt)

# Clear output (cls/clear)
def cls():
    try:
        if osType() == "Windows":
            system("cls")
        elif osType() == "Linux":
            system("clear")
        else:
            error("Incompatible OS, exiting...")
            exit()
    except:
        info("Incompatible OS, exiting...")

# Set window title
def setTitle(txt):
    system("title "+txt)
from colorama import Fore
from platform import system as osName
from os import system

# Defining colors from each type of output
class clrs:
    Info = Fore.YELLOW
    Error = Fore.RED
    Success = Fore.GREEN
    Ask = Fore.BLUE
    Divisor = Fore.CYAN

# Clear command prompt
def cls():
    if osName() == "Windows":
        system("cls")
    elif osName() == "Linux":
        system("clear")

# Print information
def info(txt):
    try:
        print(clrs.Info+txt+Fore.WHITE)
    except:
        print(txt)

# Return user-response
def ask(txt):
    try:
        return input(clrs.Ask+txt+Fore.WHITE)
    except:
        return input(txt)

# Print error message
def error(txt):
    try:
        print(clrs.Error+txt+Fore.WHITE)
    except:
        print(txt)

# Print success message
def success(txt):
    try:
        print(clrs.Success+txt+Fore.WHITE)
    except:
        print(txt)

# Print separator
def divisor():
    try:
        print(clrs.Divisor+"\n----------------------------------------\n"+Fore.WHITE)
    except:
        print("\n----------------------------------------\n")

# Close the program
def exitScript():
    ask("\nPress enter to close the window...")
    cls()
    exit()
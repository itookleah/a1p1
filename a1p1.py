# assignment 1 part 1

# Leah Vann
# lvann@uci.edu
# 33131498

from pathlib import Path

def view():
    myPath = Path("\ics32")
    for currentPath in myPath.iterdir():
        print(currentPath)


def commands():
    command = input("Please view(L) or quit(Q): \n")
    while command != 'q':
        view()
        command = input("Please view(L) or quit(Q): \n")


if __name__ == "__main__":
    commands()

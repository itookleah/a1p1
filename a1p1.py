# assignment 1 part 1

# Leah Vann
# lvann@uci.edu
# 33131498

from pathlib import Path

def view():
    myPath = Path("C:\ics32")
    for currentPath in myPath.iterdir():
        print(currentPath)


if __name__ == "__main__":
    view()
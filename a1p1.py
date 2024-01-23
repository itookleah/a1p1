# assignment 1 part 1

# Leah Vann
# lvann@uci.edu
# 33131498

from pathlib import Path

def view(directory):
    myPath = Path(directory)

    #print files
    for currentPath in myPath.iterdir():
        if currentPath.is_file():
            print(currentPath)
    
    #print directories
    for currentPath in myPath.iterdir():
        if currentPath.is_dir():
            print(currentPath)




def commands():
    command = input("Please view(L) or quit(Q): \n")
    while command != 'q':
        view("\ics32")
        command = input("Please view(L) or quit(Q): \n")


if __name__ == "__main__":
    commands()

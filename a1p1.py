# assignment 1 part 1

# Leah Vann
# lvann@uci.edu
# 33131498

from pathlib import Path

command = input("View specifed directory([COMMAND] [INPUT] [[-]OPTION] [INPUT]) or quit(Q): \n")

#View (L) or Quit (Q)
command1 = ''
#Input
command2 = ''
#[-]Option
command3 = ''

start = 0
for i, comm in enumerate(command):
    if comm == ' ':
        if not command1:
            command1 = command[start:i]
        elif not command2:
            command2 = command[start:i]
        start = i + 1
if not command3:
    command3 = command[start:]


def view_files(directory):
    myPath = Path(directory)
    for currentPath in myPath.iterdir():
        if currentPath.is_file():
            print(currentPath)
    

def view_directories(directory):
    myPath = Path(directory)
    for currentPath in myPath.iterdir():
        if currentPath.is_dir():
            print(currentPath)


def commands():
    if command1 == 'L':
        if command3 == '-f':
            view_files(command2)
        elif command3 == command3:
            view_files(command2)
            view_directories(command2)


    

if __name__ == "__main__":
    commands()

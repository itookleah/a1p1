# assignment 1 part 1

# Leah Vann
# lvann@uci.edu
# 33131498

from pathlib import Path

command = input("View specifed directory([COMMAND] [INPUT] [[-]OPTION] [INPUT]) or quit(Q): \n")

#View (L) or Quit (Q)
command1 = ''
#Directory name
command2 = ''
#[-]Option
command3 = ''
#input
command4 = ''

dir = Path(command2)

start = 0
for i, comm in enumerate(command):
    if comm == ' ':
        if not command1:
            command1 = command[start:i]
        elif not command2:
            command2 = command[start:i]
        elif not command3:
            command3 = command[start:i]
        else:
            command4 = command[start:i]
        start = i + 1
if not command2 and start < len(command):
    command2 = command[start:]
elif not command3 and start < len(command):
    command3 = command[start:]
elif not command4 and start < len(command):
    command4 = command[start:]

def view_files(directory):
    '''Views files in specified directory'''
    myPath = Path(directory)
    for currentPath in myPath.iterdir():
        if currentPath.is_file():
            print(currentPath)
    

def view_directories(directory):
    '''View folders in specified directory'''
    myPath = Path(directory)
    for currentPath in myPath.iterdir():
        if currentPath.is_dir():
            print(currentPath)


def recursive_directories(directory):
    myPath = Path(directory)
    view_files(directory)
    for item in myPath.iterdir():
        if item.is_dir():
            print(item)
            view_files(item)
            recursive_directories(item)


def create_file():
    new = Path(command2 + command4 + '.dsu')
    new.touch()


def delete_file():
    deleteFile = command2
    if deleteFile.lower().endswith(".dsu"):
        path = Path(deleteFile)
        path.unlink()
        print(deleteFile + ' DELETED')
    else:
        print("File must end with '.dsu'. Please try again.")


def read_file():
    pass


def commands():
    if command1 == 'L':
        if command3 == '-f':
            view_files(command2)
        elif command3 == '-r':
            recursive_directories(command2)
        else:
            view_files(command2)
            view_directories(command2)
    elif command1 == 'C':
        if command3 =='-n':
            create_file()
    elif command1 == 'D':
        delete_file()
    elif command1 == 'R':
        pass


if __name__ == "__main__":
    commands()

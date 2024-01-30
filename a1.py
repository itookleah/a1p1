# assignment 1 part 1

# Leah Vann
# lvann@uci.edu
# 33131498

from pathlib import Path

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


def create_file(directory, name):
    new = Path(directory + name + '.dsu')
    new.touch()


def delete_file(directory):
    deleteFile = directory
    if deleteFile.lower().endswith(".dsu"):
        path = Path(deleteFile)
        path.unlink()
        print(deleteFile + ' DELETED')
    else:
        print("File must end with '.dsu'. Please try again.")
        commands()


def read_file(directory):
    myPath = Path(directory)
    myFile = open(directory, 'r')
    if directory.lower().endswith(".dsu"):
        if myPath.stat().st_size == 0:
            print('EMPTY')
            commands()
        else:
            for i in myFile.readlines():
                print(i)
    else:
        print("File must end in '.dsu'")
        commands()
    myFile.close()


def commands():
    command = input()
    command1 = ''
    command2 = ''
    command3 = ''
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
            create_file(command2, command4)
    elif command1 == 'D':
        try:
            delete_file(command2)
        except FileNotFoundError:
            print("File must be a '.dsu' file. Please try again.")
            commands()
    elif command1 == 'R':
        read_file(command2)


if __name__ == "__main__":
    commands()

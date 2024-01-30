# Assignment 1

# Leah Vann 
# lvann@uci.edu
# 33131498

This program is a simple code that allows the user to view the files in a directory of their choosing along with a few additional commands. 
When the program is initially run the user is prompted to input commands or quit using 'Q'. 
Based on the commands that the user chooses and the directory that is chosen by the user, the code wil output the files/directories chosen. 
If the user wishes to view contents of a folder they must input a single line of code following the format of [COMMAND] [INPUT] [[-]OPTION] [INPUT]. 
For example, "L \ics32 -f" which will only view the files from the folder "ics32"but it will not output the directories/folders that are in ics32.
The current working commands on their own are L, C, D, R. L allows the user to view files of their specified directory.
C allows users to create a .dsu file with a name of their choosing. D allows the user to delete a file as long as it exists.
R allows the user to read a .dsu file's content, but will check if the code is also empty prompting the user to re-input their input.

import os, sys

def subfolder(path, nodes):
    for item in os.listdir(path):
        print("  " * nodes, end="")
        print("- " + item)
        if os.path.isdir(path + "\\" + item):             #re-run the function if its a folder
            subfolder(path + "\\" + item, nodes + 1)
            
def get_tree(path):
    for item in os.listdir(path):
        print(item)
        if os.path.isdir(path + "\\" + item):
            subfolder(path + "\\" + item, 1)
            print("\n")
                    
def path_checker(path):
    if os.path.isdir(path):
        get_tree(path)

    else:
        print("Invalid path")

if len(sys.argv) == 1:
    get_tree(os.getcwd())       #show tree of current directory if no arguments are supplied
else:
    path_checker(sys.argv[1])
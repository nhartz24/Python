# Noah Hartzfeld
# Section 5
# 10/29/2020

import os


# Problem 1


def print_dir_contents(path):
    # str --> nonetype
    # precondition --> str represents a valid path
    # prints the number of files and subdiractories in a directory as well as their names
    subdir = []
    files = []
    

    content = os.listdir(path) # List of all the files and subdir in path
    for item in content:
        item_path = os.path.join(path,item) # full path to item
        if os.path.isdir(item_path):
            subdir.append(item)

        else:
            files.append(item)
            
    print(str(len(files)),'files:')     
    for item in sorted(files):
        print(2 *' ',item)


    print (str(len(subdir)),'subdirectories:')
    for item in sorted(subdir):
        print(2*' ',item)




# Problem 2

def checked_print_dir_contents(path):
    # str --> nonetype
    # prints the number of files and subdiractories in a pdirectory as well as their names or
    # tells if the path is not valid or if the path does not lead to a directory
    try:
        print_dir_contents(path)
    except FileNotFoundError:
        print(path,'is not a valid path.')
    except NotADirectoryError:
        print(path,'is not a directory.')




# Problem 3


def file_stats(path):
    # str --> nonetype
    # prints the number of words and number of lines in a file or tells if the path leads to
    # a directory instead or if the path is not valid
    try:
        x = open(path,"r")
        read = x.read()
        split = read.split()
        acc = 0
        acc2 = 0
        for line in read:
            acc += 1

        for item in split:
            acc2 += 1

        x.close()

        print ('The file sample', path, 'contains', str(acc), 'words on', str(acc2), 'lines')

    except FileNotFoundError:
        print(path,'is not a valid path.')    
    except IsADirectoryError:
        print(path,'is a directory.')



# Problem 4

def find_in_file(path,search):
    # str --> list[int]
    # returns a list of line numbers in which search appears in the path
    x = open(path,"r")
    acc = []
    i = 1
    for line in x:
        if search in line:
            acc.append(i)
            i += 1

    return acc
                  
                    

'''
# 1

def print_dir_contents(path):
    files = []
    subdir =[]

    contents = os.listdir(path)
    for item in contents:
        full_path = os.path.join(path,item)
        if os.path.isdir(full_path):
            subdir.append(item)
        else:
            files.append(item)


    print(len(files), 'files :')
    for char in files:
        print(char)

    print(len(subdir), 'subdirectories :')
    for char in subdir:
        print(char)


def checked_print_contents(path):

    try:
        print_dir_contents(path)
    except FileNotFoundError:
        print("not a valid path")
    except IsADirectoryError:
        print('not a directory')


def file_stats(path):
    x = open(path,'r')
    read = x.read()
    split = read.split()
    lines = 0
    words = 0
    for line in read:
        lines += 1
    for word in split:
        words += 1

      
def find_in_file(path, x):
    x = open(path)
    read = x.read()
    for line in read:
        if x in line:
 '''        

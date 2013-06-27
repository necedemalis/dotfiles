import os

def get_dirlist(path):
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def litter (path):
    list = []
    dirlist = get_dirlist (path)
    for f in dirlist:
        new_path = os.path.join (path, f)
        if os.path.isfile(new_path):
            list.append(new_path)
        elif os.path.isdir (new_path):
            litter (new_path)
    return list

def trash_txt ():
    path = os.path.dirname(os.path.abspath(__file__))
    my_file = open ("trash.txt", "w")
    list = litter(path)
    for x in list:
        my_file.write (x)
        my_file.write ("\n")


trash_txt()

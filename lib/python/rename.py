import re
import os

os.chdir('/home/joecool/lib/python/project_euler/')
def rename():
    for filename in os.listdir('.'):
        if filename.endswith('.py'):
            if len(filename[:-3]) == 8:
                print (filename)
                a = ''.join(["problem0",filename[-4:]])
                print(a)
                os.rename(filename,a)

with open ('/home/joecool/names.txt') as a_text:
    for line in a_text:
        line = line.rstrip()
        res = re.search (r"([0-9]*)\s*([A-Za-z0-9- ]*)",line)
        name = (res.group(2).replace(" ", "_"))
        name = name.lower()
        for filename in os.listdir('.'):
            if filename.endswith('.py'):
                if filename[7:-3] == res.group(1):
                    print(filename)
                    full_name = ''.join(["problem",res.group(1),"-",name,".py"])
                    os.rename(filename,full_name)

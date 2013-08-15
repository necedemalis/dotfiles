import pickle

with open('05.p','rb') as f:
    entry = pickle.load(f)

for i in entry:
    line = ''
    for n in i:
        (x,y) = n
        part = x*y
        line += part
    print(line)

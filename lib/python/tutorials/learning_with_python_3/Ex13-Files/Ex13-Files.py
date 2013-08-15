#1
infile= open ("/home/joecool/test.txt")
outfile=open ("/home/joecool/test2.txt","w")
xs=infile.readlines()
infile.close ()
xs.reverse ()
for x in xs:
    outfile.write (x)
outfile.close()

outfile=open ("/home/joecool/test2.txt")
while True:
    theline=outfile.readline()
    if len(theline)==0:
        break
    print(theline,end="")
outfile.close()

#2
myfile = open ("snake.txt", "r")
while True:
    line=myfile.readline()
    if len(line)==0:
        break
    sp = line.split()
    for x in sp:
        if x == "snake":
            print (line, end="")
        else:
            continue

myfile.close()

#3
infile=open ("alice.txt")
outfile=open("alice2.txt","w")
count =1
txt_count="%05d" % 1
new_line=""
while True:
    line = infile.readline()
    if len(line)==0:
        break
    new_line = txt_count + " " + line
    outfile.write(new_line)
    count += 1
    txt_count= "%05d" % count

infile.close()
outfile.close()

#4
infile=open ("alice2.txt")
outfile=open ("alice3.txt","w")
while True:
    line = infile.readline()
    if len(line)==0:
        break
    sp = line.split()
    line2 = " ".join(sp[1:])
    outfile.write(line2)
    outfile.write ("\n")
infile.close()
outfile.close()

fin=open ('/home/joecool/Dokumente/Python/tp-Ex9-words.txt')
line=fin.readline
#for line in fin:
#	if len(line) >= 20:
#		word = line.strip()
#		print (word)
	

#2
def has_no_e (w):
	e=0
	for x in w:
		if x is "e":
			e=1
	if e==0:
		print (True)
	else: print(False)
#print(has_no_e("aff"))

#2
def print_has_no_e ():
	tex=open ('/home/joecool/Dokumente/Python/tp-Ex9-words.txt')
	line=tex.readline
	l=0
	c=0
	w=0
	w_wo_e=0
	p=0
	for line in tex:
		while l < len(line):
			if line[c]!="e":
				c+=1
			l+=1
		if c == len(line):
			word = line.strip()
			print (word)
			w_wo_e+=1
			c=0
			l=0
		else:
			c=0
			l=0
		w+=1
	p=100/(w/w_wo_e)
	print ("The list (in total {1} words) contains {0} words without the letter 'e', which is a percentage of {2}%.".format(w_wo_e,w,p))
#print_has_no_e()

#3
def print_has_no (x):
	tex=open ('/home/joecool/Dokumente/Python/tp-Ex9-words.txt')
	line=tex.readline
	l=0
	c=0
	fc=0
	w=0
	w_wo_e=0
	p=0
	let_str =""
	for line in tex:
		while l < len(line):
			for y in x:
				if line[l]==y:
					fc+=1
			if fc ==0:
				c+=1
			l+=1
		if c == len(line):
			word = line.strip()
			print (word)
			w_wo_e+=1
			c=0
			l=0
			fc=0
		else:
			c=0
			l=0
			fc=0
		w+=1
	p=100/(w/w_wo_e)
	if len(x)>1:
		let="letters"
		for a in x:
			let_str= let_str + " " + "'"+a+"'"
	else:
		let="letter"
		let_str= x
	print ("The list (in total {1} words) contains {0} words without the {4} {3}, which is a percentage of {2}%.".format(w_wo_e,w,p,let_str,let))
#print_has_no(("a","e","i"))

#6
def is_abecedarian ():
	tex=open ('/home/joecool/Dokumente/Python/tp-Ex9-words.txt')
	line=tex.readline
	l=1
	c=0
	w=0
	w_wo_e=0
	p=0
	for line in tex:
		while l < len(line):
			o=(ord(line[l]))-1
			if o == ord(line[l-1]):
				c+=1
			l+=1
		if c == len(line)-2:
			word = line.strip()
			print (word)
			w_wo_e+=1
			c=0
			l=1
		else:
			c=0
			l=1
		w+=1
	p=100/(w/w_wo_e)
	print ("The list (in total {1} words) contains {0} words that are abecedarian, which is a percentage of {2}%.".format(w_wo_e,w,p))
#is_abecedarian()

#7
def is_three_con_letters (x):
	l=0
	while l < len (x)-1:
		if x[l] == x[l+1]:
			if len (x) >= l+6:
				if x[l+2]==x[l+3] and x[l+4] == x[l+5]:
					return True
				else:
					return False
			else:
				return False
		else:
			l+=1
#is_three_con_letters("hhsspp")
#7
def find_three ():
	tex=open ('/home/joecool/Dokumente/Python/tp-Ex9-words.txt')
	line=tex.readline
	for line in tex:
		if is_three_con_letters (line):
			print (line)
#find_three()

#8
def is_nr_palindromic ():
	for x in range (100000, 1000000):
		s1=str(x)
		n1=s1[2:6]
		if n1[0]==n1[3] and n1[1]==n1[2]:
			y1=x+1
			s2=str(y1)
			n2=s2[1:6]
			if n2[0]==n2[4] and n2[1]==n2[3]:
				y2=x+2
				n3=str(y2)
				if n3[1]==n3[4] and n3[2]==n3[3]:
					y3=x+3
					n4=str(y3)
					if n4[0]==n4[5] and n4[1]==n4[4] and n4[2]==n4[3]:
						print (x)
#is_nr_palindromic

#9
def are_reversed (dif):
	child=0
	count=0
	while True:
		mother=daughter+dif
		if child==mother[::-2]:
			count=count+1
			

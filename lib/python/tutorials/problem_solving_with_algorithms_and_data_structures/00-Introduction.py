def squareroot(n):
    root = n/2
    for i in range(20):
        root = (1/2) * (root + (n/root))
    return root


#Shakespeare Äffchen
import random
def gen1(length):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(length):
        res = res + alphabet[random.randrange(27)]

    return res

def score(goal,teststring):
    numsame = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numsame += 1
    return numsame / len(goal)

def main():
    goalstring = "methinks it is like a weasel"
    newstring = gen1(28)
    best = 0
    newscore = score(goalstring,newstring)
    while newscore <1:
        newstring = gen1(28)
        print (newstring)


#Fraction class
def gcd(m,n):
    while m%n !=0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    """Fraction class"""

    def __init__(self,top,bottom):
        if isinstance(top,int) == False:
            raise ValueError ("Numerator is not an integer")
        if isinstance(bottom,int) == False:
            raise ValueError ("Denumerator is not an integer")
        common = gcd(top,bottom)
        self.num = top//common
        self.den = bottom//common

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def __repr__(self):
        return "Fraction(num:{}, den:{})".format(self.num,self.den)

    def __eq__(self,other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum
    
    def __ne__(self, other): #!=
        firstnum = self.num/self.den
        secondnum = other.num/other.den
        return firstnum != secondnum
        pass
    
    def __lt__(self, other): #<
        firstnum = self.num/self.den
        secondnum = other.num/other.den
        return firstnum < secondnum
    
    def __le__(self, other): #<=
        firstnum = self.num/self.den
        secondnum = other.num/other.den
        return firstnum <= secondnum
    
    def __gt__(self, other): #>
        firstnum = self.num/self.den
        secondnum = other.num/other.den
        return firstnum > secondnum
    
    def __ge__(self, other): #>=
        firstnum = self.num/self.den
        secondnum = other.num/other.den
        return firstnum >= secondnum

    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den*otherfraction.den
        return Fraction(newnum,newden)

    def __sub__(self,otherfraction):
        newnum = self.num*otherfraction.den - self.den*otherfraction.num
        newden = self.den*otherfraction.den
        return Fraction(newnum,newden)
    
    def __mul__(self,otherfraction):
        newnum = self.num*otherfraction.num
        newden = self.den*otherfraction.den
        return Fraction(newnum,newden)

    def __truediv__(self,otherfraction):
        newnum = self.num*otherfraction.den
        newden = self.den*otherfraction.num
        return Fraction(newnum,newden)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

f1 = Fraction(1,-2)
print(repr(f1))
f2 = Fraction(1,4)
print(f1!=f2)
f3= f1/f2
print(f3)

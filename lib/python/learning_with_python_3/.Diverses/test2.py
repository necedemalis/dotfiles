julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")

(name, surname, b_year, movie, m_year, profession, b_place) = julia

bob = ("Bob","CS")

import math

def f(r):
	c=2*math.pi*r
	a=math.pi*r*r
	return (c,a)

def tup (r):
	a = r[0]
	b = r[1]
	return (b,a)

print (tup(bob))

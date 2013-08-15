from math import sqrt

def main():
    '''Find the triangle numbers that is also pentagonal and hexagonal in $range.'''
    for n in range(2,30000):
        hexagonal = int(n*(2*n-1))
        pentagonal = (sqrt(24*hexagonal+1)+1)/6
        if (pentagonal/int(pentagonal)) == 1.0: # Check if also pentagonal
            triangle = (sqrt(8*hexagonal+1)-1)/2
            if triangle/int(triangle) ==1.0: # Check if also triangle
                   print(hexagonal)

if __name__ == '__main__':
    main()

def number_spiral_diagonals(spiral):
    '''Find the sum of the numbers on the diagonals in a $spiral by $spiral spiral.'''

    spiral = (spiral-1)//2
    position = 1; summe = 1; additor=0
    for i in range(spiral):
        additor += 2
        for i in range(4):
            position += additor
            summe += position
    print(summe)

number_spiral_diagonals(1001)

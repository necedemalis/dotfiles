def lattice_path(max):
    '''Find number of possible lattice paths (move right and down) through a $max*$max grid.'''

    max = max + 1
    liste0 = [1]
    liste1 = [1]
    matrix = []

    #generating lists
    for i in range(max-1):
        liste0.append(1)
        liste1.append(0)
    for i in range(max):
        if i == 0:
            matrix.append(liste0)
        else:
            matrix.append(liste1)

    #adding together numbers of paths to each point in lattic (http://www.robertdickau.com/lattices.html)
    for row in range (0,max-1):
        sum = 1
        for number in range (1, max):
            sum += matrix[row][number]
            matrix[row+1][number] = sum

    print('There are {0} possible routes through a {1}x{1} grid.'.format(matrix[-1][-1],max-1))


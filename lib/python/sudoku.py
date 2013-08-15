input = [("a2",5), ("a4",8),("a6",6), \
         ("b1",6), ("b4",9),("b6",3), \
         ("c1",1), ("c3",8),("c8",4), \
         ("d7",6), ("d8",7), \
         ("e3",2), ("e6",7), \
         ("f7",1), ("f8",8), \
         ("g1",3), ("g3",4),("g8",2), \
         ("h1",2), ("h4",7),("h6",9), \
         ("i2",7), ("i4",5),("i6",4)] \



#input = [("a1",8), ("a3",7),("a5",6),("a7",4),("a9",1), \
         #("b2",6), ("b7",3), \
         #("c4",7), ("c6",8), \
         #("d1",6), ("d5",2),("d9",3), \
         #("e4",3), ("e6",5), \
         #("f1",2), ("f5",4),("f9",7),  \
         #("g4",1), ("g6",9), \
         #("h2",8), ("h8",7), \
         #("i1",5), ("i3",1),("i5",7),("i7",6),("i9",2)] \

class square():
    """Docstring for square """

    def __init__(self,columnrange,linerange,square_fields={}):
        self.columnrange = columnrange
        self.linerange = linerange
        self.square_fields = square_fields.copy()

    def find_fields(self,lines):
        for line in range (1,len(lines)+1):
            if line >= self.linerange and line <= self.linerange + 2:
                for column in lines[line]:
                    if ord(column) >= ord(self.columnrange) and ord(column)<= ord(self.columnrange) + 2:
                        self.square_fields[column,line]= lines[line][column]

    def number(self):
        self.number = self.square_fields[self.column,self.line]
        return self.number

class cube():

    def __init__(self,column,line,cube_fields={}):
        self.column = column
        self.line = line
        self.cube_fields = cube_fields.copy()

    def find_fields(self,lines):
        for line in range (1,len(lines)+1):
            if line == self.line:
                for column in lines[line]:
                    if ord(column) == ord(self.column):
                        self.cube_fields[column,line]= lines[line][column]

    def number(self):
        self.number = self.cube_fields[self.column,self.line]
        return self.number

    def position(self):
            return (self.column,self.line) 

    def possible_numbers(self,n):
        self.possible_numbers = n


def make_lines(input):
    d = {i:0 for i in "abcdefghi"}
    lines_list = ["dummy"]
    for i in range(1,10):
        lines_list.append(d.copy())
    
    for i in input:
        pos, number = i
        line = int(pos[1])
        column = pos[0]
        lines_list[line][column] = number
    
    return lines_list
def make_columns(input):
    d = {i:0 for i in range(1,10)}
    columns_list = ["dummy"]
    for i in range(1,10):
        columns_list.append(d.copy())
    
    for i in input:
        pos, number = i
        column = ord(pos[0])-96
        line = int(pos[1])
        columns_list[column][line] = number
    
    return columns_list
def make_squares(lines):
    squares = ["dummy"]
    for i in range(1,9,3):
        for n in range(1,9,3):
            squares.append(square(chr(96+n),i))

    for i in range(1,10):
        squares[i].find_fields(lines)

    return squares
def make_cubes(lines):
    cubes = ["dummy"]
    for i in range(1,10):
        for n in range(1,10):
            cubes.append(cube(chr(96+n),i))

    for i in range(1,len(cubes)):
        cubes[i].find_fields(lines)

    return cubes

def main(input):
    summe = 0

    lines = make_lines(input)
    columns = make_columns(input)
    squares = make_squares(lines)
    cubes = make_cubes(lines)

    #Seek Possible Numbers List
    for i in range (1,len(cubes)):
        if cubes[i].number() == 0:
            cubes[i].possible_numbers(list(range(1,10)))
        else:
            cubes[i].possible_numbers([])


    #Los geht's!
    #while summe < 80:
    for i in range(1,15):
        summe = 0

        #Lines
        for i in range (1,len(cubes)):
            if cubes[i].number == 0:
                for column in lines[cubes[i].line]:
                    number = lines[cubes[i].line][column]
                    if number in cubes[i].possible_numbers:
                        cubes[i].possible_numbers.remove(number)

        #Columns
        for i in range (1,len(cubes)):
            if cubes[i].number == 0:
                for line in columns[ord(cubes[i].column)-96]:
                    number = columns[ord(cubes[i].column)-96][line]
                    if number in cubes[i].possible_numbers:
                        cubes[i].possible_numbers.remove(number)

        #Squares
        for i in range (1,len(cubes)):
            for square in range(1,10):
                if ord(cubes[i].column) >= ord(squares[square].columnrange) and ord(cubes[i].column) <= ord(squares[square].columnrange) +2:
                    if cubes[i].line >= squares[square].linerange and cubes[i].line <= squares[square].linerange + 2:
                        for key in squares[square].square_fields:
                            number = squares[square].square_fields[key]
                            if number in cubes[i].possible_numbers:
                                cubes[i].possible_numbers.remove(number)


        #Look for exclusives per square
        ###Squares
        for i in range(1,len(squares)):
            sq_list = [] #= all cubes in 1 square
            test_possibles_list = []
            one_time = 0
            for keys in squares[i].square_fields:
                for cube in range (1,len(cubes)):
                    for key in cubes[cube].cube_fields:
                        if keys == key:
                            sq_list.append ((cubes[cube].column,cubes[cube].line,cubes[cube].possible_numbers))

            for cube in range(len(sq_list)):
                if len(sq_list[cube][2]) != []:
                    for n in sq_list[cube][2]:
                        test_possibles_list.append(n)
            for number in test_possibles_list:
                if test_possibles_list.count(number) == 1:
                    one_time = number
            for z in range(len(sq_list)):
                if one_time in sq_list[z][2]:
                    for cube in range (1,len(cubes)):
                        for key_cube in cubes[cube].cube_fields:
                            if key_cube[0] == sq_list[z][0] and key_cube[1] == sq_list[z][1]:
                               cubes[cube].possible_numbers = [one_time]

        ###Columns
        for cube in range(1,len(cubes)):
            one_time = 0
            test_possibles_list = []
            if cubes[cube].possible_numbers != []:
                for c in range(1,len(cubes)):
                    if cubes[c].possible_numbers != [] and cubes[c].column == cubes[cube].column:
                            for possibles in cubes[c].possible_numbers:
                                test_possibles_list.append(possibles)

            for number in test_possibles_list:
                if test_possibles_list.count(number) == 1:
                    one_time = number

            if one_time in cubes[cube].possible_numbers:
                   cubes[cube].possible_numbers = [one_time]

            ###Lines


        #Find list with 1 number
        for i in range (1,len(cubes)):
            if len(cubes[i].possible_numbers) == 1:
                #print(cubes[i].column,cubes[i].line,cubes[i].possible_numbers)

                #Cube Entry
                for key in cubes[i].cube_fields:
                    c,l = key
                    number = cubes[i].possible_numbers.pop()
                    cubes[i].cube_fields[key] = number

                #Line Entry
                for column in lines[l]:
                    if column == c:
                        lines[l][column] = number
                        pass

                #Column Entry
                for line in columns[ord(c)-96]:
                    if line == l:
                        columns[ord(c)-96][line] = number
                        pass

                #Square Entry
                for square in range(1,10):
                    for key in squares[square].square_fields:
                        if key[0] == c and key[1] == l:
                            squares[square].square_fields[key] = number


        #How many finished?
        for i in range (1,len(cubes)):
            if cubes[i].possible_numbers == []:
                summe +=1
        #print(summe)

    sudoku = "\n-------------\n|"
    for cube in range(1,len(cubes)):
        for key in cubes[cube].cube_fields:
            sudoku += str(cubes[cube].cube_fields[key])
        if cube%3 == 0:
            sudoku += "|"
        if cube%27 == 0:
            sudoku += "\n-------------"
        if cube%9 == 0 and cube <81:
            sudoku += "\n|"
    print (sudoku)


if __name__ == '__main__':
    from datetime import datetime
    now = datetime.now()
    main(input)
    print(datetime.now() - now)

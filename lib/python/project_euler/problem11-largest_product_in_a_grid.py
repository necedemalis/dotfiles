'''Greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the problem11_grit.txt grid.'''

matrix = []
highest = ()

with open('problem11_grit.txt',encoding='utf-8') as a_file:
    for line in a_file:
        row = tuple(line.split())
        matrix.append(row)

for row in range(len(matrix)):
    for number in range(len(matrix[row])):
        if row >= 3: #up
            sum = 1
            for i in range(4):
                sum *= int(matrix[row-i][number])
            if sum > highest:
                highest = sum
            if number >= 3: #diagonal-left-up
                sum = 1
                for i in range(4):
                    sum *= int(matrix[row-i][number-i])
                if sum > highest:
                    highest = sum
            if number <=len(matrix[row])-4: #diagonal-right-up
                sum = 1
                for i in range(4):
                    sum *= int(matrix[row-i][number+i])
                if sum > highest:
                    highest = sum
        if row <= len(matrix)-4: #down
            sum = 1
            for i in range(4):
                sum *= int(matrix[row+i][number])
            if sum > highest:
                highest = sum
            if number >= 3: #diagonal-left-down
                sum = 1
                for i in range(4):
                    sum *= int(matrix[row+i][number-i])
                if sum > highest:
                    highest = sum
            if number <=len(matrix[row])-4: #diagonal-right-down
                sum = 1
                for i in range(4):
                    sum *= int(matrix[row+i][number+i])
                if sum > highest:
                    highest = sum
        if number >= 3: #left
            sum = 1
            for i in range(4):
                sum *= int(matrix[row][number-i])
            if sum > highest:
                highest = sum
        if number <=len(matrix[row])-4: #right
            sum = 1
            for i in range(4):
                sum *= int(matrix[row][number+i])
            if sum > highest:
                highest = sum

print(highest)

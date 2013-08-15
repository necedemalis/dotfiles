import os

def sum_down(upper_line,lower_line):
    '''Sums lower line in triangle with upper line and returns a list with higher of both possible numbers.'''
    num1 = 0; num2 = 0
    new_line = []
    for i in range(len(upper_line)):
        num1 = upper_line[i] + lower_line[i]
        num2 = upper_line[i] + lower_line[i+1]
        new_line.append(max(num1,num2))
    return new_line

def __main__():
    '''Find the maximum total from top to bottom of the triangle in problem18_triangle.txt.'''
    triangle_list = []
    with open (''.join([os.getcwd(),"/problem67-triangle.txt"])) as a_file:
        for line in a_file:
            temp_list = []
            for digit in line.rstrip().split():
                temp_list.append(int(digit))
            triangle_list.append(temp_list)


    triangle_list.reverse()
    lower_line = triangle_list[0]
    line = 1
    while len(lower_line) > 1:
        lower_line = sum_down (triangle_list[line],lower_line)
        line += 1

    print(lower_line[0])

if __name__ == '__main__':
    __main__()

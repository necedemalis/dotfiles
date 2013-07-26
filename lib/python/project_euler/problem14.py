def longest_collatz_seq(highest):
    number = 2
    num_dict = {}

    while number <= highest:
        if number not in num_dict:
            n = number
            num_list = []
            while n != 1:
                if n not in num_dict:
                    if n%2 == 0:
                        n = int(n/2)
                    else:
                        n = 3*n + 1
                    num_list.append(n)
                    num_dict[number] = len(num_list)
                else:
                    num_dict[number] = (len(num_list) + num_dict[n])
                    break
            number += 1

    sorted_list = []
    for a,b in list(num_dict.items()):
        (a,b) = (b,a)
        sorted_list.append((a,b))
    sorted_list.sort()
    print('The starting number {0} produces the longest chain: {1}.'.format(sorted_list[-1][1],sorted_list[-1][0]))

from datetime import datetime
startTime = datetime.now()
longest_collatz_seq(1000000)
print(datetime.now()-startTime)

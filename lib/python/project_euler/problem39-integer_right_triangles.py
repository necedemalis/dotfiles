'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?
'''

def find_pythagorean_triples(m,n,k):
    '''Find pythagorean triples.'''
    a = k*(m**2-n**2)
    b = k*(2*m*n)
    c = k*(m**2+n**2)
    if a > b:
        return ((a,b,c),sum([a,b,c]))
    else:
        return ((b,a,c),sum([a,b,c]))

def main():
    highest = 0
    highest_perimeter = 0
    triples_set = set()
    triples_dict = {}
    for m in range(2,25):
        for n in range(1,m-1):
            for k in range(1,10):
                pythagorean_tripel = find_pythagorean_triples(m,n,k)
                if pythagorean_tripel[1] <= 1000:
                    triples_set.add(pythagorean_tripel)
    for tripel in triples_set:
        if tripel[1] in triples_dict:
            triples_dict[tripel[1]] += 1
        else:
            triples_dict[tripel[1]] = 1
    for key in triples_dict:
        if triples_dict[key] > highest:
            highest = triples_dict[key]
            highest_perimeter = key

    print (highest_perimeter)

if __name__ == '__main__':
    main()

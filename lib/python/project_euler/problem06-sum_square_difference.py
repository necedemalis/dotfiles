def sum_sq_diff(n):
    summe = 0
    sum_sq = 0
    for i in range(n+1):
        sum_sq += i**2
        summe += i
    summe = summe**2
    return summe - sum_sq

print(sum_sq_diff(100))

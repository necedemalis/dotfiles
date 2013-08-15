def gen_months_list():
    '''Generates tuple with dictionary {month: number of days} for (year, leap year).'''

    months = {}
    for i in range(1,13):
        if i == 2:
            months[i] = 28
        elif i == 4 or i == 6 or i == 9 or i == 11:
            months[i] = 30
        else:
            months[i] = 31
    months_leap_year = months.copy()
    months_leap_year[2] += 1
    return (months, months_leap_year)

def __main__(first_year,last_year):
    '''Counts how many Sundays fell on the first of the month during inclusive $first_year and $last_year.'''

    (months,months_leap_year) = gen_months_list()
    days = sum(months.values())+1 # 1.Jan 1901
    sunday_sum = 0

    for year in range (first_year,last_year+1): #100 Jahre
        if year%4 == 0 or (year%100 == 0 and year%400 == 0):
            months_per_year = months_leap_year
        else:
            months_per_year = months
        for month in months_per_year:
            if days%7 == 0:
                sunday_sum += 1
            days += months[month]

    print('"{0}" sundays fell on the first of the month during the months from Jan. {1} to Dec. {2}.'.format(sunday_sum, first_year,last_year))

if __name__ == '__main__':
    __main__(1901,2000)

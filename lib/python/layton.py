for multiplicand in range (1, 9):
    for multiplicator in range (123,877):
        if str(multiplicand) not in str(multiplicator) \
        and len(str(multiplicator)) == len(set(str(multiplicator))) \
        and "0" not in str(multiplicator) and "9" not in str(multiplicator):
            product = multiplicator*multiplicand
            x= True
            for i in str(product):
                if i in str(multiplicator) or i == str(multiplicand) or str(product).count(i) >= 2 \
                or "0" in str(product) or "9" in str(product) or len(str(product)) != 4:
                    x = False
            if x == True:
                print(product, multiplicator, multiplicand)

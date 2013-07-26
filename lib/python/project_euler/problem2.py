def fibonacci(max):
        a,b = 0,1
        while a < max:
            yield a
            a,b = b, a+b

gen = fibonacci(4000000)
a_list = [i for i in gen if i%2 == 0]
print(sum(a_list))

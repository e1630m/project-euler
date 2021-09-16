def fib(n=int(4e6)):
    a, b = 1, 2
    t = 2
    while 1:
        a, b = b, a + b
        if b > n:
            return t
        if b % 2 == 0:
            t += b


print(fib())

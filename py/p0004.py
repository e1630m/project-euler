def pal(n=999):
    max_pal = 9
    a = n
    s = 10 ** (len(str(n)) - 1)
    while a >= s:
        if a % 11 == 0:
            b, div = n, 1
        else:
            b, div = n - n % 11, 11
        while b >= a:
            prod = a * b
            sprod = str(prod)
            if prod <= max_pal:
                break
            if sprod == sprod[::-1]:
                max_pal = prod
            b -= div
        a -= 1
    return max_pal


print(pal())

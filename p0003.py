def pfactor(n=600851475143):
    i, div = 2, n
    while i ** 2 <= div:
        if div % i:
            i += 1
        else:
            div //= i
    return div


print(pfactor())
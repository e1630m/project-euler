def sieve(comp={}, i=2):
    while 1:
        if i not in comp:
            comp[i * i] = [i]
            yield i
        else:
            for p in comp[i]:
                comp.setdefault(p + i, []).append(p)
            del comp[i]
        i += 1


def nth_prime(n=10001):
    for i, p in enumerate(sieve()):
        if i == n - 1:
            return p


print(nth_prime())

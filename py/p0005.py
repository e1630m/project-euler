def count_pfactors(n):
    counts = {i: 0 for i in range(1, n + 1)}
    i, div = 2, n
    while i ** 2 <= div:
        if div % i:
            i += 1
        else:
            counts[i] += 1
            div //= i
    counts[div] += 1
    return counts


def smallest_multiple(n):
    factors = {i: 0 for i in range(1, n + 1)}
    for i in range(1, n + 1):
        for k, v in count_pfactors(i).items():
            if factors[k] < v:
                factors[k] = v
    prod = 1
    for i in [k ** v for k, v in factors.items() if v]:
        prod *= i
    return prod


print(smallest_multiple(20))

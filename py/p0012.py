def sprime(n, memo):
    try:
        return memo[n]
    except KeyError:
        for i in range(2, int(n**0.5 + 1)):
            if not n % i:
                memo[n] = i
                return i
        memo[n] = n
        return n


def get_factors(n, memo):
    factors, prime = [], 2
    while n >= prime:
        prime = sprime(n, memo)
        if n >= prime:
            n //= prime
            factors.append(prime)
    return factors


def count_divisors(factors):
    prod = 1
    for v in [factors.count(u) + 1 for u in list(set(factors))]:
        prod *= v
    return prod


def get_tnum(n):
    return (n**2 + n) // 2


memo, i, triangle = {}, 1, get_tnum(1)
while count_divisors(get_factors(triangle, memo)) < 500:
    i += 1
    triangle = get_tnum(i)
print(get_tnum(i))

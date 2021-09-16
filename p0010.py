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

sum_primes = 0
limit = int(2e6)
for p in sieve():
    if p >= limit:
        break
    sum_primes += p
print(sum_primes)

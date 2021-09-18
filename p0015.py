def prod(end, start=2, ans=1):
    for i in range(start, end):
        ans *= i
    return ans


def comb(n):
    r, c = n
    return prod(r + c + 1, r + 1) // prod(r + 1)


lattice = (20, 20)
print(comb(lattice))

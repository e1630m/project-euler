def sqrd_sum(n=100):
    return int((2 * n + 1) * (n + 1) * n / 6)


def sum_sqrd(n=100):
    return int((0.5 * n * (n + 1))**2)


print(sum_sqrd() - sqrd_sum())

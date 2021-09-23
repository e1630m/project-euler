n = 1000
for a in range(n // 3, 0, -1):
    for b in range(n // 2, a, -1):
        c = n - a - b
        if a**2 + b**2 == c**2:
            print(a * b * c)

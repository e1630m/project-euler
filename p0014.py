def collatz(n, memo={}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    if n % 2:
        tmp = n * 3 + 1
    else:
        tmp = n // 2
    memo[n] = collatz(tmp) + 1
    return memo[n]


longest = idx = 0
for i in range(int(1e6)):
    candidate = collatz(i)
    if candidate > longest:
        longest = candidate
        idx = i
print(idx, longest)

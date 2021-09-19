from time import perf_counter_ns


def gsum(n, d):
	q, r = divmod(n, d)
	return d * q * (q + 1) // 2 if r else d * q * (q - 1) // 2

n = 1000
iterations = int(1e6)

start = perf_counter_ns()
for _ in range(iterations):
	ans = gsum(n, 3) + gsum(n, 5) - gsum(n, 15)
end = perf_counter_ns()
print(f'result: {ans}, time_elapsed: {end - start}, iterations: {iterations}')

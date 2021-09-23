#include <stdio.h>
#include <time.h>

int gsum(int n, int d);

void main(void)
{
	int n = 1000;
	int iterations = 1000000, i = 1000000;
	int ans;
	clock_t start, end;

	start = clock();
	while (i)
	{
		i--;
		ans = gsum(n, 3) + gsum(n, 5) - gsum(n, 15);
	}
	end = clock();

	printf("result: %d, time_elapsed: %ldus, iterations: %d", ans, end - start, iterations);
}

int gsum(int n, int d)
{
	int q = n / d;
	int r = n % d;
	if (r)
	{
		return d * q * (q - 1) / 2;
	}
	return d * q * (q + 1) / 2;
}
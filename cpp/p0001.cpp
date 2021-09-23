#include <iostream>
#include <ctime>

int gsum(int n, int d);

int main() {
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

	std::cout << "result: " << ans;
	std::cout << ", time_elapsed: " << end - start;
	std::cout << ", iterations: " << iterations;
}

int gsum(int n, int d) {
	int q = n / d;
	int r = n % d;
	if (r)
	{
		return d * q * (q - 1) / 2;
	}
	return d * q * (q + 1) / 2;
}
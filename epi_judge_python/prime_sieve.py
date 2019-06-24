import math
from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n):
    is_prime = [False] + [False] + [True] * (n - 1)
    for i in range(2, math.floor(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i + 1, len(is_prime)):
                if is_prime[j] and j % i == 0:
                    is_prime[j] = False
    return [i for i , a in enumerate(is_prime) if a]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))

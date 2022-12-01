from functools import reduce
from operator import mul


def lcm(nums: list[int]):
    factors = dict()
    for num in nums:
        for k, v in getPrimeFactors(num).items():
            factors[k] = v if k not in factors else int(max(factors[k], v))
    return reduce(mul, [pow(k, v) for k, v in factors.items()], 1)


def getPrimeFactors(n: int) -> dict[int, int]:
    assert n >= 2
    i = 2
    factors = dict()
    while (i * i <= n):
        if (n % i == 0):
            n /= i
            try:
                factors[i] += 1
            except KeyError:
                factors[i] = 1
        else:
            i += 1
    try:
        factors[n] += 1
    except KeyError:
        factors[n] = 1
    return factors

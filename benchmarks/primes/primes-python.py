# Copyright (c) 2019 Princeton University
# Copyright (c) 2016 Ivan Zahariev
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import sys

def main(params):
    """
    standard optimized sieve algorithm to get a list of prime numbers
    """
    n = 10000000

    if n < 2:
        return {'Number of primes found': 0}
    if n == 2:
        return {'Number of primes found': 2}
    # do only odd numbers starting at 3
    if sys.version_info.major <= 2:
        s = range(3, n + 1, 2)
    else:  # Python 3
        s = list(range(3, n + 1, 2))
    # n**0.5 simpler than math.sqr(n)
    mroot = n ** 0.5
    half = len(s)
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m * m - 3) // 2  # int div
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i = i + 1
        m = 2 * i + 3
    res = [2] + [x for x in s if x]
    return {'Number of primes found': len(res)}

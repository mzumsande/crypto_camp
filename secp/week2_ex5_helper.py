import itertools
import math

# P_i = 2^i G
# find smallest i s.th. P_i = G
# (2^i - 1) G = 0 mod N
# 2^i = 1 mod N
# Can solve this if all divisors of N-1 are known: Create a list of all divisors, sort, find smallest i for which
# 2^i = 1 mod N

N=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

# vibe-coded
def all_divisors(prime_factors):
    # Count the multiplicity of each prime
    factor_counts = {}
    for p in prime_factors:
        factor_counts[p] = factor_counts.get(p, 0) + 1
    # For each prime, create a list of its powers: [p^0, p^1, ..., p^e]
    powers = [[p**e for e in range(factor_counts[p] + 1)] for p in factor_counts]
    # Generate the cartesian product of all powers
    divisors = [math.prod(combo) for combo in itertools.product(*powers)]
    return sorted(divisors)

def first_pow2_mod1_divisor(divisors, N):
    for d in divisors:
        if pow(2, d, N) == 1:
            return d
    return None


prime_factors = [2,2,2,2,2,2, 3,149,631,107361793816595537,174723607534414371449,341948486974166000522343609283189] # from Wolfram alpha

res = all_divisors(prime_factors)
print(first_pow2_mod1_divisor(res, N))

#Result: 1809251394333065553493296640760748560200586941860545380978205674086221273349

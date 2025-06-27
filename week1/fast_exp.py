
def fast_exp(g, exp, mod):
    res = 1
    gpow = g % mod
    while (exp > 0):
        if exp & 1:
            res = res * gpow % mod
        gpow = gpow*gpow % mod;
        exp >>= 1
    return res

assert fast_exp(3, 218, 1000) == 489
assert fast_exp(2, 10, 1000) == pow(2, 10, 1000)
assert fast_exp(7, 256, 13) == pow(7, 256, 13)

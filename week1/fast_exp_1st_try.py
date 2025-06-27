
def fast_exp(g, exp, mod):
    # compute binare expansion of exp
    #print(bin(exp)) #would also work...
    bexp = bin_exp(exp)
    # compute powers
    res = 1
    gpow = g % mod
    for i in range(1, len(bexp) + 1):
        if(bexp[-i]) == "1":
            res = res * gpow % mod
        gpow = gpow*gpow % mod;
    #print(f"result of {g}^{exp} mod {mod}: {res}")
    return res


def bin_exp(num):
    bin = ""
    while(num > 0):
        rem = num % 2
        bin = str(rem) + bin
        num = num //2
    return bin

assert fast_exp(3, 218, 1000) == 489
assert fast_exp(2, 10, 1000) == pow(2, 10, 1000)
assert fast_exp(7, 256, 13) == pow(7, 256, 13)

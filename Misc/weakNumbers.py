# ==================================================================================
# The weakness of a number n is defined as the number of positive integers
# smaller than n that have MORE divisors than n. The following script outputs
# the weakness of the weakest numbers in the range [1, n] and the amount of
# numbers in such range that have the specified weakness as a list of two elements,
# where the first element is the weakness and the second element is the amount.
# ==================================================================================

def findNumDivisors(n):
    dct = {}
    k = 2
    while n != 1:
        if n % k == 0:
            dct[k] = dct.get(k, 0) + 1
            n //= k
        else:
            k += 1

    mult = 1
    for key in dct:                         # 12 = 2 x 2 x 3
       mult *= (dct[key] + 1)               # 12 = (2**2) x (3**1)
    return mult                             # number of divisors = multiplication of (exponents + 1)
                                            # number of divisors = (2 + 1) x (1 + 1) = 6
def weakNumbers(n):
    lst = [0, 1]
    for i in range(2, n+1):
        lst.append(findNumDivisors(i))

    cnts = [0] * len(lst)

    for i in range(len(lst)-1, -1, -1):
        for j in range(i-1, -1, -1):
            if lst[j] > lst[i]:
                cnts[i] += 1

    cnts = cnts[1:]                         # remove first index to avoid erroneous
                                            # counting for small examples (0, 1, 2)
    maxi = max(cnts)
    return [maxi, cnts.count(maxi)]

print(weakNumbers(1))                       # expected output: [0, 1]
print(weakNumbers(2))                       # expected output: [0, 2]
print(weakNumbers(4))                       # expected output: [0, 4]
print(weakNumbers(7))                       # expected output: [2, 1]
print(weakNumbers(9))                       # expected output: [2, 2]

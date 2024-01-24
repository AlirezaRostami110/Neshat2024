import gmpy2
import sys

sys.set_int_max_str_digits(5010)

for i in range(10**4999+1, 10**5000, 2) :
    if gmpy2.is_prime(i) :
        print(i)
        break
    else :
        print(i)
        print(False)

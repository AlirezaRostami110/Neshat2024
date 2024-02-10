import sympy
import sys

sys.set_int_max_str_digits(5000)

def is_prime(value):
    limit = int(sympy.Add((sympy.sqrt(value)),1))
    for i in range(2, limit):
        if value % i == 0:
            return False
    return True


def find_prime():
    num = 10**4999 + 1
    while True:
        if is_prime(num):
            return num
        print("failed")
        num += 2

if __name__ == "__main__": 
    print(find_prime())
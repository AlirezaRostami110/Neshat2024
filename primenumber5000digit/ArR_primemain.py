from sympy import isprime
from concurrent import futures
import time

import sys
sys.set_int_max_str_digits(5001)


calibr = False
def generate_prime_number(ls):
    global calibr
    start = ls[0]
    end = ls[1]
    for number in range(start, end, 2):
        if calibr == True:
            return
        if isprime(number):
            calibr = True
            break
    return number
        

def thread_generator(digits, thrds):

    start = 10**(digits-1)+1
    end = 10**10**digits
    size = (end-start)//thrds

    lists = [[i, i+size] for i in range(start, end, size)]
    with futures.ThreadPoolExecutor(max_workers= thrds) as executor:
        results = list(executor.map(generate_prime_number, lists))
    return set(results)

start = time.perf_counter()
print(thread_generator(5000,20))

end = time.perf_counter()

print(round(end -start), 3)

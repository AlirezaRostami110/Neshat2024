import gmpy2

found = False
start = 10**4999 + 1
while not found:
    if gmpy2.is_prime(start):
        found = True
        print(start)
    print("failed")
    start += 2
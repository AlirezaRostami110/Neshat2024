from concurrent import futures
import time

start = time.perf_counter()

def sum_ls(ls):
    return sum(ls)


a  = list(range(1,2401))
n = 4
size = len(a)//n
lists = [a[i:i+size] for i in range(0, len(a), size)]
    

with futures.ThreadPoolExecutor(max_workers=n) as executor:
    results = list(executor.map(sum_ls, lists))

ans = sum(results)


end = time.perf_counter()
print(round(end-start, 3))

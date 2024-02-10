import threading

def sum_sublist(sublist, result):
    result.append(sum(sublist))

def main():
    num_threads = 4
    num_list = [1,2,3,4,5,6,7,8,9,10]
    results = []

    threads = []
    for i in range(num_threads):
        start = i*len(num_list) // num_threads
        end = (i+1)*len(num_list) // num_threads
        t = threading.Thread(target=sum_sublist,args=(num_list[start:end], results))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    
    total_sum = sum(results)
    print("last result is ", total_sum)

if __name__ == "__main__":
    main()
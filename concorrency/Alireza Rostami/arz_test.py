from threading import Thread

n = int(input("Calculatig the sum of numbers from 1 to : "))

num_list = [i for i in range(1,n)]

ans_sum = []

def sumnum(a_list):
    ans_sum.append(sum(a_list))

len_num = len(num_list)

lists = [num_list[i * len_num // 4: (i + 1) * len_num // 4] for i in range(4)]

threads = []

for list in lists:
    my_thread = Thread(target=sumnum, args=(list,))
    my_thread.start()
    threads.append(my_thread)

for thread in threads:
    thread.join()

print(sum(ans_sum))
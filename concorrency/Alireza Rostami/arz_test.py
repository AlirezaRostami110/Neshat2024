# First Code
'''
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
'''

# Second Code
from threading import Thread

n = int(input("Calculatig the sum of numbers from 1 to : "))

num_list = [i for i in range(1,n)]

#Using in list_dividing function
len_num = len(num_list)
divided_lists = []

def list_dividing(n):
    for i in range(n):
        divided_lists.append(num_list[i * len_num // n: (i + 1) * len_num // n])
    return divided_lists

answer_result = 0

def sumnum(a_list):
    global result
    global answer_result
    result = sum(a_list)
    answer_result += result
    return answer_result

# We want to have 4 threads so we choose 4 by the arg of list_dividing func
list_dividing(4)

threads = []

for list in divided_lists:
    my_thread = Thread(target=sumnum, args=(list,))
    my_thread.start()
    threads.append(my_thread)

for thread in threads:
    thread.join()

print("The result is :", answer_result)

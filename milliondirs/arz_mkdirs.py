import os
from time import time

def int_to_persian(num):
    persian_numbers = {
        '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴',
        '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'
    }
    return ''.join(persian_numbers[digit] for digit in str(num))

def create_directories(base_path, count=1000000):
    for i in range(1, count + 1):
        i = i*i
        dir_name = int_to_persian(i)
        path = os.path.join(base_path, dir_name)
        os.makedirs(path, exist_ok=True)

if __name__ == "__main__":
	start_time = time()
	base_path = "."
	create_directories(base_path)
	end_time = time()
	print(f"{round(end_time-start_time,2)} Seconds.")

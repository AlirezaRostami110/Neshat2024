import os
from unicodedata import digit

def num_to_persian(num):
    persian_digits ={
        '0':'۰',
        '1':'۱',
        '2':'۲',
        '3':'۳',
        '4':'۴',
        '5':'۵',
        '6':'۶',
        '7':'۷',
        '8':'۸',
        '9':'۹'
        }
    
    num_str = str(num)
    result = [persian_digits[digit] for digit in num_str]
    return ''.join(result)


def create_directories(path):
    
    if not os.path.exists(path):
        os.makedirs(path)

    for i in range(1, (10**6)+1):
        power = i*i
        name = num_to_persian(power)
        os.makedirs(os.path.join(path, name))


if __name__ == "__main__":
    input_path = input("Enter path: ")
    create_directories(input_path)
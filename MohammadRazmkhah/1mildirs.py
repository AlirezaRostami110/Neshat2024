import os
def number_to_persian(num):
    digits = {
        0: "۰",
        1: "۱",
        2: "۲",
        3: "۳",
        4: "۴",
        5: "۵",
        6: "۶",
        7: "۷",
        8: "۸",
        9: "۹",
    }
    result = ""
    while num > 0:
        digit = num % 10
        result = digits[digit] + result
        num = num // 10
    return result
def create_directories(directoryPath, startNumber, endNumber):
    if not os.path.exists(directoryPath):
        os.makedirs(directoryPath)

    for i in range(startNumber, endNumber+1):
        dirNameEN = i*i
        dirNameFA = number_to_persian(dirNameEN)
        dirPath = os.path.join(directoryPath, dirNameFA)
        os.makedirs(dirPath)

directoryPath = input("Enter the path of directories:")
create_directories(directoryPath,1,10**6)

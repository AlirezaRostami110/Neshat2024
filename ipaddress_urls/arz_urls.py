import re

name = input()
name = name + '/'
spliter = re.split("/+", name)
protocol = spliter[0].replace(':', '')
print('\nProtocol : ', protocol)

i = 1
while i > 0 :
    if i == 1 :
        print('Domain Name : ', spliter[i])
    elif i == 2 :
        print('Folder Structure : ', spliter[i])
    elif i == 3 :
        print('Filename : ', spliter[i])
        break
    i += 1

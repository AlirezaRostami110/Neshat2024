import ipaddress
import random
import secrets

ipv4 = str(ipaddress.IPv4Address(random.getrandbits(32)))
print('\nIPv4 Address : ', ipv4)

IPv6 = str(ipaddress.IPv6Address(random.getrandbits(128)))
print('IPv6 Address : ', IPv6)

list_hex = [secrets.token_hex(1) for i in range(6)]
mac_address = ':'.join(list_hex)
print('MAC Address : ',mac_address, '\n')

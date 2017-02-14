import sys
sys.path.append("..")

import regex

print('regex.find_first("b11111 c22222", "(?P<n>\d+)")')
print(regex.find_first("b11111 c22222", "(?P<n>\d+)"))
print('==================================================')
print('regex.find_first("b11111 c22222", "(?P<n>\d+)", "n")')
print(regex.find_first("b11111 c22222", "(?P<n>\d+)", "n"))
print('==================================================')
print('regex.find_all("b11111 c22222", "(?P<n>\d+)")')
print(regex.find_all("b11111 c22222", "(?P<n>\d+)"))
print('==================================================')
print('regex.find_all("b11111 c22222", "(?P<n>\d+)", "n")')
print(regex.find_all("b11111 c22222", "(?P<n>\d+)", "n"))


#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/swap-case/problem


def swap_case(s):
    new_string = ''
    for i in s:
        if i.islower() == True:
            new_string+=(i.upper())
        elif i.isupper() == True:
            new_string+=(i.lower())
        elif i.isspace() == True:
            new_string+=i
        else:
            new_string+=i
    return new_string
  
  
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

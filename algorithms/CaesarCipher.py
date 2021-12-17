#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/caesar-cipher-1/problem

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    al = 'abcdefghijklmnopqrstuvwxyz'
    shift = 0
    encoded = ''
    for i in range(len(s)):
        let = s[i]
        special = let in "!@#$%^&*()[]{}`'-+?_=,.<>/"
        if not special and not let.isnumeric():
            pos = al.index(let.lower())
            shift = pos + k
        if shift > 25:
            shift %=26
        elif shift < 0:
            shift += 26
        if special or let.isnumeric():
            encoded += let
        elif let.isupper():
            encoded += al[shift].upper()
        else:
            encoded += al[shift]

    return encoded
 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/bon-appetit/problem

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    whole_bill = sum(bill)
    not_eaten = bill.pop(k)
    splited_bill = int(sum(bill)/2)  
    anna_paid = b
    
    if anna_paid == splited_bill:
        print('Bon Appetit')
    else:
        print(anna_paid - splited_bill)
    
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

#!/usr/bin/env python
'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.'''

myarg = input("enter max limit: ")

def multiple_3_or_5(maxlimit):
    counter=0
    for i in range(1, int(maxlimit), 1):
        if i%3==0 and i%15!=0:
            counter+=i
        if i%5==0 and i%15!=0:
            counter+=i
    return(counter)

print(multiple_3_or_5(myarg))

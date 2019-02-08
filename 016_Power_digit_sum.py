'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''
def power_sum(exp):
    sum = 0
    pow = 2 ** int(exp)
    for i in str(pow):
        sum = sum + int(i)
    return(sum)
   
print(power_sum(1000))

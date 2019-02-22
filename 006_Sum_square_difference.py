'''The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

def sum_of_square(max_num):
    sum_of_square = 0
    sq_of_sum = 0
    for n in range(max_num+1):
        sum_of_square+=n**2 
        sq_of_sum+=n
        
    return(sq_of_sum**2-sum_of_square)
    
    
    
print(sum_of_square(100))

'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

# Using algorithm method instead of brute way: https://people.revoledu.com/kardi/tutorial/BasicMath/Prime/Algorithm-PrimeFactor.html

def prime_list(numberr):
    num = int(numberr ** 0.5) 
    prime_numbers=[]
    for i in range(2,num+1):
        if i>=2:
            for im in range(2,i):
                if i%im==0:
                    break
            else:
                prime_numbers.append(i)
    return(prime_numbers)
                
#Iterate over the list of prime numbers
def largest_prime(mynum):
    prime_factors=[]
    for i in prime_list(mynum):
        if mynum % i == 0:
            prime_factors.append(i)
            continue
    return(prime_factors[-1])
        
        
print(largest_prime(600851475143))

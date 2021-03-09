'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.Find the largest palindrome made from the product of two 3-digit numbers.'''

# 3 digits
def palin(x, y):
    largest_palindrome = 0
    z=-1
    print(type(x),type(y),type(z))
    for i in range(x, y, z):
        for j in range(x, y, z):
            prod_arr=[]
            # calculate product of nnn x mmm
            prod = i*j
            # convert number to array to check if product is palindrome
            for xx in str(prod):
                prod_arr.append(int(xx))
            
            # cal rev of string
            rev_prod_arr = []
            for r in range(len(prod_arr),0,-1):
                rev_prod_arr.append(prod_arr[r-1])

            #print(i,j,prod,prod_arr,rev_prod_arr) #print(prod,prod_arr,rev_prod_arr)
            # compare 1st half with rev(2nd half)
            if prod_arr == rev_prod_arr and prod>largest_palindrome:
                largest_palindrome = prod
                min_num=i
                max_num=j
                #print("NISHA",str(prod_arr),i,j)
                
    return largest_palindrome,min_num,max_num

print(palin(999,100))

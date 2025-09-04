def factorial(n):
    if n<0:
        return("invalid entry")
    
    elif n==1:
        return (1)
    
    #recursion
    return (n*factorial(n-1))

n = int(input("Enter a number: "))
factorial_=factorial(n)
try:
    print("%d! = %d"%(n,factorial_))
except:
    print(factorial_)

# n! = n*(n-1)*(n-2)*...*1
# 0! = 1
# 1! = 1
# 2! = 2*1 = 2
# 3! = 3*2*1 = 6
# 4! = 4*3*2*1 = 24
# 5! = 5*4*3*2*1 = 120
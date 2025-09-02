import math

def prime(n):
    if n<=0:
        return("invalid entry")
    
    elif n==1:
        return("not a prime no.")
    
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return("not a prime no.")
    return("prime no.")

n = int(input("Enter a number: "))
print(f"{n} is {prime(n)}")
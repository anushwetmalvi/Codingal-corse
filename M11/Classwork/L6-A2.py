# algorithm for finding all prime numebr up to any given limit.
def SieveOfEratosthenes(num):
    prime = [True for i in range(num + 1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1
    
    for p in range (2, num):
        if prime[p]:
            print(p, end=", ")

num = int(input("Enter an integer- "))
print("FOlowing are the prime number smaller")
print("than or equal to", num)
SieveOfEratosthenes(num)            
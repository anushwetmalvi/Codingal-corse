#Counting the total number of bits
def numberOfBits(n):
    count = 0
    while n:
        count += 1
        n = n >> 1
    return count

n = int(input("Enter a number: "))
print(f"Total number of bits: {numberOfBits(n)}")
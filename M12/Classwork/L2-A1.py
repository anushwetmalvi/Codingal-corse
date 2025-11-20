#check the count of zeros and ones bits in the number we have enterted
def numberOffBits(n):
    ones = 0
    zeroes = 0
    while (n>0):
        if (n & 1) == 1:
            ones += 1
        else:
            zeroes += 1
        n = n >> 1
    print("Number of ones bits:", ones, ", Number of zeroes bits:", zeroes)

number = int(input("Enter a number: "))
numberOffBits(number)      
'''
find and print all number from 1 to 3000 that are both:
1. prime numbers, and
2. palindromic
'''

a = int(input("Enter your number: "))

for num in range(1, a +1):
    c =0
    rev = 0
    temp = num

    # check for prime number
    for i in range(1, temp + 1):
        if temp % i == 0:
            c += 1

    if c == 2:
        # check for palindromic number
        while temp > 0:
            rev = rev * 10 + (temp % 10)
            temp = temp // 10

        if rev == num:
            print(num, end=", ")
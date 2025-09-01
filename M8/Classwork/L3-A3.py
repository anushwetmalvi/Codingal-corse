num = int(input("Enter number to check ? "))

if num > 50:
    print("Number is greater than 50")
    if num % 2 == 0:
        print("and it is even")
    else:
        print("and it is odd")
else:
    print("Number is less than 50")
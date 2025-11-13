# program to check if given number is prime or not
from math import sqrt

number = int(input("Enter a number: "))
print("\n")

# if given number is greather than 1
if number > 1:

    # check if the number is dibvisible from 2 to sqrt(number)
    for i in range(2, int(sqrt(number)) + 1):

        #if divisible by any number it is a non_prime number
        if (number % i) == 0:
            print(f"{number} is a non-prime number")
            break
    else:
        print(f"{number} is a prime number")

else:
    print(f"{number} is a non-prime number")
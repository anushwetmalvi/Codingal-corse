# programa to find lcm of two numbers

#input
largestNumber = int(input("Enter the larger number: "))
smallestNumber = int(input("Enter the smaller number: "))

#finding lcm
number_for_multiply = 0
lcm = 0
while(True):
    number_for_multiply += 1
    multiple = largestNumber * number_for_multiply
    if(multiple % smallestNumber == 0):
        lcm = multiple
        break

print(f"The LCM of the two numbers is: {lcm}")
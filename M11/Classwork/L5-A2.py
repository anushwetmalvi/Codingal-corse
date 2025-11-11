# programa to find HCF/GCD of two numbers

#enter 2 numbers
numberLargest = int(input("Enter the larger number: "))
numberSmallest = int(input("Enter the smaller number: "))

# using Euclidean Algorithm
while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print(f"The HCF/GCD of the two numbers is: {numberLargest}")
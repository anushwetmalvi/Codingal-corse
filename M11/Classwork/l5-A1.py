#Check if the number is palimdrom or not 
#take infrom the user
number = int(input("Enter a number: "))

#store the orignal number for comparison later
original_number = number
reversed_number = 0

# reverse the number
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10
# check if the original number is equal to the reversed number
if original_number == reversed_number:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")
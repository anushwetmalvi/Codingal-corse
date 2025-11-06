# to find factors of user input

# Goes from 1 to number and checks if I divide the nuber . if yes , it is a factor
def print_factors(number):
    print("The factors of", number, "are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

# input from user
number = int(input("Enter a number to find its factors: "))

#calling function
print_factors(number)
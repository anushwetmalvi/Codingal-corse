num = int(input("Enter a number: "))
temp = num
sum = 0
while(num != 0):
    remainder = num % 10 
    sum = sum + remainder**3
    num = num // 10

if sum == temp:
    print(f"{temp} is an Armstrong number")
else:
    print(f"{temp} is not an Armstrong number")
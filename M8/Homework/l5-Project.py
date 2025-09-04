a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

for i in range(20):
    print(a, end=" ")
    a, b = b, a+b
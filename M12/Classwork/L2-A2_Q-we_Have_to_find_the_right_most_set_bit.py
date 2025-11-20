def rightMostSetBit(number):
    if number == 0:
        return 0
    position = 1
    while (number & 1) == 0:
        number = number >> 1
        position += 1
    print("The position of right most set bit is:", position)

number = int(input("Enter a number: "))
rightMostSetBit(number)
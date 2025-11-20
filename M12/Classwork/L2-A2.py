#check weather a bit is a set(1) or not set(0)
def setOrNot(number, n):
    if number & (1 << (n - 1)) == 0:
        print("set it is '1'")
    else:
        print("not set it is '0'")

number = int(input("Enter a number: "))
n = int(input("Enter the position of bit to be checked: "))
setOrNot(number, n)
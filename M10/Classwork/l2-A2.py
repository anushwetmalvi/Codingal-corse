file = open("Coding.txt", "r")
print("reading the first line.....")
print(file.readline())
file.close()

file = open("Coding.txt", "r")
print("reading multiple lines.....")
for i in range(3):
    print(file.readline())
file.close()

file = open("Coding.txt", "r")
print("looping through the lines.....")
for line in file:
    print(line)
file.close()
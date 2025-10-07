file = open('Coding.txt','r')
print(file.read())
file.close()

file = open('Coding.txt','r')
print("\nRead in parts \n")
print(file.read(8))
file.close()

file = open('Coding.txt','a')
file.write("\n hi iam penguin and i am 1 yr old.")
file.close()
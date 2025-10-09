with open("codingal.txt","w") as file:
    file.write("Hi! i am penguin and i am 1 yr old.")

with open("codingal.txt","r") as file:
    data = file.readlines()
    print(data)
    print("Words in the file are.......")
    for line in data:
        word = line.split()
        print(word)
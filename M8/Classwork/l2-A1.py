name = "Penguin" #string datatype
age = 15 #integer datatype
is_student = True #boolean datatype true/false
weight = 38.5 #float datatype

print("Name:", name)
print("data type of name is", type(name))
print("Age:", age)
print("data type of age is", type(age))
print("Is Student:", is_student)
print("data type of is_student is", type(is_student))
print("Weight:", weight)
print("data type of weight is", type(weight))

print("\n After type casting:")
age = str(age)
print(age)
print("data type of age is", type(age))
weight = int(weight)
print(weight)
print("data type of weight is", type(weight))
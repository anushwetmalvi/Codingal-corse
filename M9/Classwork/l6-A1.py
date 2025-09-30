class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"i am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("meow")


class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"i am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("bark")

c = cat("cati", 2)
d = dog("dogi", 3)

for animal in (c, d):
    animal.info()
    animal.make_sound()
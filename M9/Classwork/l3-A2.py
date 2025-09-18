class Student:
    grade = 7
    name = "Anushwet"

    # method 1-
    def intro(self):
        print("Hi I am a student")

    # method 2-
    def details(self):
        print("My name is", self.name)
        print("I am in grade", self.grade)

ob = Student()
ob.intro()
ob.details()                            
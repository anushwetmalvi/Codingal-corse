class robot:
    name = "Robo Xstreme"
    color = "red and white"
    model = "RX100"
    cpu = "Intel i7"
    price = 50000

    def intro(self):
        print("Hi I am a robot.")

    def details(self):
        print("My name is", self.name)
        print("My color is", self.color)
        print("My model is", self.model)
        print("My CPU is", self.cpu)
        print("My price is", self.price)

    def thankyou(self):
        print("Thankyou for seeing my details.")

ob = robot()
ob.intro()
ob.details()
ob.thankyou()
class Computer:

    def __init__(self):
        self.__maxprice = 900 
    
    def sell(self):
        print("selling Price: {}".format(self.__maxprice))

    def setmaxprice(self, price):
        self.__maxprice = price
    
c = Computer()
c.sell()

c.__maxprise = 100
c.sell()

c.setmaxprice(1000)
c.sell()
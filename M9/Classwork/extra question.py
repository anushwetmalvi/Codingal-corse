class a:
    
    def printa(self):
        print ("hi i am clss A")

class b(a):

    def printb(self):
        print("hi i am class b , i am child of class b.")

class c(b):

    def printc(self):
        print("hi am i am the clid of class b .")


a1 = a()
a1.printa()
b1 = b()
b1.printb()
c1 = c()
c1.printc()
class Computers:
    #attribute (vaiables)
    def __init__(self): #self is argument __init__ is special method. it will get call automatically
        print("in init")

    #attribute (methods(functions))
    def config(self): #self is the object which you are passing while calling the function.
        print("i5, 16gb, 1tb")

comp1 = Computers()
comp2 = Computers()

Computers.config(comp1)
Computers.config(comp2)

comp1.config()
comp2.config()
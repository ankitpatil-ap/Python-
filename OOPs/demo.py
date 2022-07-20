class Computer:
    #attribute (vaiables)
    def __int__(self):
        print("init ")
    #attribute (methods(functions))
    def config(self): #self is the object which you are passing while calling the function.
        print("i5, 16gb, 1tb")


comp1 = Computer() #constructor
comp2 = Computer()

#Computer.config(comp1)  #here we call config from computer class and specify object comp1 to run
#Computer.config(comp2)


comp1.config() #calling config as comp1 belong to computer class . this is the standard use of syntax
comp2.config()
#print(type(comp1))
#<class '__main__.Computer'> here computer is our user define class
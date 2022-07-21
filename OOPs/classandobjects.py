class Employee:
    increment = 1.5  # it is class variable which is globally accessible in the class
    no_of_employee = 0  # class variables

    def __init__(self, fname, lname,  # here self is an instance of class
                 salary):  # __init is constructor  and this function is going to run when ever object is created
        self.fname = fname
        self.lname = lname  # self.lname is variables,state, attribute of instance
        self.salary = salary  # these are instance variables
        # self.increment = 1.4
        Employee.no_of_employee += 1  # we can call direct class variable using class name

    def increase(self):
        # self.salary = int(self.salary * Employee.increment)     #this is global class variable call from class employee
        # print(self.salary)
        self.salary = int(self.salary * self.increment)  # this is instance variable call from function using self.

    @classmethod  # this is called decorator it specifies the class methods is here
    def change_increment(cls, amount):  # this is class method it must be next to decorator line here self is not
        # given here we specify cls is a class as argument and amount is other argument or parameter
        cls.increment = amount

    @classmethod
    def from_str(cls, emp_string):  # this is class method as attribute
        fname, lname, salary = emp_string.split("-")  # here string is split using split function
        return cls(fname, lname, salary)


    @staticmethod    #the method which does not take class variable as argument not self instance variable as an argument
    def isopen(day):           #it does take self as an automatic argument; here you specify your own arguments
        if day =="sunday":
            return False
        else:
            return True

print(Employee.no_of_employee)
A = Employee('Ankit', 'Patil', 100000)  # object with parameters A and R are object of class
print(Employee.no_of_employee)
R = Employee('Raghav', 'Patil', 100000)
print(Employee.no_of_employee)
Ankit = Employee.from_str("Ankit-Patil-100000")  # object with input string
'''Whenever we call object though you do not give arguments or parameter to object but
it will still take self as parameter or instance of object by default.'''
print(A.salary)
A.increase()  # object A calls increase function from
print(A.salary)
print(A.fname, R.fname)  # calling  attribute of class using different objects
print(A.__dict__)  # it will print all the variables of instance

# {'fname': 'Ankit', 'lname': 'Patil', 'salary': 210000, 'increment': 1.4}

# A.increment = 2                                                    #this will modify instance to 'A' object
print(A.__dict__)
# {'fname': 'Ankit', 'lname': 'Patil', 'salary': 210000, 'increment': 9}

print(Employee.__dict__)  # this will print all instance and functions of class
# {'__module__': '__main__', 'increment': 1.5, '__init__': <function Employee.__init__ at 0x0000022DE513ECB0>, 'increase': <function Employee.increase at 0x0000022DE513ED40>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}


print(A.salary)

Employee.change_increment(2)
# here we call method using class name as an aurgument which updates its variable and spcify the 2 as an aurgument
A.increase()
print(A.salary)

print(Ankit.fname)
print(Ankit.lname)
print(Ankit.salary)


print(Employee.isopen('monday'))  #static function or method call
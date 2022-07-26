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

    @staticmethod  # the method which does not take class variable as argument not self instance variable as an argument
    def isopen(day):  # it does take self as an automatic argument; here you specify your own arguments
        if day == "sunday":
            return False
        else:
            return True


"""print(Employee.no_of_employee)
A = Employee('Ankit', 'Patil', 100000)  # object with parameters A and R are object of class
print(Employee.no_of_employee)
R = Employee('Raghav', 'Patil', 100000)
print(Employee.no_of_employee)
Ankit = Employee.from_str("Ankit-Patil-100000")  


"""
#Emplyee is superclass


class Programmer(Employee):  # here all functions and methods of Employee class is inherited in Programmer class
    def __init__(self,fname,lname,salary,proglang,exp):
        super().__init__(fname,lname,salary)  #it call init of superclass in this class
        self.proglang = proglang
        self.exp = exp
    def increase(self):
        # self.salary = int(self.salary * Employee.increment+0.2)     #this is global class variable call from class employee
        # print(self.salary)
        self.salary = int(self.salary * self.increment)
        return self.salary


Ankit = Programmer('Ankit', 'Patil', 100000,'Python',5)  # here object of programmer is created with method of employee
print(Ankit.increase())  # fname is the instance of self which is in employee class

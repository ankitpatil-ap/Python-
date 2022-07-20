num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
operator = (input("chose operations +,-,*,/,%: "))

if (operator == "+"):
    print(num1 + num2)
elif (operator == "-"):
    print(num1 - num2)
elif (operator == "*"):
    print(num1 * num2)
elif (operator == "/"):
    print(num1 / num2)
elif (operator == "%"):
    print(num1 % num2)
else:
    print("Invalid Number")
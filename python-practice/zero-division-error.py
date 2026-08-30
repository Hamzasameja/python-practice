try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("The result is:" + str(result))
except ZeroDivisionError:
    print("You cannot divide by zero. Please enter a valid number.")
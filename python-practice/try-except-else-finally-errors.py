try:
    num=int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    print("Great, You entered:" + str(num))
finally:
    print("program completed.")
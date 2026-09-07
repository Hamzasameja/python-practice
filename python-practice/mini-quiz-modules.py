import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2

num1, num2 = generate_question()
print("What is "+ str(num1) + " + " + str(num2) + "?")

answer = int(input("Your answer: "))
correct_answer = num1 + num2

if answer == correct_answer:
    print("Correct!")
else:
    print("Incorrect. The correct answer is: " + str(correct_answer))
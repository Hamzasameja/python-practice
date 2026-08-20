def analyzing_numbers(numbers):
    total = 0
    count_even = 0
    biggest = numbers[0] 

    for num in numbers:
        total = total + num
        if num % 2 == 0:
            count_even = count_even + 1
        if num > biggest:
            biggest = num

    print("Sum:" + str(total))
    print("Count of even numbers:" + str(count_even))
    print("Biggest number:" + str(biggest))

my_numbers = [3, 8, 1, 15, 6, 20]
analyzing_numbers(my_numbers)
def get_even(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = get_even(my_numbers)
print(result)
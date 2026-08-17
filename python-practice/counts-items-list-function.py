def count_greater(numbers, limit):
    count = 0
    for num in numbers:
        if num > limit:
            count = count + 1
    return count

numbers = [3, 8, 1, 15, 6, 20]
result = count_greater(numbers, 5)
print(result)
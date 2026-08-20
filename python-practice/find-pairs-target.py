numbers = [2, 4, 6, 8,]
target = 10

for a in numbers:
    for b in numbers:
        if a + b == target:
            print(str(a) + " + " + str(b) + " = " + str(target))
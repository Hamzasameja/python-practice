list1 = [1, 2, 3]
list2 = [2,3,4]

match_count = 0

for a in list1:
    for b in list2:
        if a == b:
            match_count += 1
            print(str(a) + " matches " + str(b))
print("Total matches: " + str(match_count))
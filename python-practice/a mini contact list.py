def add_person(people, name, age):
    people.append({"name" : name, "age" : age})

def print_all(people):
    for person in people:
        print(person["name"] + " - " + str(person["age"]))


def find_person(people, name):
    for person in people:
        if person["name"] == name:
            return person
    return None

people = []

add_person(people, "Hamza" ,21)
add_person(people, "Ali" ,22)
add_person(people, "Yasmin" ,20)

print("All contacts:")
print_all(people)

print("\nsearching for Ali:")
result = find_person(people, "Ali")
print(result)
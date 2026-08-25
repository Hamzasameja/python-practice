def find_person(people, name):
    for person in people:
        if person["name"] == name:
            return person
    return None

people = [
    {"name": "Hamza", "age": 21},
    {"name": "Ali", "age": 22},
    {"name": "Yasmin", "age": 20}
]

result = find_person(people, "Ali")
print(result)

result2 = find_person(people, "John")
print(result2)  
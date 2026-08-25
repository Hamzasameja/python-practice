def get_adults(people, min_age):
    adults = []
    for person in people:
        if person["age"] >= min_age:
            adults.append(person)
    return adults


people = [
    {"name": "Hamza", "age": 21},
    {"name": "Ali", "age": 22},
    {"name": "Yasmin", "age": 20}
]

result = get_adults(people, 21)
for person in result:
    print(person["name"] + " is an adult.")
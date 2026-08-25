def get_adults(people, min_age):
    adults = []
    for person in people:
        if person["age"] >= min_age:
            adults.append(person)
    return adults
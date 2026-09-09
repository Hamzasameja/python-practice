import json

person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Convert Python object to JSON string
json_string = json.dumps(person)
print(json_string)
print(type(json_string))
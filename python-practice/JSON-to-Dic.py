import json

json_string = '{"name": "John Doe", "age": 30, "city": "New York"}'
person = json.loads(json_string)
print(person)
print(type(person))
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])
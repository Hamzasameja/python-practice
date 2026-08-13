person = {"name": "Hamza", "age": 21, "city": "Jalalpur"}

if "age" in person:
    print("Age is :", str(person["age"]))
else: 
    print("Age not found")

if "email" in person:
    print("Email is :", str(person["email"]))   
else:
    print("Email not found")
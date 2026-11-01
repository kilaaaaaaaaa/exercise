person1 = {
    "first_name": "priskila",
    "last_name": "arum",
    "age" : 18,
    "city" : "bandung"
}

person2 = {
    "first_name": "joko",
    "last_name": "widodo",
    "age" : 60,
    "city" : "solo"
}

person3 = {
    "first_name": "jokowi",
    "last_name": "dodo",
    "age" : 25,
    "city" : "jakarta"
}

people = [person1, person2, person3]

for person in people:
    print(f"name: {person['first_name']} {person['last_name']}")
    print(f"age: {person['age']}")
    print(f"city: {person['city']}\n")
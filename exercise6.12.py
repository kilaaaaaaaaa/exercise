favorite_num = {
    "udin": {
        "age" : 20,
        "numbers" : [7, 8]
    },
    "budi": {
        "age" : 21,
        "numbers" : [3, 4]
    },
    "edo": {
        "age" : 22,
        "numbers" : [5, 6]
    }
}

for name, info in favorite_num.items():
    print(f"name: {name.title()}")
    print(f"age: {info['age']}")
    print(f"numbers: {info['numbers']}\n")
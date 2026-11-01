prompt = "enter your age (enter 'quit' to finish): "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("your ticket is free")
        elif age < 13:
            print("your ticket is $10")
        else:
            print("your ticket is $15")
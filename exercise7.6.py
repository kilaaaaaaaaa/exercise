toping = ""

while toping != 'quit':
    toping = input("enter a pizza toping (enter 'quit' when you are finished): ")
    if toping != 'quit':
        print(f"i will add {toping} to your pizza")

active = True

while active:
    toping = input("enter a pizza toping (enter 'quit' when you are finished): ")
    if toping == 'quit':
        active = False
    else:
        print(f"i will add {toping} to your pizza")

while True:
    toping = input("enter a pizza toping (enter 'quit' when you are finished): ")
    if toping == 'quit':
        break
    else:
        print(f"i will add {toping} to your pizza")
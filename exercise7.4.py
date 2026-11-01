prompt = "enter a pizza toping (enter 'quit' when you are finished): "

while True:
    toping = input(prompt)
    if toping == 'quit':
        break
    else:
        print(f"i will add {toping} to your pizza")
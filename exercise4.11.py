pizzas = ["meat lovers", "cheese", "paperoni"]

friends_pizzas = pizzas[:]

pizzas.append("tuna")
friends_pizzas.append("mushroom")

print("my favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nmy friends favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)
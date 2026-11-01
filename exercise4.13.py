foods = ("chicken", "beef", "pork", "fish", "duck")

print("original menu:")
for food in foods:
    print(food)

foods[0] = "lamb"

foods = ("lamb", "beef", "pork", "fish", "tofu")

print("\nmodified menu:")
for food in foods:
    print(food)
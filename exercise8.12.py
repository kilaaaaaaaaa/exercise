def make_sandwich(*ingredients):
    print("making a sandwich with: ")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich("ham")
make_sandwich("egg", "cheese")
make_sandwich("chicken", "beef", "sausage")
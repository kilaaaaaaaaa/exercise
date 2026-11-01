sandwich_orders = ["chicken", "tuna","beef", "tuna", "cheese", "tuna"]
finished_sandwiches = []

print("we are out of tuna today")

while "tuna" in sandwich_orders:
    sandwich_orders.remove("tuna")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"i made your {current_sandwich} sandwich")
    finished_sandwiches.append(current_sandwich)

print("finished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
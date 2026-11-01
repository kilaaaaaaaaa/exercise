sandwich_orders = ["chicken", "beef", "tuna", "cheese"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"i made your {current_sandwich} sandwich")
    finished_sandwiches.append(current_sandwich)

print("finished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
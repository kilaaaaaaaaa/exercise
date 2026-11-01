current_users = ["udin", "budi", "edo", "doni", "toto"]
new_users = ["UDIN", "joko", "dodi", "EDO", "jono"]

current_user_lower = []

for user in current_users:
    current_user_lower.append(user.lower())
    
for new_user in new_users:
    if new_user.lower() in current_user_lower:
        print(f"username '{new_user}' is already taken. please choose a different username.")
    else:
        print(f"username '{new_user}' is available.")
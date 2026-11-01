favorite_num = {
    "udin": [7, 8],
    "budi": [3, 4],
    "edo": [5, 6],
    "doni": [9, 10],
    "joko": [1, 2]
}

for name, numbers in favorite_num.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")
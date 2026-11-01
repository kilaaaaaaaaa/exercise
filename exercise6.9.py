favorite_places = {
    "udin": ["bali", "lombok", "raja ampat"],
    "budi": ["jepang", "korea", "taiwan"],
    "edo": ["new york", "italy", "australia"]
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"- {place.title()}")
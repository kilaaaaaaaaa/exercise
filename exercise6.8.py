pet1 = {
    "animal" : "cat",
    "owner" : "priskila",
}

pet2 = {
    "animal" : "dog",
    "owner" : "pris",
}

pet3 = {
    "animal" : "bird",
    "owner" : "kila",
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"animal: {pet['animal']}")
    print(f"owner: {pet['owner']}\n")
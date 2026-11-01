favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
    }

people = ["jen", "sarah", "edward", "phil", "budi"]

for person in people:
    if person in favorite_languages:
        print(f"thank you for taking the poll, {person.title()}")
    else:
        print(f"{person.title()}, please take our poll")
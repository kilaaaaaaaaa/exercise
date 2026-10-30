guests = ["one direction", "olivia rodrigo", "sabrina carpenter", "bruno mars", "taylor swift", "justin bieber"]

print("i can only invite two people for dinner")

guest = guests.pop()
print(f"sorry {guest}, i can't invite you to dinner")

guest = guests.pop()
print(f"sorry {guest}, i can't invite you to dinner")

guest = guests.pop()
print(f"sorry {guest}, i can't invite you to dinner")

guest = guests.pop()
print(f"sorry {guest}, i can't invite you to dinner")

print(f"hello {guests[0]}, you are still invited to dinner")
print(f"hello {guests[1]}, you are still invited to dinner")

del guests[0]
del guests[0]

print(guests)
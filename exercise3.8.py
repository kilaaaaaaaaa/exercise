places = ["new york", "italy", "canada", "japan", "korea"]

print("urutan asli :")
print(places)

print("\nurutan alfabet :")
print(sorted(places))

print("\nurutan asli :")
print(places)

print("\nurutan alfabet terbalik :")
print(sorted(places, reverse=True))

print("\nurutan asli :")
print(places)

places.reverse()
print("\n   urutan terbalik :")
print(places)

places.reverse()
print("\nurutan setelah dibalik :")
print(places)

places.sort()
print("\nurutan setelah diurutkan alfabet :")
print(places)

places.sort(reverse=True)
print("\nurutan setelah diurutkan alfabet terbalik :")
print(places)
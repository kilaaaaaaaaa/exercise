cities = ["bandung", "solo", "cimahi", "semarang"]

print(cities[0])

cities[0] = "jogja"
print(cities)

cities.append("karawang")
print(cities)

cities.insert(1, "garut")
print(cities)

del cities[0]
print(cities)

popped_city = cities.pop()
print(cities)
print(popped_city)

cities.remove("jogja")
print(cities)

print(sorted(cities))

cities.sort()
print(cities)

cities.reverse()
print(cities)

print(len(cities))
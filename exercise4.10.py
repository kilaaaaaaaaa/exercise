animals = ["dog", "cat", "rabbit", "hamster", "bird", "fish", "turtle"]

print("the first three items in the list are:")
print(animals[:3])

print("three items from the middle of the list are:")
middle = len(animals) // 2
print(animals[middle-1:middle+2])

print("the last three items in the list are:")
print(animals[-3:])
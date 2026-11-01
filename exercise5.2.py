name = "kila"
age = 18
number = 16
friuts = ["banana", "mango", "grapes"]

print(name == "kila")
print(name != "kila")

print(name.lower() == "kila")
print(name.lower() == "KILA")

print(age == 18)
print(age != 18)
print(age > 10)
print(age < 10)
print(age >= 18)
print(age <= 10)

print(age > 10 and number > 15)
print(age > 10 and number < 10)

print(age > 10 or number > 15)
print(age < 10 or number > 10)

print("banana" in friuts)
print("orange" in friuts)

print("orange" not in friuts)
print("banana" not in friuts)
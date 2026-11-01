cities = {
    "bandung" : {
        "country" : "indonesia",
        "population" : 2500000,
        "fact" : "city of flowers"
    },
    "jakarta" : {
        "country" : "indonesia",
        "population" : 10000000,
        "fact" : "capital city of indonesia"
    },
    "solo" : {
        "country" : "indonesia",
        "population" : 500000,
        "fact" : "city of culture"
    }
}

for city, info in cities.items():
    print(f"city: {city.title()}")
    print(f"country: {info['country']}")
    print(f"population: {info['population']}")
    print(f"fact: {info['fact']}\n")
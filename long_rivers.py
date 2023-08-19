rivers = [
 {"name": "Nile", "length": 4157},
 {"name": "Yangtze", "length": 3434},
 {"name": "Murray-Darling", "length": 2310},
 {"name": "Volga", "length": 2290},
 {"name": "Mississippi", "length": 2540},
 {"name": "Amazon", "length": 3915}
]

for i in range(len(rivers)):
    print(rivers[i]["name"])

total_river_length = 0

for i in range(len(rivers)):
    total_river_length += rivers[i]["length"]
print(total_river_length)


for i in range(len(rivers)):
    if rivers[i]["name"][0] == "M":
        print(rivers[i]["name"])

for i in range(len(rivers)):
    river_length_in_km = rivers[i]["length"] * 1.6
    print(round(river_length_in_km,2))

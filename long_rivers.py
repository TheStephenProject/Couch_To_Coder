rivers = [
 {"name": "Nile", "length": 4157},
 {"name": "Yangtze", "length": 3434},
 {"name": "Murray-Darling", "length": 2310},
 {"name": "Volga", "length": 2290},
 {"name": "Mississippi", "length": 2540},
 {"name": "Amazon", "length": 3915}
]

for river in rivers:
    print(river["name"])

total_river_length = 0
for river in rivers:
    total_river_length += river["name"]
print(total_river_length)


for river in rivers:
    if river["name"][0] == "M":
        print(river["name"])

for river in rivers:
    river_length_in_km = river["length"] * 1.6
    print(round(river_length_in_km,2))

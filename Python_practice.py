# Lists
print("Hello World!")
words = ['hi', 'bye', 'hello', 'goodbye']
print(words[:3])
counties = ["Arapahoe","Denver","Jefferson"]
print(counties[1:3])
counties.append("El Paso")
print(counties)
counties.insert(2, "El Paso")
print(counties)
counties.remove("El Paso")
print(counties)
counties.pop(3)
print(counties)
counties[2] = "El Paso"
print(counties)
counties = ["Arapahoe","Denver","Jefferson"]
counties.insert(1, "El Paso")
counties.pop(0)
print(counties)

# Tuples
counties_tuple = ("Arapahoe","Denver","Jefferson")
print(counties_tuple[:-2])
print(counties_tuple[:2])
print(counties_tuple[:-1])
print(counties_tuple[1:2])

# Dictionaries
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)
voting_data.insert(1, {"county":"El Paso", "registered_voters": 461149})
del voting_data[0]
print(voting_data)
voting_data[1], voting_data[2] = voting_data[2], voting_data[1]
print(voting_data)
voting_data.append({'county': 'Arapahoe', 'registered_voters': 422829})
print(voting_data)


# if
counties = ["Arapahoe","Denver","Jefferson"]
if counties[2] != 'Denver':
    print(counties[1])

"""
score = int(input("What is your test score? "))
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')
"""

# membership operators
counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso are not the list of counties.")

# While loop
x = 0
while x <= 5:
    print(x)
    x = x + 1

# For loop
for county in counties:
    print(county)
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

# Retrieving keys and values from a dictionary
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

# Alternative value retrieval
print(counties_dict["Arapahoe"])

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

# Retrieve key:value pairs\
for key, value in counties_dict.items():
    print(key, value)
for county, voters in counties_dict.items():
    print(county, voters)

# Skill drill
for county, voters in counties_dict.items():
    print(f"{county.title()} has {voters} registered voters!")

# retrieving a dictionary from a list
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

"""
# Format floating decimals in print()
    # f'{value:{width}.{precision}}'
        # with 'thousands' separator as ,
        # f'{value:{width},.{precision}}'

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes.\n"
    f"The total number of votes in the election was {total_votes}.\n"
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)
"""

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.\n")

for region in voting_data:
    print(f'{region["county"]} county has {region["registered_voters"]} registered voters!\n')

# 3.3.1

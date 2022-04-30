# Loops through a dictionary using for loop

# add a key/value pair
# add colour : red
car["colour"] = "red"
print(car)

# remove a key from a dictionary using pop()
car.pop("colour")
print(car)

# clear dictionary using clear()
car.clear()

# loop dictionaries
# print all key names in the dictionary
for x in thisdict:
    print(x)

# print all values in the dictionary
for x in thisdict :
    print(thisdict[x])

# print values to return values in dictionary
for x in thisdict.values()
    print(x)

# use keys() to return the keys of a dictionary
for x in thisdict.keys():
    print(x)

# loop both keys and values using items()
for x, y in thisdict.items():
    print(x, y)

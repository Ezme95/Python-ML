# List is a non-homogeneous data structure that stores the elements in single row
# and multiple rows and columns (mutable)
List represented by []

# Tuple is also a non-homogeneous data structure that stores single row
# and multiple rows and columns (not mutable or cannot change)
Tuple represented by ()

# Set data structure is also non-homogeneous data structure but stores in single row
# data is unique
Set represented by {}

# Dictionary is also a non-homogeneous data structure which stores key value pairs
Dictionary represented by {}


# unpacking a tuple

fruilts = ["apple", "banana", "cherry"]
x, y, z = fruilts

print (x, y, z)

# format can take unlimited number of arguments

a = "strawberries"
b = "apples"
c = "durians"
text = "Sammy likes to eat {}, {} and {}"

print(text.format(a,b,c))

# use index to ensure placeholders are correct
a = "strawberries"
b = "apples"
c = "durians"
text = "Sammy likes to eat {2}, {0} and {1}"

print(text.format(a,b,c))

# use append to add to a string list
fruits = ["apple", "banana", "cherry"]
fruits.append("kiwi")
print(fruits)

# use insert to add to string list
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"yakult")
print(fruits)

# use remove to remove to string list
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)

# use update to add multiple items to a string set
fruits = {"apple", "banana", "cherry"}
more_fruits = {"orange", "mango", "grapes"}
fruits.update(more_fruits)
print(fruits)

#use discard to remove items from a string set
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)


# dictionaries have key:value pairs and are ordered

car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 1964
}
# get the modeL using get()
print(car.get("model"))

# change a value in the dictionary
car["year"] = 1983
print(car.get("year"))

# copy a dictionary
mydict = thisdict.copy()
print(mydict)


Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview


#casting is the specification of the type of variable
x = str(3) # x is string 3
y = int (3) # y is integer 3
z = float(3) # z is floating point 3.0; meaning with decimal point


# retrieving the type of variable
print (type (x))


# data types examples
x = "Hello World"	# str
x = 20	# int
x = 20.5	# float
x = 1j	# complex, "j" symbolises the imaginary part of a complex number
x = ["apple", "banana", "cherry"]	#list => are mutable ; []
x = ("apple", "banana", "cherry")	#tuple => are inmutable; ()
x = range(6)	#range
x = {"name" : "John", "age" : 36}	#dict = ordered holds key value pair
x = {"apple", "banana", "cherry"}	#set => mutable with no duplicated elements
x = frozenset({"apple", "banana", "cherry"})	#frozenset
x = True	#bool
x = b"Hello"	#bytes
x = bytearray(5)	#bytearray
x = memoryview(bytes(5))	#memoryvie

# The following are String functions

# multi line string
a = '''the fat fox and the fat cat were so big,
goodness me how awful was that,
they ended up dead in the ditch'''
print(a)




# python does not have char/character data type
# each single character is a string with length of 1
# a string is also an array
a = "hello world"
# print the second string element (0 = 1 position; 1 = 2nd position)
print(a[1])



# use len() to get length of the string; counts space as well
a = "Hello world"
print(len(a))



# to check or search in a string use "in"
# returns true or false
b = "hello world, how are you, hello to you too"
print("hello" in b)

b = "hello world, how are you, hello to you too"
if "jesus" in b :
    print("yo mama is fat")
else :
    print("yo mama is slim")

# to check or search not in a string use "noy"
# returns true or false
b = "hello world, how are you, hello to you too"
print("hello" in b)

b = "hello world, how are you, hello to you too"
if "jesus" not in b :
    print("yo mama is fat")
else :
    print("yo mama is slim")


# string slicing by specifing the start and end index, separated by a colon
b = "hello world, how are you, hello to you too"
print(b[2:5])

# slice from the start
b = "hello world, how are you, hello to you too"
print(b[:5])

# slide to the end
b = "hello world, how are you, hello to you too"
print(b[2:])

# use negative indexes to start the slide from the end of the string
b = "hello world, how are you, hello to you too"
print(b[-5:-2])



# Uppercase
b = "hello world, how are you, hello to you too"
print(b.upper())

# Lowercase
b = "hello world, how are you, hello to you too"
print(b.lower())

# strip => removes whitespace between words
b = "hello world, how are you, hello to you too"
print(b.strip())
b.strip()

# replace => replace string elements
b = "hello world, how are you, hello to you too"
print(b.replace("h", "H"))

# split String
b = "hello world1 how are you1 hello to you1 too"
print(b.split("1"))

# use + to concatenate
a = "juke"
b = "box"
print(a.upper() + b.upper())

# use format to combine strings with numbers
# the method formats the numbers to strings in the {} holders

age = 42
text = "Sammy is {} years old"
print(text.format(age))




# escape characters; used to insert illegal string elements
# i.e. use backslash \ to insert "" as Text
text = "jupiter and the slut were often known as \"idiots\" to the public"
print(text)

# other escape characters
\'	Single Quote
\\	Backslash
\n	New Line
\r	Carriage Return
\t	Tab
\b	Backspace
\f	Form Feed
\ooo	Octal value
\xhh	Hex value

capitalize()	# Converts the first character to upper case
casefold()	# Converts string into lower case
center()	# Returns a centered string
count()	# Returns the number of times a specified value occurs in a string
encode()	# Returns an encoded version of the string
endswith()	# Returns true if the string ends with the specified value
expandtabs()	# Sets the tab size of the string
find()	# Searches the string for a specified value and returns the position of where it was found
format()	# Formats specified values in a string
format_map()	# Formats specified values in a string
index()	# Searches the string for a specified value and returns the position of where it was found
isalnum()	# Returns True if all characters in the string are alphanumeric
isalpha()	# Returns True if all characters in the string are in the alphabet
isdecimal()	# Returns True if all characters in the string are decimals
isdigit()	# Returns True if all characters in the string are digits
isidentifier()	# Returns True if the string is an identifier
islower()	# Returns True if all characters in the string are lower case
isnumeric()	# Returns True if all characters in the string are numeric
isprintable()	# Returns True if all characters in the string are printable
isspace()	# Returns True if all characters in the string are whitespaces
istitle()	# Returns True if the string follows the rules of a title
isupper()	# Returns True if all characters in the string are upper case
join()	# Joins the elements of an iterable to the end of the string
ljust()	# Returns a left justified version of the string
lower()	# Converts a string into lower case
lstrip()	# Returns a left trim version of the string
maketrans()	# Returns a translation table to be used in translations
partition()	# Returns a tuple where the string is parted into three parts
replace()	# Returns a string where a specified value is replaced with a specified value
rfind()	# Searches the string for a specified value and returns the last position of where it was found
rindex()	# Searches the string for a specified value and returns the last position of where it was found
rjust()	# Returns a right justified version of the string
rpartition()	# Returns a tuple where the string is parted into three parts
rsplit()	# Splits the string at the specified separator, and returns a list
rstrip()	# Returns a right trim version of the string
split()	# Splits the string at the specified separator, and returns a list
splitlines()	# Splits the string at line breaks and returns a list
startswith()	# Returns true if the string starts with the specified value
strip()	# Returns a trimmed version of the string
swapcase()	# Swaps cases, lower case becomes upper case and vice versa
title()	# Converts the first character of each word to upper case
translate()	# Returns a translated string
upper()	# Converts a string into upper case
zfill()	# Fills the string with a specified number of 0 values at the beginning

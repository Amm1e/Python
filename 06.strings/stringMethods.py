# Strings are immutable
#split converts a string to list using a seprator
#join function joins a list to form a string using seperator

name="hello world"
print(name.upper(), name , sep="....")# default separator is space.
print(name.capitalize())
print(name.title())
text="Apple,Orange,Banana,Grapes"
text2="Apple Orange Banana Grapes"
text3="Apple . Orange . Banana . Grapes"
print(text.split(","))
print(len(text.split(",")))
print(len(text2.split()))
print(text2.split())
print(len(text3.split(".")))
print(text3.split("."))
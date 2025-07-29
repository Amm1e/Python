#format fucntion
text="Good morning {}. You are {} years old. {} is a beautiful day"
# name=(input("Enter the name ")).strip()
name=(input("Enter the name "))
age=int(input("Enter your age "))
day=(input("What day is today ")).strip()   
print(text.format("Ammie", 90,"Tuesday"))
print(text.format(name, age , day))

# this could be done using fstrings
print("===============using fstring=================")
print(f"Good morning {name}. You are {age} years old. {day} is a beautiful day")
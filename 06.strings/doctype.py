a=9
age = int(input("Enter your age "))
print(f"value of a before Global {a}")

def printage(age):
    """This function helps to tell abot local and global variable
            Even though the age is inputted by the consumer the function would always condsider the age which is closest of its scope here it takes local age and then we use GLOBAL for a"""
    age =29
    global a
    a= 89
    print(f"your age is {age}")
    print(printage.__doc__)

printage(age)
print(a)
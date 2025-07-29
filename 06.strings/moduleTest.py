import requests
import mymodule
def greetings(name):
    ''' This function greets the user'''
    print(f"Greetings of day {name}")

name=input("Enter your name ")
mymodule.hello(name)

print(requests.get("https://www.google.com"))



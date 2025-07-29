# Walrus operator is used to assign value of a function while it executes

import random

while (a:=input("Enter the Value:")):
    if a=='q':
        break

def returnNum():
    return random.random()*100.6

while(a:=returnNum())>10: #Assign the return value of returnNum() to a, and then check if a > 10
    print(a)
print(f"bye value of a was {a}")




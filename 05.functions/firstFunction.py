def add(a, b, plus=1):
    return a+b+plus

#default argument:
# ++++++++++++++++++++++++++++++
print(add(3,4))
#default value of plus is overridden
print(add(3,4,5))
# +++++++++++++++++++++++++++++++

#keyword Argument where the paramerter name is also given

print(add(b=9,a=4,plus=9))
print(add(plus=9,b=9,a=4))


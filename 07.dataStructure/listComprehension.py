a=5
b=6
table5=[]
for i in range(1,11):
    table5.append(a*i)
print(table5)

# this could also be done in 1 line

table6 = [b*i for i in range(1,11)]
print(table6)
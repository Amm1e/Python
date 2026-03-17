numbers = [1, 2, 3, 2, 4, 1, 5, 3]

# Task 1: Print unique numbers using a set
# Task 2: Print how many times each number appeared

set1 =set(numbers)
print(set1)
d1={}
i=1
for number in numbers:
    if number in d1.keys():
        d1[number]+=1
    else:
        d1[number]=1
print(d1)
 




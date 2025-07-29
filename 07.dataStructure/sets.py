set ={32,43,"amritansh"}
print(set)
# print(set[0]) This would give error as sets are unordered.
#set.remove(33) can only remove if the element present in set else gives error.
set.discard(33)  #dont giver error.

set.add(34) #34 could be added anywhere as the set is unordered.

print(set)

set.update("amritansh")
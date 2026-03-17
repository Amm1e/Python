from collections import Counter

numbers = [1, 2, 3, 2, 4, 1, 5, 3]

# Task 1: Print unique numbers using a set
# Task 2: Print how many times each number appeared

unique = set(numbers)
count = Counter(numbers)

print(unique)
print(dict(count))

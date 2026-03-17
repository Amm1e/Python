numbers = [2, 7, 11, 15]
target = 9

# Find two numbers that add up to target
# Output: [2, 7]
dic={}
for number in numbers:
    required = target - number
    if required in dic.keys():
        print ([number, required])
    else:
        dic[number]=1
        


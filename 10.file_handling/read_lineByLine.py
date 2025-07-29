try:
    f = open("Isreal.txt","r")
except FileNotFoundError: 
    print("File does not exits")
    exit()
for line in f:
    print(line)
f.close()
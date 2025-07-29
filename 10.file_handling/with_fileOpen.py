#with is known as context manager
with open("Isreal.txt","r")as f:
    print(f.read())
#when file opened using wiht you need not to close file it automaticallly gets closed
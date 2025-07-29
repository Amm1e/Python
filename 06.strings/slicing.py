# -ve indices are nothing but -ve plus length of string.
name="Amritansh"
print(name[0:8])
print(name[0:-1]) #-1+9=8 name[-1]= name[8]

# indexing has a third parmeter which is skiping of character
print(name[0:8:2]) #will first slice the string then print skiping 2-1 characters
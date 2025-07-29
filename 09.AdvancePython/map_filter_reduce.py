from functools import reduce


l2=[2,3,4,5,6]
def square(x):
    return x*x
l3=map(square, l2) #prints map location
l4=list(map(square, l2)) #prints content of map
l5=list(map(lambda x: x*x , l2)) # map reduce using lambda, map fuction takes a functon and iterable in parameters and apply the function to every  object of the iterable.
print(l3)
print(l4)
print(l5)


l1=[3.5,23,2342,5,2,5,1,55,88,978,9,5,6,4,53,]

even =  list(filter(lambda x:x%2==0,l1))#filter funtions filter out from iteratables and return the values which satisfy the condition same as map it retuns object which we typecast to list
print(even)


print (reduce(lambda x,y: x+y, l1))#reduce reduces the list to a smaller value as in this case it would sum the entire list and retun the sum, unlike map and filter it does not return object it returns value
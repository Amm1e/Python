# fibonacci series
# 0,1,1,2,3,5,8,13,21.......n=(n-2)+(n-1) nth term 1st term=0 2nd term = 1
# 1,1,2,3,4,5,6,7,8

def fibo(n):
    if (n == 0 or n == 1):
     return n
    return fibo(n-1) + fibo(n-2)
n= int(input("Enter the number:"))
print(fibo(n))
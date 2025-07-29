def repeat(a):
    def decorator(func):
        def Wrapper(n):
             for i in range(a):
                print("T able start:")
                func(n)
                print("Table end.")
        return Wrapper
    return decorator

@repeat(4)
def table(n):
    for i in range(1,11):
        print(n*i)

table(3)
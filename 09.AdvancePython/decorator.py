def decorator(func):
  
    def wrapper(name):
        print("befor sayHello function")
        func(name)
        print("after sayHello function")
    
    return wrapper


@decorator
def sayHello(name):
    print(f"Hello {name}")

sayHello("Ammie")
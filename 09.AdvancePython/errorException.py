try:
    name = input("Enter your name ");
    
    if name.isdigit():
        raise ValueError("Name should have Characters")



    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    print(f"{a}/{b}={a/b}")



except ValueError:
    print("Only Numbers can be inputed")

# except ZeroDivisionError:
#     print("Dividing by zero is not permitted")

except Exception as e:
    print(e)

else:
    print("Division finished")

finally:
    print(f"Good day!! {name if name in locals() else ''}")

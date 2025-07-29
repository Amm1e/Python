#property that the nested function remembers the variable of the outer function even the outer function has stopped executing.

def egg():
    color = "brown"
    def buy():
        print(f"You bought a {color} egg")
    return buy

egg()()



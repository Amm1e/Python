def marks(**kwargs):
    for name, score in kwargs.items():
        print(f"{name} attained a score ofa {score}")

marks(ram=90, syam=99)
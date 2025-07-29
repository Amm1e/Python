# you need to pass args before kwargs

def func1(*args, **kwargs):
    print(args)
    print(kwargs)

func1(3,3,44,'3f', ram=00, syam="33")
def myfunc (*args):
    for values in args:
        print (values, end='\n')
    if args:
        print ()

def myfunc2 (**kwargs):
    for k, v in kwargs.items():
        print (k, v, sep= '->', end = ' ')
    if kwargs:
        print ()

def myfunc3(*args,**kwargs):
    if args:
        for val in args:
            print (val, end = " ")
    if kwargs:
        for k,v in kwargs.items():
            print (k, v, sep = '=>', end = " ")


def apply (func:object, value:object) -> object:
    return func(value)

def outer ():
    def inner ():
        print ("This is inner function")
    print ("This is outer, returning inner.")
    return inner


#print (apply(type, 'Marvin'))
#i = outer ()
#i()
#myfunc(2,3,'prog')
#print ("hello world")

myfunc3("string", a = 10, b = 3)

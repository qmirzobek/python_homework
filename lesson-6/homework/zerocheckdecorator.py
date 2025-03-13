


def div(a,b):
    return a/b

def check(func):
    # if(b==0):
    #     print()
    def wrapper(a,b):
        try:
            print(func(a,b))           
        except ZeroDivisionError:
            print("Denominator can't be zero")
            
    # wrapper.__name__=func.__name__
    return wrapper
a=input("Enter number a and b input: ")
print('output: ', end="")
# print(a)
a=check(div)
a(6,3)

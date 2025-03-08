# task5
def is_prime(n):
    try:
        n=int(n)
        for i in range(2,n):
            if(n%i==0):
                return False
        else:
            return True
    except:
        print("An error occured")


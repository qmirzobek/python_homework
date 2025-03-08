# task 3
try: 
    while True:
        number=int(input('Enter a positive integer: '))
        if(number>=0):
            break
    for i in range(1,(number+1)):
        if(number%i==0):
            print(f"{i} is a factor of {number}")

except:
    print('Error occured')




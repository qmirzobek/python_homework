a=input("Enter a string: ")

f=False
for i in range(0,len(a)):
    if((a[i]).isdigit()):
        f=True
        break
if(f):
    print('It contains digit')
else:
    print('It doesn\'t contain digit')
    

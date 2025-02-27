import string
a=input('Enter a string: ')
b=''
for i in range(len(a)):
    if(a[i]!=" "):
        b+=a[i]

print(b)



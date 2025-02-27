import string
a=input("Enter a string: ")
c=input("Enter a character: ")
b=''
# b=a.split(c)
for i in range(len(a)):
    if(a[i]!=c):
        b+=a[i]

# b=a.rstrip(c)
print(b)



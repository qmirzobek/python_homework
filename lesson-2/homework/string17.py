


a=input("Enter a string: ")
b=''
for i in range(len(a)):
    if(a[i]=="a" or a[i]=="e" or a[i]=="u" or a[i]=="i" or a[i]=="o"):
        b+="*"
    else:
        b+=a[i]
print(b)








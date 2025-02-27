a=input('Enter a string: ')
b=input('Enter another string: ')
l=0
f=False
for i in range(len(a)):
    l=0
    for j in range(i,len(a)):
        if a[j]==b[j]:
            l+=1
    if(l==len(b)):
        f=True
        break

if(f):
    print("a contains b")
else:
    print("a does not contain b")
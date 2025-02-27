a=input()
f=True
for i in range(0,len(a)):
    if(a[i]!=a[len(a)-1-i]):
        f=False
        break
if(f):
    print("Palindrome")
else:
    print("Not a palindrome")
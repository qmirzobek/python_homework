a=int(input("Enter number of words you want to enter: "))
c=""
i=1
while(True):
    b=input("Enter a word: ")
    c+=b
    if(a<=i):
        break
    i+=1
    c+=","
print(c)





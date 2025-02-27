a=input("Enter a string: ")

w=a.split()
c=""
for i in range(len(w)):
    c+=w[i][0]
print(c)


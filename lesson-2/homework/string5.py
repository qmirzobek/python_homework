a=input()
vowels=0
consonants=0
for i in range(0,len(a)):
    if(a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u'):
        vowels+=1
    else:
        consonants+=1
print("Vowels: ",vowels)
print("Consonants: ",consonants)

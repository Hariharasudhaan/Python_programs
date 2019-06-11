s=input("Enter the String:")                                                    #Getting String from User
l=[]
z=[]
s=s.lower()                                                                     #Change into Lowercase
for i in s:
    z.append(i)
print(z)
for k in z:                                                                     #Loop for Identifying Vowels
    if(k=='a' or k=='e' or k=='i' or k=='o' or k=='u'):
        l.append(k)
print(l)
n=len(l)                                                                        #Finding Length of the Vowel Array
x=n-1
for j in range(0,len(z),1):                                                     #Loop for Swapping Vowels
    if(x==n-1):
         if(z[j]=='a' or z[j]=='e' or z[j]=='i' or z[j]=='o' or z[j]=='u'):
            z[j]=l[x]
            x=0
    else:
        if(z[j]=='a' or z[j]=='e' or z[j]=='i' or z[j]=='o' or z[j]=='u'):
            z[j]=l[x]
            x=x+1
       
print(z)


s=input("Enter the string:")                #Getting a String
n=int(input("Enter the index number:"))     #Getting the Index Value
l=s.split(' ')
z=l[n]
x=list(z)
c=0
for i in z:                                 #Loop for counting the size of the Word
    c=c+1
j=c-1
for i in range(0,c//2,1):                   #Loop for reversing the word
    if(i!=j):
        temp=x[i]
        x[i]=x[j]                           #swapping Process
        x[j]=temp
    j=j-1
x=''.join(x)                                #Coverting list to string
print(s.replace(z,x))                       #Replacing the Old Word with New Word

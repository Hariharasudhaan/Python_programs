a=[]                                            #Inistializing Array
length=0
n=int(input("Enter the size of an Array:"))     #Getting size of an Array
for i in range(0,n,1):
    z=input("Enter the word:")
    a.append(z)
for i in range(0,n,1):
    count=0
    for j in range(0,n,1):
        if(a[i]==a[j]):                         #Finding Twice Elements
            count=count+1
    if(count==2):
        length=length+1
print(length//2)                                #Print the Length 

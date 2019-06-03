n=int(input("Enter Size of an array:"))     #getting Size of an Array
l=[]
for i in range(0,n,1):                      #Loop for getting Array
    z=int(input("Enter the value:"))
    l.append(z)
temp=0                                      #Temporary variable for Swapping
j=n-1
for i in range(0,n//2,1):                   #Loop for Swapping
    if(i!=j):
        temp=l[i]
        l[i]=l[j]
        l[j]=temp
    j=j-1
print(l)

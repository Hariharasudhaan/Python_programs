n=int(input("Enter Size of an array:"))          #getting Size of an Array
a=[]
for i in range(0,n,1):                           #Loop for getting Array
    z=int(input("Enter the element:"))
    a.append(z)
k=int(input("Enter the Kth element:"))           #Getting Kth value from the User
a.sort()                                         #Sorting the given Array
print(a[k-1])

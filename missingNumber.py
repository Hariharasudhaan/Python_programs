n=int(input("Enter Size of an array:"))          #getting Size of an Array
a=[]
k=1
for i in range(0,n,1):                           #Loop for getting Array
    z=int(input("Enter the element:"))
    a.append(z)
a.sort()                                         #Sorting the Array
for i in range(0,n,1):                           #Loop for Finding the Missing Element
    if(a[i]==k):
        k=k+1
    else:
        print(k)
        break
if(k==n+1):                                      #If No Missing Number,print "-1"
    print("-1")
    

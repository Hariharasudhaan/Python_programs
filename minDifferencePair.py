n=int(input("Enter size of an Array:"))
a=[]
for i in range(0,n,1):                              #Getting Array Elemnts
    z=int(input("Enter the element:"))
    a.append(z)
a.sort()                                            #Sorting the Array
mini=a[1]-a[0]                                      #Initialize Minimum value as Difference of first two array elements
for i in range(0,n,1):
    for j in range(i+1,n,1):
        x=a[j]-a[i]                                 #Loop for finding Minimum Difference 
        if(mini>x):
            mini=x
print(mini)                                         #Print the Minimum Value
            
        

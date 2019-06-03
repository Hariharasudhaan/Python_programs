n=int(input("Enter Size of an array:"))          #getting Size of an Array
a=[]
for i in range(0,n,1):                           #Loop for getting Array
    z=int(input("Enter the element:"))
    a.append(z)
for i in range(0,n,1):                           #Loop for Finding First Repeatation
    z=a[i]
    for j in range(i+1,n,1):    
        if(z==a[j]):
            ans=z                                #If the element repeated in the array then make answer=1 and Break the Statement
            break
print(ans)

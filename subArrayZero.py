n=int(input("Enter Size of an array:"))          #getting Size of an Array
a=[]
c=0
for i in range(0,n,1):                           #Loop for getting Array
    z=int(input("Enter the element:"))
    a.append(z)
for i in range(0,n and c!=1,1):                  #Loop for Calculating Subset for Zero
    sum=a[i]
    for j in range(i+1,n,1):
        sum=sum+a[j]    
        if(sum==0):
            c=1                                  #If the Sum is Zero make c=1 and Break the Statement
            break
        else:
            c=0
if(c==1):
    print("True")
else:
    print("False")

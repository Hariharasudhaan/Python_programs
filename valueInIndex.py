n=int(input("Enter Size of an array:"))     #getting Size of an Array
l=[]
for i in range(0,n,1):                      #Loop for getting Array
    z=int(input("Enter the value:"))
    l.append(z)
max=max(l)                                  #To find Maximum Value
for j in range(0,max+1,1):
        if(j in l):
            print(j)
        else:
            print(-1)

n=int(input("Enter Size of an array:"))          #getting Size of an Array
a=[]
for i in range(0,n,1):                           #Loop for getting Array
    z=int(input("Enter the element:"))
    x=z*z                                        #Square the given Value
    a.append(x)
a.sort()                                         #Sort the Array
for i in a:
    print(i)                                     #Print the Values separately
    

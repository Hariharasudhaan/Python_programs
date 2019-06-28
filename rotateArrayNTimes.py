a=[]                                                #Initialize Array
n=int(input("Enter the size of an Array:"))
x=int(input("Enter the D element:"))
for i in range(0,n,1):
    z=int(input("Enter the Element:"))              #Loop for Gettng Array Elements
    a.append(z)
for i in range(0,x,1):
    temp=a[0]                                       #Assining First value as Temp
    for j in range(1,n,1):
        a[j-1]=a[j]                                 #Swapping Values to Previous Index
    a[n-1]=temp                                     #Assining First Value to Last Index
print(a)

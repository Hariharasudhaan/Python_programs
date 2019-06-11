n=int(input("Enter Size of an array:"))          #getting Size of an Array
a=[]
le=[]
gr=[]
eq=[]
c=0
for i in range(0,n,1):                           #Loop for getting Array
    z=int(input("Enter the element:"))
    a.append(z)     
a.sort()                                         #Sorting the Array
x=int(input("Enter the pivot Value:"))           #Getting Pivot value form the User
for i in a:             
    if(i<x):
        le.append(i)
    elif(i>x):
        gr.append(i)                             #Loop for Partion
    else:
        eq.append(i)
le.sort(reverse=True)                            #Descending the Array
gr.sort(reverse=True)
print(le+eq+gr)                                  #Print the Result by Combining all the Array's

n=int(input("Enter size of an array:"))
l=[]
for i in range(0,n,1):                              #Loop for Array
    x=int(input("Enter the element:"))
    l.append(x)
l1= sorted(l, key = l.count,reverse=False)          #Sorting Based on Frequecy
l1.reverse()                                        #Reversing the List 
print(l1)

from itertools import groupby, count                                        #Importing Functions
n=int(input("Enter size of an array:"))
l=[]
for i in range(0,n,1):                                                      #Loop for Array
    x=int(input("Enter the element:"))
    l.append(x)
l.sort()                                                                    #Sorting an Array
c = count()
val = max((list(g) for _, g in groupby(l, lambda x: x-next(c))), key=len)
print(len(val))                                                             #Print The Count as Result

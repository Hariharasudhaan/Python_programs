s1=input("Enter the String 1:")                 #Getting String 1 from User
s2=input("Enter the String 2:")                 #Getting String 2 from User
l1=[]
l2=[]
c=0
for i in s1:                                    #Loop for Splitting String 1
    l1.append(i)
for i in s2:                                    #Loop for Splitting String 2
    l2.append(i)
if(len(l1)==len(l2)):
    for j in range(0,len(l2),1):                #Loop for Rotation
        temp=l2[0]
        for i in range(1,len(l2),1):            #Loop for Swapping String 2
            l2[i-1]=l2[i]
        l2[i]=temp
        if(l2 == l1):                           #If List 1 and List 2 are Equal,print True
            c=1
        if(c==1):
            print("True")
            break
    if(c!=1):
        print("False")
        
else:
 print("False")
